import openai
import os

openai.api_key = "sk-svcacct-qmsP54NDOpQ3Ayx3QI8EEPnvDUFlArGiGm6efreX3UAqdIvyKiBIb1mVFh-jz1iT3BlbkFJrQXVgoenf9Hk88KEqVrmBNCChCL2ylFGSjTKWMcNPdmIzkWOTZm7VE0mEn4w7AA"

def ler_nome_arquivo_na_pasta(nome_pasta): # Pasta contendo os arquivos dos manuais das maquinas
    arquivos = os.listdir(nome_pasta)
    return arquivos

def generate_manual(nome_pasta, machine):
    manuais = ler_nome_arquivo_na_pasta(nome_pasta)
    messages = [
        {
            "role": "user",
            "content": f"""Visando solucionar um problema de uma maquina {machine}, procure o manual da maquina na lista abaixo e retorne apenas o nome do arquivo: {manuais}"""
        }
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    return response.choices[0].message

def generate_resume(nome_pasta, nome_manual, problem):
    with open(f"{nome_pasta}/{nome_manual}", "r") as file:
        manual = file.read()
    messages = [
        {
            "role": "user",
            "content": f"""Gostaria de um resumo do manual {nome_manual} visando solucionar um problema de {problem}. O manual é o seguinte: {manual}"""
        }
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return response.choices[0].message

def generate_tool_list(nome_pasta, nome_manual):
    with open(f"{nome_pasta}/{nome_manual}", "r") as file:
        manual = file.read()
    messages = [
        {
            "role": "user",
            "content": f"""Gostaria de uma lista de ferramentas necessárias para o manual {nome_manual}. O manual é o seguinte: {manual}"""
        }
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return response.choices[0].message

