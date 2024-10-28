from fastapi import FastAPI
from pydantic import BaseModel

import IA
app = FastAPI()

#Constantes e caminhos
nome_pasta = '../Nuvem/'

class Order(BaseModel):
    maquina: str
    problema: str

class Product(BaseModel):
    maquina: str # Frontend - input
    problema: str # Frontend - input
    manual: str # Frontend - link
    manual_resumido: str # Frontend - texto
    lista_ferramentas: str # Banco de dados

order = Order(maquina="maquina", problema="problema")
product = Product(maquina="maquina", problema="problema", manual="manual", manual_resumido="manual_resumido", lista_ferramentas="lista_ferramentas")



@app.get("/ok")
async def ok():
    return {"message": "ok"}


@app.get("/order/{maquina}/{problema}")
async def place_order(maquina: str, problema: str):
    order.maquina = maquina
    order.problema = problema
    product.maquina = maquina
    product.problema = problema
    return {"message": f"OS para maquina {maquina} com o problema {problema} gerado com sucesso!"}

@app.get("/product")
async def place_product():

    return {"message": f"Maquina: {product.maquina}\nProblema: {product.problema}Link do manual completo: {product.manual}\nLista de ferramentas: {product.lista_ferramentas}\nManual resumido: {product.manual_resumido}"}

@app.get("/generate_manual")
async def generate_manual():
    product.manual = IA.generate_manual(nome_pasta, order.maquina)["content"]
    return {"message": product.manual}

@app.get("/generate_resume")
async def generate_resume():
    product.manual_resumido = IA.generate_resume(nome_pasta, product.manual, order.problema)["content"]
    
    return {"message": product.manual_resumido}

@app.get("/generate_tool_list")
async def generate_tool_list():
    product.lista_ferramentas = IA.generate_tool_list(nome_pasta, product.manual, order.problema)["content"]
    return {"message": product.lista_ferramentas}
