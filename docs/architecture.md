# 🏗️ Arquitetura — IDP Platform Engineering

## Visão Geral

A plataforma segue o modelo **Platform as a Product**, onde a infraestrutura complexa é abstraída em um portal self-service.

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

## Componentes

### Software Catalog
- Auto-descoberta de repositórios via GitHub Entity Provider
- Leitura automática de `catalog-info.yaml` de todos os repos da organização
- Atualização a cada 30 minutos

### TechDocs (Docs-as-Code)
- Documentação descentralizada em Markdown
- Motor de geração: MkDocs com `techdocs-core`
- Publicação local integrada ao portal

### Software Templates (Golden Paths)
- Templates para criação automatizada de microsserviços
- Python/FastAPI com CI/CD, Dockerfile seguro e observabilidade
- Publicação automática no GitHub e registro no catálogo

### Integração Kubernetes
- Visualização de Pods, Deployments e status
- Acesso via Service Account Token
- Sem necessidade de `kubectl` para desenvolvedores
