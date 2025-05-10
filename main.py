import streamlit as st
from azure.storage.blob import BlobServiceClient
import os
import pyodbc
import uuid
from dotenv import load_dotenv
from urllib.parse import quote

# Carregando as variáveis de ambiente
load_dotenv()

BlobConnectionString = os.getenv('BLOB_CONNECTION_STRING')
BlobContainerName = os.getenv('BLOB_CONTAINER_NAME')
BlobAccountName = os.getenv('BLOB_ACCOUNT_NAME')

SqlServer = os.getenv('SQL_SERVER')
SqlDatabase = os.getenv('SQL_DATABASE')
SqlUser = os.getenv('SQL_USER')
SqlPassword = os.getenv('SQL_PASSWORD')

# Função para conectar ao banco SQL Server
def connect_to_database():
    conn_str = (
        "DRIVER={SQL Server};"
        f"SERVER={SqlServer};"
        f"DATABASE={SqlDatabase};"
        f"UID={SqlUser};"
        f"PWD={SqlPassword};"
        "TrustServerCertificate=yes;"
    )
    return pyodbc.connect(conn_str)

# Upload da imagem para o Blob Storage
def upload_blob(file):
    blob_service_client = BlobServiceClient.from_connection_string(BlobConnectionString)
    container_client = blob_service_client.get_container_client(BlobContainerName)
    blob_name = str(uuid.uuid4()) + "_" + file.name
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(file.read(), overwrite=True)
    encoded_blob_name = quote(blob_name, safe='')
    image_url = f"https://{BlobAccountName}.blob.core.windows.net/{BlobContainerName}/{encoded_blob_name}"
    return image_url

# Inserir produto no banco de dados
def insert_product(product_name, product_price, product_description, product_image):
    try:
        image_url = upload_blob(product_image)
        conn = connect_to_database()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Produtos (nome, preco, descricao, imagem_url) VALUES (?, ?, ?, ?)",
            (product_name, product_price, product_description, image_url)
        )
        conn.commit()
        conn.close()
        st.success("✅ Produto cadastrado com sucesso!")
        return True
    except Exception as e:
        st.error(f"❌ Erro ao inserir produto: {e}")
        return False

# Buscar produtos
def list_products():
    try:
        conn = connect_to_database()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Produtos")
        products = cursor.fetchall()
        conn.close()
        return products
    except Exception as e:
        st.error(f"❌ Erro ao listar produtos: {e}")
        return []

def list_products_screen():
    products = list_products()
    if products:
        for product in products:
            image_url = product[4].strip()
            #st.write(f"🔗 URL da imagem: {image_url}")
            if image_url:
                try:
                    st.image(image_url, width=100)
                except Exception as e:
                    st.write(f"❌ Erro ao carregar a imagem: {e}")
            else:
                st.write("🖼️ Imagem não disponível")
            st.write(f"**Nome:** {product[1]}")
            try:
                preco = float(product[2])
                st.write(f"**Preço:** R$ {preco:.2f}")
            except (ValueError, TypeError):
                st.write("**Preço:** Valor inválido")
            st.write(f"**Descrição:** {product[3] if product[3] else 'Sem descrição.'}")
            st.write("---")
    else:
        st.info("📭 Nenhum produto cadastrado.")

# --- Streamlit UI ---
st.title('📦 Cadastro de Produtos')

product_name = st.text_input('Nome do produto')
product_price = st.number_input('Preço do Produto', min_value=0.0, format='%.2f')
product_description = st.text_area('Descrição do Produto')
product_image = st.file_uploader('Imagem do Produto', type=['jpg', 'jpeg', 'png'])

if st.button('Salvar Produto'):
    if product_name and product_price and product_description and product_image:
        insert_product(product_name, product_price, product_description, product_image)
        
    else:
        st.warning("⚠️ Preencha todos os campos antes de salvar.")

st.header('📋 Produtos Cadastrados')

if st.button('Listar Produtos'):
    list_products_screen()
