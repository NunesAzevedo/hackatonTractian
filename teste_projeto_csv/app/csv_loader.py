import pandas as pd

# Carrega o CSV das ferramentas
def carregar_ferramentas():
    caminho_csv = 'data/ColinhadeCodigos SAP.csv'
    ferramentas_df = pd.read_csv(caminho_csv)
    return ferramentas_df

# Carrega o CSV das reservas
def carregar_reservas():
    caminho_csv = 'data/almoxarifado.csv'
    reservas_df = pd.read_csv(caminho_csv)
    return reservas_df

# Função para obter as reservas de uma ferramenta específica
def obter_reservas_por_codigo_sap(codigo_sap: str):
    reservas_df = carregar_reservas()
    # Filtra as reservas por código SAP
    reservas_filtradas = reservas_df[reservas_df['Código SAP'] == codigo_sap]
    if reservas_filtradas.empty:
        return None
    # Convertendo o DataFrame para dicionário para retornar na API
    reservas = reservas_filtradas.to_dict(orient='records')
    return reservas
