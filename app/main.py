from fastapi import FastAPI
from datetime import  datetime

import requests

LISTA_TAREFAS = []
APP = FastAPI()

def nova_tarefa(id: int, titulo: str, descricao: str):
    return{
        "id": id,
        "titulo": titulo,
        "descricao": descricao,
        "concluido": False,
        "criado_em": datetime.now()
    }

def verificar_existencia_tarefa(id: int):
    """Função auxiliar para verificar a existência de uma tarefa com base no seu ID"""
    for tarefa in LISTA_TAREFAS:
        if id == tarefa['id']:
            return True
    return False

@APP.get("/")
def index():
    return "Olá, DevOps!"

@APP.get("/tarefas")
def listar_tarefas():
    #Listar Tarefas (somente com id e titulo)
    if len(LISTA_TAREFAS) == 0:
        return LISTA_TAREFAS

    tarefas = []
    for tarefa in LISTA_TAREFAS:
        info = {"id": tarefa['id'], "titulo": tarefa['titulo']}
        tarefas.append(info) 
    return tarefa

@APP.get("/tarefas/{id}")
def listar_tarefas_especifica(id: int):
    if len(LISTA_TAREFAS) == 0:
        return {"mensagem": "Não existe nenhuma tarefas com esse id"}
    
    if id >= 0 and id < len(LISTA_TAREFAS):
        return LISTA_TAREFAS[id]

    return {"mensagem": "Não existe nenhuma tarefas com esse id"}

@APP.post("/tarefas/criar", status_code=201)
def criar_tarefa(titulo: str, descricao: str):
    id = len(LISTA_TAREFAS)
    tarefa = nova_tarefa(id, titulo, descricao)
    LISTA_TAREFAS.append(tarefa)
    return {"mensagem": "Tarefa criada com sucesso!"}

@APP.put("/tarefas/atualizar/{id}")
def atualizar_tarefa(id: int, titulo: str = "", descricao: str = "", concluido: bool = False):
    global LISTA_TAREFAS

    tarefa_existe = verificar_existencia_tarefa(id)

    if not tarefa_existe:
        return {"mensagem": "TAREFA NÃO EXISTE!"}
    
    tarefa = None
    for indice in range(len(LISTA_TAREFAS)):
        tarefa = LISTA_TAREFAS[indice]

        # Sai do loop
        if tarefa['id'] == id:
            break
    
    if titulo != "":
        LISTA_TAREFAS[indice]['titulo'] = titulo
    
    if descricao !=  "": 
        LISTA_TAREFAS[indice]['descricao'] = descricao
    
    if concluido == True:
        requests.post(f"http://notificacoes:8000/notificar?titulo={tarefa['titulo']}&data_finalizacao={datetime.now()}",timeout=10)
        timeout=10

    LISTA_TAREFAS[indice]['concluido'] = concluido

    return {"mensagem": "OK"}

@APP.delete("/tarefas/deletar/{id}")
def excluir_tarefa(id: int):
    if id >= 0 and id < len(LISTA_TAREFAS):
        LISTA_TAREFAS.pop(id)
        return {"mensagem": "Tarefa excluída com sucesso"}

    return {"mensagem": "Não existe nenhuma tarefa com esse id"}

@APP.get("/health")
def health():
    return {"status": "ok"}   