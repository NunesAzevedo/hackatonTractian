from fastapi import FastAPI
from .api import router

app = FastAPI()

# Registra as rotas da API
app.include_router(router)

# Adiciona uma rota raiz para evitar o erro 404 na raiz
@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Ferramentas e Reservas!"}
