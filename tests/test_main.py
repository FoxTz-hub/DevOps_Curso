from fastapi.testclient import TestClient

from app import APP

CLIENT = TestClient(APP)

def test_index():
    requisicao = CLIENT.get("/")

    assert requisicao.status_code == 200
    assert requisicao.json() == "Olá, DevOps!"

def test_criar_tarefa():
    requisicao = CLIENT.post("/tarefas/criar", params={"titulo": "Tarefa 1", "descricao": "Descrição da Tarefa 1"})

    assert requisicao.status_code == 201
    assert requisicao.json()["mensagem"] == "Tarefa criada com sucesso!"