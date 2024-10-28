from fastapi import FastAPI
from .file_handler import processar_arquivo_txt, gerar_csv_ferramentas

app = FastAPI(
    title="Gerenciamento de Ferramentas - Fábrica",
    description="API para processar textos de problemas, selecionar ferramentas e verificar disponibilidade",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Gerenciamento de Ferramentas!"}

# Rota para gerar o CSV com as ferramentas escolhidas diretamente a partir do arquivo .txt
@app.get("/gerar_csv/")
def gerar_csv():
    # Processa o arquivo .txt e obtém as ferramentas escolhidas
    ferramentas_escolhidas = processar_arquivo_txt()

    # Se houver ferramentas escolhidas, gera o CSV
    if ferramentas_escolhidas:
        gerar_csv_ferramentas(ferramentas_escolhidas)
        return {"message": "Arquivo CSV gerado com sucesso!", "ferramentas": ferramentas_escolhidas}
    else:
        return {"message": "Erro ao processar o arquivo de problema. Nenhuma ferramenta foi encontrada."}
