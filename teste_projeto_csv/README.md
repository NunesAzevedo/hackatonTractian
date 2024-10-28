# Projeto Fábrica - Gerenciamento de Ferramentas e Reservas

Este projeto é uma API construída com **FastAPI** para gerenciar ferramentas e suas reservas em uma fábrica. Os dados das ferramentas e suas reservas são carregados de arquivos CSV em vez de um banco de dados.

## Funcionalidades

- Listar todas as ferramentas disponíveis.
- Consultar as reservas de uma ferramenta específica por código SAP.

## Estrutura do Projeto

- `app/`: Contém a aplicação principal, com rotas e carregamento dos arquivos CSV.
- `data/`: Diretório onde estão armazenados os arquivos CSV (dados das ferramentas e reservas).
- `tests/`: Testes automatizados para garantir o correto funcionamento das rotas.

## Requisitos

- **Python 3.7+**
- As dependências listadas no arquivo `requirements.txt`

## Como Executar

### 1. Instalar as Dependências

Crie um ambiente virtual e instale as dependências:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
