# Gerenciamento de Ferramentas - Fábrica

Este projeto consiste em uma API construída com **FastAPI** que processa arquivos de texto contendo a descrição de problemas em uma fábrica, utiliza o GPT-4 para selecionar as ferramentas necessárias, gera um arquivo CSV com as ferramentas selecionadas e verifica o próximo horário em que essas ferramentas estarão disponíveis no almoxarifado.

## Funcionalidades

- Upload de arquivos `.txt` contendo a descrição do problema.
- Seleção automática de ferramentas utilizando GPT-4.
- Geração de arquivo CSV com as ferramentas escolhidas e seus códigos SAP.
- Verificação do primeiro horário disponível para uso das ferramentas no almoxarifado.

## Estrutura do Projeto

```bash
projeto-fabrica/
│
├── app/
│   ├── __init__.py                 # Inicialização do pacote
│   ├── main.py                     # Ponto de entrada da aplicação FastAPI
│   ├── api.py                      # Rotas da API
│   ├── csv_loader.py               # Manipulação dos arquivos CSV
│   ├── gpt_service.py              # Integração com OpenAI GPT para escolha de ferramentas
│   ├── file_handler.py             # Manipulação de arquivos .txt e geração de CSV
│
├── data/                           # Diretório contendo os arquivos CSV existentes
│   ├── ColinhadeCodigos SAP.csv    # CSV das ferramentas e códigos SAP
│   └── almoxarifado.csv            # CSV das reservas por hora
│
├── temp_files/                     # Diretório temporário para arquivos .txt e CSV gerados
│   └── ferramentas_selecionadas.csv # Arquivo CSV gerado com as ferramentas selecionadas
│
├── openai_key.txt                  # Arquivo contendo a chave da API do OpenAI
├── requirements.txt                # Dependências do projeto
├── README.md                       # Documentação do projeto
