import openai
import os
import pandas as pd
from .csv_loader import carregar_ferramentas

# Função para carregar a chave da API do arquivo txt
def carregar_api_key(caminho: str) -> str:
    """
    Lê a API Key do arquivo txt.

    Parâmetros:
        caminho (str): Caminho para o arquivo txt contendo a API Key.
    
    Retorna:
        str: API Key.
    """
    try:
        with open(caminho, 'r') as file:
            return file.read().strip()
    except Exception as e:
        print(f"Erro ao carregar a API Key: {e}")
        return ""

# Carregar a API key da OpenAI a partir do arquivo .txt
openai.api_key = carregar_api_key('openai_key.txt')

def escolher_ferramentas(texto_problema: str) -> list:
    """
    Usa o GPT para escolher as ferramentas necessárias com base na descrição do problema.

    Parâmetros:
        texto_problema (str): Texto com a descrição do problema.
    
    Retorna:
        list: Lista de dicionários contendo 'Categoria', 'Descrição' e 'Código SAP' das ferramentas.
    """
    print("DEBUG: Carregando as ferramentas disponíveis.")
    
    # Carrega as ferramentas disponíveis
    ferramentas_df = carregar_ferramentas()

    # Cria a mensagem de entrada para o modelo de chat GPT
    mensagens = [
        {"role": "system", "content": "Você é um assistente que ajuda a selecionar ferramentas para consertos em uma fábrica."},
        {"role": "user", "content": f"Com base no seguinte problema, identifique quais ferramentas serão necessárias:\n\n{texto_problema}\n\nFerramentas disponíveis:\n{ferramentas_df[['Descrição do Material/Equipamento', 'Código SAP']].to_string(index=False)}\n\n"}
    ]

    print("DEBUG: Enviando o seguinte prompt para o GPT:\n", mensagens)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Pode usar "gpt-3.5-turbo" se "gpt-4" não estiver disponível no seu plano
            messages=mensagens,
            max_tokens=200,
            temperature=0.5
        )

        # Extrair a resposta do GPT
        ferramentas_texto = response.choices[0].message['content'].strip()

        print("DEBUG: Resposta do GPT:\n", ferramentas_texto)

        # Extrair ferramentas da resposta do GPT (exemplo: "Serra Circular - Código SAP: MAT001")
        ferramentas_escolhidas = []
        for linha in ferramentas_texto.split("\n"):
            if "Código SAP:" in linha:
                # Extrair o nome da ferramenta e o código SAP
                partes = linha.split(" - Código SAP:")
                nome_ferramenta = partes[0].split(".")[-1].strip()  # Extrair o nome sem o número da lista
                codigo_sap = partes[1].strip()
                ferramentas_escolhidas.append((nome_ferramenta, codigo_sap))

        # Mapeia as ferramentas escolhidas para seus detalhes no DataFrame
        ferramentas_selecionadas = []
        for nome_ferramenta, codigo_sap in ferramentas_escolhidas:
            ferramenta_info = ferramentas_df[ferramentas_df['Código SAP'] == codigo_sap]
            if not ferramenta_info.empty:
                ferramentas_selecionadas.append({
                    'Categoria': ferramenta_info['Categoria'].values[0],
                    'Descrição': ferramenta_info['Descrição do Material/Equipamento'].values[0],
                    'Código SAP': ferramenta_info['Código SAP'].values[0]
                })
        
        print("DEBUG: Ferramentas mapeadas após a resposta do GPT:\n", ferramentas_selecionadas)
        return ferramentas_selecionadas

    except Exception as e:
        print(f"Erro ao selecionar ferramentas usando GPT: {e}")
        return []
