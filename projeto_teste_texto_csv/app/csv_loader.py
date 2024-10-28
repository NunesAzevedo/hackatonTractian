import pandas as pd

# Carrega o CSV das ferramentas
def carregar_ferramentas():
    """
    Carrega o arquivo CSV que contém as ferramentas e seus códigos SAP.
    
    Retorna:
        pd.DataFrame: DataFrame contendo as ferramentas e códigos SAP.
    """
    caminho_csv = 'data/ColinhadeCodigosSAP.csv'
    try:
        ferramentas_df = pd.read_csv(caminho_csv)
        return ferramentas_df
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo {caminho_csv} não encontrado.")
    
# Carrega o CSV das reservas
def carregar_reservas():
    """
    Carrega o arquivo CSV que contém as reservas das ferramentas por horário.
    
    Retorna:
        pd.DataFrame: DataFrame contendo as reservas.
    """
    caminho_csv = 'data/almoxarifado.csv'
    try:
        reservas_df = pd.read_csv(caminho_csv)
        return reservas_df
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo {caminho_csv} não encontrado.")

# Verifica o próximo horário em que todas as ferramentas estarão disponíveis
def verificar_disponibilidade(ferramentas_escolhidas: list) -> str:
    """
    Verifica o primeiro horário em que todas as ferramentas estarão disponíveis no almoxarifado.

    Parâmetros:
        ferramentas_escolhidas (list): Lista de códigos SAP das ferramentas escolhidas.
    
    Retorna:
        str: Primeiro horário em que todas as ferramentas estarão disponíveis ou mensagem de indisponibilidade.
    """
    reservas_df = carregar_reservas()

    # Horários disponíveis no CSV (todas as colunas menos a primeira, que contém os códigos SAP)
    horarios = reservas_df.columns[1:]

    # Verifica a disponibilidade de todas as ferramentas para cada horário
    for hora in horarios:
        disponivel = True
        for ferramenta in ferramentas_escolhidas:
            status = reservas_df[reservas_df['Código SAP'] == ferramenta][hora].values
            if len(status) == 0 or status[0].lower() == 'reservado':
                disponivel = False
                break
        if disponivel:
            return hora

    return "Nenhum horário disponível para todas as ferramentas."
