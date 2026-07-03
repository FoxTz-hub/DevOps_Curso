from fastapi import FastAPI
from datetime import  datetime

TAREFA_FINALIZADA = [] 
APP_NOTIFICACAO = FastAPI()

@APP_NOTIFICACAO.post("/notificacao")
def criar_notificacao(titulo: str, data: datetime):
    tarefa = {
        "titulo": titulo,
        "data": data
    }
    TAREFA_FINALIZADA.append(tarefa)
    print(f"Notificação enviada para o usuário: Tarefa '{titulo}' concluída em {data}")
    return {"message": "Notificação enviada com sucesso!"}