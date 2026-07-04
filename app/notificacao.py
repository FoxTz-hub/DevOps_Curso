from fastapi import FastAPI
from datetime import  datetime

NOTIFICACOES = []
APP_NOTIFICACAO = FastAPI()

# @APP_NOTIFICACAO.post("/notificacao")
# def criar_notificacao(titulo: str, data: datetime):
#     tarefa = {
#         "titulo": titulo,
#         "data": data
#     }
#     TAREFA_FINALIZADA.append(tarefa)
#     print(f"Notificação enviada para o usuário: Tarefa '{titulo}' concluída em {data}")
#     return {"message": "Notificação enviada com sucesso!"}

@APP_NOTIFICACAO.post("/notificar")
def notificar(titulo: str, data_finalizacao: datetime):
    global NOTIFICACOES
    
    resultado = f"Tarefa '{titulo}' finalizada em {data_finalizacao}"
    print(resultado)

    NOTIFICACOES.append(resultado)

    return {"status": "OK"}