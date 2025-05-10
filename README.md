# desafio-dio-armazenamento-de-dados
Dio Desafio: Armazenando dados de um E-Commerce na Cloud

Este projeto é uma aplicação web desenvolvida com **Streamlit** para gerenciar o cadastro de produtos. Ele utiliza o **Azure Blob Storage** para armazenar imagens e o **SQL Server** para gerenciar os dados dos produtos.

## 🚀 Funcionalidades

- **Cadastro de Produtos**: Insira o nome, preço, descrição e imagem de um produto.
- **Armazenamento de Imagens**: As imagens são enviadas para o **Azure Blob Storage**.
- **Listagem de Produtos**: Exibe os produtos cadastrados com suas respectivas informações e imagens.
- **Banco de Dados**: Os dados dos produtos são armazenados em um banco de dados **SQL Server**.

---

## 🛠️ Tecnologias Utilizadas

- **[Streamlit](https://streamlit.io/)**: Framework para criação de aplicações web interativas.
- **[Azure Blob Storage](https://azure.microsoft.com/pt-br/services/storage/blobs/)**: Serviço de armazenamento de objetos na nuvem.
- **[SQL Server](https://www.microsoft.com/pt-br/sql-server/)**: Banco de dados relacional.
- **[Python](https://www.python.org/)**: Linguagem de programação principal.
- **Bibliotecas Python**:
  - `azure-storage-blob`: Para integração com o Azure Blob Storage.
  - `pyodbc`: Para conexão com o SQL Server.
  - `dotenv`: Para gerenciar variáveis de ambiente.
  - `uuid`: Para geração de identificadores únicos.

---

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter:

1. **Python 3.7+** instalado.
2. Uma conta no **Azure** com um **Blob Storage** configurado.
3. Um banco de dados **SQL Server** configurado.
4. As seguintes variáveis de ambiente configuradas no arquivo `.env`, no projeto temos o .env_example que pode ser utilizado:
   ```env
   BLOB_CONNECTION_STRING=<sua_connection_string>
   BLOB_CONTAINER_NAME=<nome_do_container>
   BLOB_ACCOUNT_NAME=<nome_da_conta_blob>
   SQL_SERVER=<servidor_sql>
   SQL_DATABASE=<nome_do_banco>
   SQL_USER=<usuario_sql>
   SQL_PASSWORD=<senha_sql>
   ```

---

## 🖥️ Como executar o projeto

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/armazenamento_cloud_desafio_azure.git
   cd armazenamento_cloud_desafio_azure
   ```

2. **Instale as dependências**:
   ```bash
   pip install -r requisitos.txt
   ```

3. **Configure o arquivo `.env`**:
   - Crie um arquivo `.env` na raiz do projeto e preencha com as variáveis de ambiente necessárias.

4. **Execute o aplicativo**:
   ```bash
   streamlit run main.py
   ```

5. **Acesse no navegador**:
   - O Streamlit abrirá automaticamente no navegador. Caso contrário, acesse: [http://localhost:8501](http://localhost:8501).

---

## 📂 Estrutura do Projeto

```plaintext
📦 armazenamento_cloud_desafio_azure
├── main.py               # Código principal da aplicação
├── requirements.txt      # Dependências do projeto
├── .env                  # Variáveis de ambiente (não incluído no repositório), mas pode se basear no arquivo .env_example;
└── README.md             # Documentação do projeto
```

---

## 📝 Notas Importantes

- **Permissões do Blob Storage**: Certifique-se de que o container do Blob Storage está configurado como **publicamente acessível** para que as imagens possam ser exibidas.
- **Banco de Dados**: A tabela `Produtos` deve ser criada no SQL Server com a seguinte estrutura:
  ```sql
  CREATE TABLE Produtos (
      id INT PRIMARY KEY IDENTITY(1,1),
      nome NVARCHAR(255) NOT NULL,
      preco FLOAT NOT NULL,
      descricao NVARCHAR(MAX),
      imagem_url NVARCHAR(MAX)
  );
  ```

---

## 🛡️ Segurança

- **Variáveis de Ambiente**: Nunca exponha suas credenciais diretamente no código. Use o arquivo `.env` para gerenciá-las.
- **Acesso ao Blob Storage**: Use políticas de acesso restritas para proteger seus dados.

---

## 📖 Referências

- [Documentação do Streamlit](https://docs.streamlit.io/)
- [Documentação do Azure Blob Storage](https://learn.microsoft.com/pt-br/azure/storage/blobs/)
- [Documentação do PyODBC](https://github.com/mkleehammer/pyodbc)

---

## 🧑‍💻 Autor

**Ana Spinetti**  
[GitHub](https://github.com/anaspinetti) | [LinkedIn](https://linkedin.com/in/ana-spinetti)


