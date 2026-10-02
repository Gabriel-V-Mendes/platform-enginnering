# 🛤️ Golden Paths — Templates de Microsserviços

## O que são Golden Paths?

Golden Paths são caminhos padronizados e automatizados para criar novos serviços. Eles garantem que todo microsserviço nasce com:

- ✅ **Dockerfile multi-stage** com usuário non-root
- ✅ **CI/CD** com GitHub Actions e Trivy scan
- ✅ **Observabilidade** com métricas Prometheus nativas
- ✅ **Registro automático** no Software Catalog

## Template Disponível: Python FastAPI

### Stack
| Tecnologia | Versão | Propósito |
|------------|--------|-----------|
| Python | 3.11 | Runtime |
| FastAPI | ≥0.115 | Framework Web |
| Uvicorn | ≥0.32 | ASGI Server |
| prometheus-client | ≥0.21 | Métricas |
| Pytest | ≥8.0 | Testes |

### Endpoints gerados automaticamente

| Rota | Descrição |
|------|-----------|
| `GET /health` | Health check para K8s probes |
| `GET /metrics` | Métricas no formato Prometheus |

### Como usar

1. Acesse o portal Backstage em `http://localhost:7007`
2. Clique em **"Create"** no menu lateral
3. Selecione **"Python FastAPI Microservice"**
4. Preencha o formulário com nome, descrição e repositório
5. O template criará automaticamente:
   - Repositório no GitHub com código fonte
   - Pipeline de CI/CD com Trivy scan
   - Registro do componente no Software Catalog

### Segurança

Todos os microsserviços gerados seguem o princípio de **Zero Root Privileges**:

```dockerfile
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
USER appuser
```

Isso previne Container Breakout e segue as melhores práticas de segurança.
