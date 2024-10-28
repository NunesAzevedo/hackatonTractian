import csv
import os
from .gpt_service import escolher_ferramentas

# Caminho do arquivo de problema e CSV de ferramentas
CAMINHO_PROBLEMA_TXT = 'temp_files/exemplo_problema.txt'
CAMINHO_CSV_FERRAMENTAS = 'temp_files/ferramentas_selecionadas.csv'


def ler_arquivo_txt(caminho: str) -> str:
    """
    Lê o arquivo .txt contendo o problema.

    Parâmetros:
        caminho (str): Caminho do arquivo .txt.
    
    Retorna:
        str: Conteúdo do arquivo .txt.
    """
    try:
        with open(caminho, 'r') as file:
            print(f"DEBUG: Lendo o arquivo {caminho}")
            return file.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo {caminho} não encontrado.")
        return ""

def processar_arquivo_txt() -> list:
    """
    Lê o arquivo de problema e usa o GPT para selecionar as ferramentas necessárias.

    Retorna:
        list: Lista de ferramentas escolhidas.
    """
    texto_problema = ler_arquivo_txt(CAMINHO_PROBLEMA_TXT)
    if not texto_problema:
        print("Erro: Nenhum texto de problema foi encontrado.")
        return []
    
    # Usa o GPT para identificar as ferramentas necessárias
    ferramentas_escolhidas = escolher_ferramentas(texto_problema)
    
    # Exibe as ferramentas escolhidas no terminal
    print("DEBUG: Ferramentas escolhidas pelo GPT:", ferramentas_escolhidas)
    
    return ferramentas_escolhidas

def gerar_csv_ferramentas(ferramentas_escolhidas: list):
    """
    Gera um arquivo CSV com as ferramentas escolhidas pelo GPT.

    Parâmetros:
        ferramentas_escolhidas (list): Lista de dicionários contendo 'Categoria', 'Descrição' e 'Código SAP' das ferramentas.
    """
    if not ferramentas_escolhidas:
        print("DEBUG: Nenhuma ferramenta escolhida para salvar no CSV.")
        return
    
    print("DEBUG: Iniciando a geração do arquivo CSV com as ferramentas selecionadas.")
    

    # Certificar-se de que o diretório temp_files existe
    os.makedirs(os.path.dirname(CAMINHO_CSV_FERRAMENTAS), exist_ok=True)

    # Cria o arquivo CSV com as ferramentas escolhidas
    with open(CAMINHO_CSV_FERRAMENTAS, mode='w', newline='') as csvfile:
        fieldnames = ['Categoria', 'Descrição', 'Código SAP']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for ferramenta in ferramentas_escolhidas:
            writer.writerow({
                'Categoria': ferramenta['Categoria'],
                'Descrição': ferramenta['Descrição'],
                'Código SAP': ferramenta['Código SAP']
            })
    
    print(f"DEBUG: Arquivo CSV gerado em: {CAMINHO_CSV_FERRAMENTAS}")
