# DevOps Curso - API de Gerenciamento de Tarefas

Projeto desenvolvido para a disciplina de **DevOps (PUCPR-LAR)** com o objetivo de demonstrar a aplicação de práticas de Integração Contínua (CI), Entrega Contínua (CD), conteinerização com Docker e implantação em Kubernetes.

## 📋 Sobre o Projeto

A aplicação consiste em uma API REST desenvolvida em **FastAPI** para gerenciamento de tarefas.

Além da API principal, o projeto possui:

- Serviço de notificações;
- Gateway utilizando Nginx;
- Conteinerização com Docker;
- Orquestração com Docker Compose;
- Pipeline CI/CD utilizando GitHub Actions;
- Implantação em Kubernetes.

---

## 🚀 Tecnologias Utilizadas

- Python 3.12
- FastAPI
- Uvicorn
- Docker
- Docker Compose
- Kubernetes
- Nginx
- GitHub Actions
- Pytest
- Bandit
- Pylint

---

## 📁 Estrutura do Projeto

```
.
├── .github/
│   └── workflows/
│       └── ci_cd.yaml
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── notificacao.py
├── tests/
├── Dockerfile
├── Dockerfile.nginx
├── docker-compose.yaml
├── deployment.yaml
├── service-devops.yaml
├── nginx.conf
├── requirements.txt
└── README.md
```

---

## ⚙️ Funcionalidades

A API permite:

- Criar tarefas
- Listar todas as tarefas
- Consultar uma tarefa específica
- Atualizar tarefas
- Excluir tarefas
- Consultar status da aplicação (Health Check)
- Consultar métricas da aplicação

---

## 📌 Endpoints

| Método | Endpoint | Descrição |
|---------|----------|-----------|
| GET | `/` | Mensagem inicial |
| GET | `/tarefas` | Lista todas as tarefas |
| GET | `/tarefas/{id}` | Busca tarefa pelo ID |
| POST | `/tarefas/criar` | Cria uma nova tarefa |
| PUT | `/tarefas/atualizar/{id}` | Atualiza uma tarefa |
| DELETE | `/tarefas/deletar/{id}` | Remove uma tarefa |
| GET | `/health` | Health Check |
| GET | `/metricas` | Métricas da aplicação |

---

## 🐳 Executando com Docker

Construir as imagens:

```bash
docker compose build
```

Subir os containers:

```bash
docker compose up
```

Ou em segundo plano:

```bash
docker compose up -d
```

---

## ☸️ Implantação no Kubernetes

Aplicar o deployment:

```bash
kubectl apply -f deployment.yaml
```

Aplicar o service:

```bash
kubectl apply -f service-devops.yaml
```

Verificar os pods:

```bash
kubectl get pods
```

Verificar os serviços:

```bash
kubectl get services
```

---

## 🔄 Pipeline CI/CD

O projeto possui uma pipeline automatizada utilizando **GitHub Actions**.

A pipeline é executada em Pull Requests para a branch `main` e também pode ser acionada manualmente.

### Etapas da Pipeline

### Integração Contínua (CI)

- Instalação das dependências
- Execução dos testes unitários
- Cobertura de código (mínimo de 65%)
- Análise estática de segurança com Bandit
- Análise de qualidade utilizando Pylint

### Análise de Dependências

- Verificação utilizando FOSSA

### Entrega Contínua (CD)

- Build da imagem Docker
- Publicação da imagem no Docker Hub

### Implantação

- Aplicação automática do Deployment Kubernetes

---

## 🧪 Executando os testes

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute os testes:

```bash
pytest
```

Executar cobertura:

```bash
pytest --cov
```

---

## 📊 Health Check

Endpoint:

```
GET /health
```

Resposta esperada:

```json
{
    "status": "ok, retorno esperado"
}
```

---

## 📦 Docker

A aplicação utiliza:

- Container da API
- Container de notificações
- Container Nginx como Gateway

---

## 🔒 Qualidade de Código

O projeto utiliza ferramentas para garantir qualidade e segurança:

- Pytest
- Coverage
- Bandit
- Pylint

---

## 👨‍💻 Autor

Projeto desenvolvido para a disciplina de **DevOps - PUCPR**.
