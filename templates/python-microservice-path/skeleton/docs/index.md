# ${{ values.name }}

${{ values.description }}

## Endpoints

| Rota | Método | Descrição |
|------|--------|-----------|
| `/health` | GET | Health check para Kubernetes probes |
| `/metrics` | GET | Métricas no formato Prometheus |

## Stack

- **Python** 3.11
- **FastAPI** ≥0.115
- **Uvicorn** como ASGI server
- **prometheus-client** para observabilidade

## Executando Localmente

```bash
pip install -r requirements.txt
uvicorn src.main:app --reload --port 8000
```

## Testes

```bash
pytest tests/ -v
```
