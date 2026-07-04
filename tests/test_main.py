from fastapi.testclient import TestClient

from app import APP

CLIENT = TestClient(APP)

def criar_tarefa_mock():
    requisicao = CLIENT.post("/tarefas/criar", params={"titulo": "Tarefa 1", "descricao": "Descrição da Tarefa 1"})

def test_index():
    requisicao = CLIENT.get("/")

    assert requisicao.status_code == 200
    assert requisicao.json() == "Olá, DevOps!"

def test_criar_tarefa():
    requisicao = CLIENT.post("/tarefas/criar", params={"titulo": "Tarefa 1", "descricao": "Descrição da Tarefa 1"})

    assert requisicao.status_code == 201
    assert requisicao.json()["mensagem"] == "Tarefa criada com sucesso!"

def test_remover_tarefa():
    criar_tarefa_mock()

    requisicao = CLIENT.delete("/tarefas/deletar/0")

    assert requisicao.status_code == 200
    assert requisicao.json() == {"mensagem": "Tarefa excluída com sucesso"}

    requisicao = CLIENT.delete("/tarefas/deletar/10")
    assert requisicao.status_code == 200
    assert requisicao.json() == {"mensagem": "Não existe nenhuma tarefa com esse id"}

def test_listar_tarefas():
    criar_tarefa_mock()

    requisicao = CLIENT.get("/tarefas")

    assert requisicao.status_code == 200
    assert len(requisicao.json()) > 0

def test_listar_tarefas_especifica():
    criar_tarefa_mock()

    requisicao = CLIENT.get("/tarefas/1")

    assert requisicao.status_code == 200
    assert requisicao.json()["id"] == 1

    requisicao = CLIENT.get("/tarefas/10")
    assert requisicao.status_code == 200
    assert requisicao.json() == {"mensagem": "Não existe nenhuma tarefas com esse id"}

def test_atualizar_tarefa():
    criar_tarefa_mock()

    requisicao = CLIENT.put("/tarefas/atualizar/1", params={"titulo": "Tarefa 2", "descricao": "Descrição da Tarefa 2"})
    assert requisicao.status_code == 200
    assert requisicao.json() == {"mensagem": "OK"}

    requisicao = CLIENT.get("/tarefas/1")
    assert requisicao.status_code == 200
    assert requisicao.json()["titulo"] == "Tarefa 1"
    assert requisicao.json()["descricao"] == "Descrição da Tarefa 1"