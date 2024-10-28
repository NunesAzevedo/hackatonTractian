from fastapi import APIRouter, File, UploadFile, HTTPException
from .file_handler import processar_arquivo_txt, gerar_csv_ferramentas
from .csv_loader import verificar_disponibilidade

router = APIRouter()

@router.post("/upload_txt/")
async def upload_txt(file: UploadFile = File(...)):
    """
    Endpoint para enviar o arquivo .txt com a descrição do problema e o horário.
    """
    if not file.filename.endswith(".txt"):
        raise HTTPException(status_code=400, detail="Somente arquivos .txt são permitidos.")
    
    # Processar o arquivo .txt (ler o conteúdo e processar com GPT)
    texto_problema = await file.read()
    ferramentas_escolhidas = processar_arquivo_txt(texto_problema.decode('utf-8'))
    
    # Gerar o CSV com as ferramentas escolhidas
    gerar_csv_ferramentas(ferramentas_escolhidas)
    
    # Verificar o próximo horário disponível no almoxarifado
    proximo_horario = verificar_disponibilidade(ferramentas_escolhidas)
    
    return {
        "ferramentas_escolhidas": ferramentas_escolhidas,
        "proximo_horario_disponivel": proximo_horario
    }
