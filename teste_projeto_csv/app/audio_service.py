import openai

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
            return file.read().strip()  # Remove possíveis quebras de linha e espaços extras
    except Exception as e:
        print(f"Erro ao carregar a API Key: {e}")
        return ""

# Caminho para o arquivo de chave API (ajuste o caminho conforme a sua estrutura de diretório)
caminho_api_key = 'openai_key.txt'  # Assumindo que o arquivo está na raiz do projeto

# Carregar a chave da API
openai.api_key = carregar_api_key(caminho_api_key)

# Função para transcrever e interpretar o áudio
def transcrever_audio(file_path: str) -> str:
    """
    Transcreve o arquivo de áudio usando o modelo Whisper da OpenAI.
    
    Parâmetros:
    file_path (str): Caminho do arquivo de áudio.
    
    Retorna:
    str: Texto transcrito a partir do áudio.
    """
    try:
        with open(file_path, "rb") as audio_file:
            transcript = openai.Audio.transcribe("whisper-1", audio_file)
        return transcript['text']
    except Exception as e:
        print(f"Erro ao transcrever o áudio: {e}")
        return ""

# Função para perguntar ao GPT quais ferramentas são necessárias com base na transcrição
def extrair_ferramentas_da_transcricao(transcricao: str) -> list:
    """
    Usa a API do GPT para identificar as ferramentas necessárias a partir da transcrição de áudio.
    
    Parâmetros:
    transcricao (str): Texto transcrito do áudio.
    
    Retorna:
    list: Lista de ferramentas identificadas.
    """
    prompt = f"A partir dessa descrição da tarefa, liste as ferramentas necessárias:\n\n{transcricao}"
    
    try:
        response = openai.Completion.create(
            model="gpt-4",
            prompt=prompt,
            max_tokens=100,
            temperature=0.5
        )
        
        # A resposta deve ser algo como "Chave de Fenda, Martelo, Alicate"
        ferramentas_texto = response.choices[0].text.strip()
        
        # Converte a string de ferramentas para uma lista
        ferramentas = [ferramenta.strip() for ferramenta in ferramentas_texto.split(",")]
        
        return ferramentas
    except Exception as e:
        print(f"Erro ao extrair ferramentas da transcrição: {e}")
        return []
