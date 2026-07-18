from fastapi import FastAPI
from datetime import datetime
import requests
import logging

LISTA_TAREFAS = []

APP = FastAPI()

LOGGER = logging.getLogger("DevOps")
LOGGER.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler("api.log", encoding='utf-8')
fmt = logging.Formatter(fmt="%(name)s | %(asctime)s | %(filename)s:%(lineno)s | %(levelname)s | %(menssage)s")

stream_handler.setFormatter(fmt)
file_handler.setFormatter(fmt)

LOGGER.addHandler(stream_handler)
LOGGER.addHandler(file_handler)

def nova_tarefa(id: int, titulo: str, descricao: str):
    return {
        "id": id,
        "titulo": titulo,
        "descricao": descricao,
        "concluido": False,
        "criado_em": datetime.now()
    }

    LOGGER.debug(f"Criando tarefa='{tarefa}'")


def verificar_existencia_tarefa(id: int):
    """
    Função auxiliar para verificar a existência de uma tarefa com base no seu ID
    """
    for tarefa in LISTA_TAREFAS:
        if id == tarefa["id"]:
            return True

    return False


@APP.get("/")
def index():
    LOGGER.info(f"Rota '/' foi acessada")
    return "Olá, DevOps!"


@APP.get("/tarefas")
def listar_tarefas():
    # Listar tarefas (somente id e título)
    LOGGER.info(f"Rota '/tarefas' foi acessada")
    if len(LISTA_TAREFAS) == 0:
        return LISTA_TAREFAS

    tarefas = []

    for tarefa in LISTA_TAREFAS:
        info = {
            "id": tarefa["id"],
            "titulo": tarefa["titulo"]
        }
        tarefas.append(info)

    return tarefas


@APP.get("/tarefas/{id}")
def listar_tarefas_especifica(id: int):
    if len(LISTA_TAREFAS) == 0:
        LOGGER.error(f"Rota '/tarefas/{id} acessada. Mensagem: {mensagem_padrao['mensagem']}")
        return {
            "mensagem": "Não existe nenhuma tarefa com esse id"
        }

    if id >= 0 and id < len(LISTA_TAREFAS):
        LOGGER.info(f"Rota '/tarefas/{id} acessada.")
        return LISTA_TAREFAS[id]

    return {
        "mensagem": "Não existe nenhuma tarefas com esse id"
    }


@APP.post("/tarefas/criar", status_code=201)
def criar_tarefa(titulo: str, descricao: str):
    id = len(LISTA_TAREFAS)

    tarefa = nova_tarefa(
        id,
        titulo,
        descricao
    )

    LISTA_TAREFAS.append(tarefa)
    LOGGER.info(f"Rota POST '/tarefas/criar' acessada. Tarefa id={id} criada.")

    return {
        "mensagem": "Tarefa criada com sucesso!"
    }


@APP.put("/tarefas/atualizar/{id}")
def atualizar_tarefa(
    id: int,
    titulo: str = "",
    descricao: str = "",
    concluido: bool = False
):
    global LISTA_TAREFAS

    tarefa_existe = verificar_existencia_tarefa(id)

    if not tarefa_existe:
        LOGGER.error(f"Rota PUT '/tarefas/atualizar/{id}' acessada. Tarefa NÃO existe.")
        return {
            "mensagem": "TAREFA NÃO EXISTE!"
        }

    tarefa = None

    for indice in range(len(LISTA_TAREFAS)):
        tarefa = LISTA_TAREFAS[indice]

        if tarefa["id"] == id:
            break

    if titulo != "":
        LISTA_TAREFAS[indice]["titulo"] = titulo

    if descricao != "":
        LISTA_TAREFAS[indice]["descricao"] = descricao

    if concluido:
        requests.post(
            f"http://notificacoes:8000/notificar?"
            f"titulo={tarefa['titulo']}&"
            f"data_finalizacao={datetime.now()}",
            timeout=10
        )

    LISTA_TAREFAS[indice]["concluido"] = concluido
    LOGGER.debug(f"Tarefa atualizada = {LISTA_TAREFAS[indice]}")
    LOGGER.info(f"Rota PUT '/tarefas/atualizar/{id}' acessada. Tarefa id={id} atualizada.")

    return {
        "mensagem": "OK"
    }


@APP.delete("/tarefas/deletar/{id}")
def excluir_tarefa(id: int):
    if id >= 0 and id < len(LISTA_TAREFAS):
        LISTA_TAREFAS.pop(id)
        LOGGER.info(f"Rota DELETE '/tarefas/{id}' acessada. Tarefa id={id} removida.")

        return {
            "mensagem": "Tarefa excluída com sucesso"
        }

    return {
        "mensagem": "Não existe nenhuma tarefas com esse id"
    }


@APP.get("/health")
def health():
    return {
        "status": "ok, retorno esperado"
    }