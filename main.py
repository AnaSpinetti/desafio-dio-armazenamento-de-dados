import streamlit as st
from azure.storage.blob import BlobServiceClient
import os
import pyodbc
import uuid
import json
from dotenv import load_dotenv

# Carregando as variaveis de ambiente
load_dotenv()

BlobConnectionString = os.getenv('BLOB_CONNECTION_STRING')
BlobContainerName = os.getenv('BLOB_CONTAINER_NAME')
BlobAccountName = os.getenv('BLOB_ACCOUNT_NAME')

SqlServer = os.getenv('SQL_SERVER')
SqlDatabase = os.getenv('SQL_DATABASE')
SqlUser = os.getenv('SQL_USER')
SqlPassword = os.getenv('SQL_PASSWORD')

st.title('Cadastro de Produtos')

# Definindo o layout da página
product_name = st.text_input('Nome do produto')
product_price = st.number_input('Preço do Produto', min_value=0.0, format='%.2f')
product_description = st.text_area('Descrição do Produto')
product_image = st.file_uploader('Imagem do Produto', type=['jpg', 'jpeg', 'png'])


if st.button('Salvar Produto'):
    return_message = 'Produto cadastrado com sucesso!'

st.header('Produtos Cadastrados')

if st.button('Listar Produtos'):
    return_message = 'Produtos listados com sucesso!'

