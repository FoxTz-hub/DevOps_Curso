from fastapi import FastAPI
from datetime import  datetime

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

@APP.post("/tarefas/criar")
def criar_tarefa(titulo: str, descricao: str):
    id = len(LISTA_TAREFAS)
    tarefa = nova_tarefa(id, titulo, descricao)
    LISTA_TAREFAS.append(tarefa)
    return tarefa

@APP.put("/tarefas/atualizar/{id}")
def atualizar_tarefa(id: int, titulo: str = "", descricao: str = "", concluido: bool = False):
    if id >= 0 and id < len(LISTA_TAREFAS):
        tarefa = LISTA_TAREFAS[id]
        if titulo:
            tarefa['titulo'] = titulo
        if descricao:
            tarefa['descricao'] = descricao
        if concluido == True:
            requests.post(f"http://localhost:8001/notificacao?titulo={tarefa['titulo']}&data={datetime.now()}")
        return tarefa

    return {"mensagem": "Não existe nenhuma tarefa com esse id"}

@APP.delete("/tarefas/deletar/{id}")
def excluir_tarefa(id: int):
    if id >= 0 and id < len(LISTA_TAREFAS):
        LISTA_TAREFAS.pop(id)
        return {"mensagem": "Tarefa excluída com sucesso"}

    return {"mensagem": "Não existe nenhuma tarefa com esse id"}   