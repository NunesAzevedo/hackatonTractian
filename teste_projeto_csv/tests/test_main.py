from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Testa se a rota de listar ferramentas está funcionando corretamente
def test_listar_ferramentas():
    response = client.get("/ferramentas/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Deve retornar uma lista
    assert len(response.json()) > 0  # Verifica se a lista não está vazia

# Testa se a rota de listar reservas por código SAP está funcionando corretamente
def test_listar_reservas():
    codigo_sap = "MAT001"  # Exemplo de código SAP
    response = client.get(f"/reservas/{codigo_sap}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Deve retornar uma lista de reservas
    assert len(response.json()) > 0  # Verifica se há reservas para o código fornecido

# Testa se uma ferramenta não existente retorna 404
def test_reservas_ferramenta_nao_encontrada():
    codigo_sap_invalido = "INVALIDO"
    response = client.get(f"/reservas/{codigo_sap_invalido}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Ferramenta não encontrada"}
