from fastapi import APIRouter, HTTPException
from .csv_loader import carregar_ferramentas, obter_reservas_por_codigo_sap

router = APIRouter()

@router.get("/ferramentas/")
def listar_ferramentas():
    # Carrega todas as ferramentas a partir do CSV
    ferramentas_df = carregar_ferramentas()
    ferramentas = ferramentas_df.to_dict(orient='records')
    return ferramentas

@router.get("/reservas/{codigo_sap}")
def listar_reservas(codigo_sap: str):
    reservas = obter_reservas_por_codigo_sap(codigo_sap)
    if reservas is None:
        raise HTTPException(status_code=404, detail="Ferramenta não encontrada")
    return reservas
