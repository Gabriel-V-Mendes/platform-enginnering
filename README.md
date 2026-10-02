
[![CI — IDP Platform Engineering](https://github.com/Gabriel-V-Mendes/infraestrutura-aws-terraform-localstack/actions/workflows/ci.yml/badge.svg)](https://github.com/Gabriel-V-Mendes/infraestrutura-aws-terraform-localstack/actions/workflows/ci.yml)

# 🏗️ IDP — Internal Developer Platform | (Está em Desenvolvimento)

*"Construir pipelines e subir clusters Kubernetes é essencial, mas como resolvemos o atrito e a lentidão dos desenvolvedores no dia a dia?"*

Essa foi a provocação que me levou a iniciar este laboratório. Como profissional apaixonado por infraestrutura e automação, decidi focar no meu **autodesenvolvimento** e explorar o universo do **Platform Engineering**, construindo do absoluto zero uma **Internal Developer Platform (IDP)** baseada no framework **Backstage**.

## 📖 A Narrativa do Estudo

Mais do que apenas agrupar e configurar ferramentas, este projeto trata a infraestrutura interna sob a ótica de **Platform as a Product**. Meu objetivo principal nesta jornada foi entender na prática como empacotar arquiteturas complexas (Kubernetes, CI/CD, Observabilidade) e entregá-las como uma experiência de portal *self-service*.

Em vez de exigir que a equipe de desenvolvimento perca tempo criando arquivos repetitivos de infraestrutura e segurança, decidi abstrair a complexidade criando os chamados **Golden Paths** (caminhos pavimentados).

## 🏛️ Arquitetura

```
┌─────────────────────────────────────────────────┐
│              Backstage Portal (UI)              │
│          http://localhost:7007                   │
├───────┬───────────┬──────────┬──────────────────┤
│Catalog│ TechDocs  │Scaffolder│   Kubernetes     │
│       │           │(Golden   │   Dashboard      │
│       │           │ Paths)   │                  │
├───────┴───────────┴──────────┴──────────────────┤
│              Backend (Node.js)                   │
│              Plugins System                      │
├──────────────────────────────────────────────────┤
│   PostgreSQL   │   GitHub API   │   K8s API      │
└────────────────┴────────────────┴────────────────┘
```

## 📁 Estrutura do Projeto

```
platform-engineering/
├── packages/
│   ├── app/                        # Frontend (React) do Backstage
│   │   └── src/modules/
│   │       ├── home/               # Widget personalizado da Home Page
│   │       └── nav/                # Sidebar e logos customizados
│   └── backend/                    # Backend (Node.js) com plugins
│       └── src/index.ts            # Registro de todos os plugins
├── templates/
│   └── python-microservice-path/   # 🛤️ Golden Path — Python/FastAPI
│       ├── template.yaml           # Definição do formulário Scaffolder
│       └── skeleton/               # Código-base gerado
│           ├── src/main.py         # API FastAPI com Prometheus
│           ├── Dockerfile          # Multi-stage, non-root
│           ├── github-folder/      # CI/CD (renomeado para .github)
│           ├── tests/              # Testes com pytest
│           └── docs/               # TechDocs do microsserviço
├── infrastructure/
│   └── docker/
│       ├── Dockerfile              # Build multi-stage do Backstage
│       ├── docker-compose.yml      # Backstage + PostgreSQL
│       ├── .env.example            # Template de variáveis de ambiente
│       └── .env                    # Variáveis locais (não versionado)
├── docs/                           # 📚 TechDocs do IDP
│   ├── index.md
│   ├── architecture.md
│   └── golden-paths.md
├── .github/workflows/ci.yml       # Pipeline CI do projeto IDP
├── app-config.yaml                 # Config de desenvolvimento
├── app-config.production.yaml      # Config de produção (Docker)
└── catalog-info.yaml               # Registro do IDP no catálogo
```

## 🧠 Aprendizados e Habilidades Desenvolvidas

- **Redução de Carga Cognitiva:** Através dos *Software Templates*, automatizei a geração de microsserviços em **Python (FastAPI)**. Isso me mostrou o imenso valor de padronizar projetos que já nascem com uma arquitetura moderna pronta em poucos segundos.
- **Segurança desde o Dia Zero (Shift-Left):** Entendi a importância de integrar a segurança no início do ciclo. Os templates que desenvolvi garantem que os containers operem com privilégios limitados (**Non-Root Containers**) e que o CI/CD no GitHub Actions já nasça com análises automatizadas de vulnerabilidades (via Trivy).
- **Docs-as-Code (TechDocs):** Implementei a cultura de manter a documentação técnica junto ao código-fonte. Aprendi a conectar repositórios ao portal, compilando o Markdown via MkDocs de forma centralizada.
- **Observabilidade Integrada:** O IDP entrega serviços que já nascem expondo endpoints `/metrics` nativos para o formato **Prometheus**, preparando o terreno para monitoramento avançado no ecossistema Kubernetes.

## 🚀 Como Rodar

### Pré-requisitos

| Ferramenta | Versão Mínima |
|---|---|
| Node.js | 22 |
| Yarn | 4 (via Corepack) |
| Docker & Docker Compose | Recente |
| Git | 2.x |

### Modo Desenvolvimento (local)

```bash
# 1. Clone o repositório
git clone https://github.com/Gabriel-V-Mendes/infraestrutura-aws-terraform-localstack.git
cd platform-engineering

# 2. Ative o Corepack (gerenciador do Yarn 4)
corepack enable

# 3. Instale as dependências
yarn install

# 4. Inicie o Backstage em modo de desenvolvimento
yarn dev
```

O portal estará disponível em `http://localhost:3000` (frontend) e `http://localhost:7007` (backend).

### Modo Produção (Docker)

```bash
# 1. Configure as variáveis de ambiente
cd infrastructure/docker
cp .env.example .env
# Edite o .env com seu GITHUB_TOKEN real

# 2. Suba os containers
docker compose up -d

# 3. Acompanhe os logs (primeiro boot leva ~60s)
docker compose logs -f backstage
```

O portal estará disponível em `http://localhost:7007`.

### Usando os Golden Paths

1. Acesse o portal em `http://localhost:7007`
2. Clique em **"Create"** no menu lateral
3. Selecione **"Python FastAPI Microservice"**
4. Preencha nome, descrição, organização e nome do repositório GitHub
5. O template cria automaticamente:
   - ✅ Repositório no GitHub com código-fonte completo
   - ✅ Pipeline CI/CD com Trivy scan
   - ✅ Registro do serviço no Software Catalog

## 🛤️ Golden Paths Disponíveis

### Python FastAPI Microservice

| Tecnologia | Versão | Propósito |
|---|---|---|
| Python | 3.11 | Runtime |
| FastAPI | ≥0.115 | Framework Web |
| Uvicorn | ≥0.32 | ASGI Server |
| prometheus-client | ≥0.21 | Métricas |
| Pytest | ≥8.0 | Testes |

**O que é gerado automaticamente:**
- API FastAPI com middleware de métricas Prometheus
- Dockerfile multi-stage com usuário **non-root**
- Pipeline CI/CD (testes + build + Trivy scan)
- Documentação TechDocs integrada ao portal
- `catalog-info.yaml` com annotations de K8s e Grafana

## 🔒 Segurança

Todos os microsserviços gerados seguem o princípio de **Zero Root Privileges**:

```dockerfile
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
USER appuser
```

O CI/CD inclui **Trivy Scanner** que bloqueia builds com vulnerabilidades `CRITICAL` ou `HIGH`.

---
*Este repositório é um registro vivo da minha evolução profissional, focado na transição e amadurecimento das práticas de DevOps tradicional para a criação de Plataformas Internas de Desenvolvimento escaláveis.*
