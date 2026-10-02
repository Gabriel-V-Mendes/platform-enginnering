import { createFrontendModule } from '@backstage/frontend-plugin-api';
import { HomePageWidgetBlueprint } from '@backstage/plugin-home-react/alpha';
import { MarkdownContent } from '@backstage/core-components';

const content = `
## 🚀 IDP — Internal Developer Platform

Bem-vindo ao portal da nossa **Plataforma Interna de Desenvolvimento**.
Aqui você encontra tudo para construir, monitorar e documentar seus serviços.

---

### ⚡ Ações Rápidas

| Ação | Link |
|------|------|
| 🛤️ Criar novo microsserviço | [Abrir Golden Paths](/create) |
| 📦 Explorar catálogo de serviços | [Software Catalog](/catalog) |
| 📚 Documentação técnica | [TechDocs](/docs) |

---

### 🛤️ Golden Paths Disponíveis

- **Python FastAPI Microservice** — Microsserviço completo com Dockerfile seguro (non-root), CI/CD com Trivy scan, métricas Prometheus e TechDocs integrado.

### 📐 Padrões da Plataforma

Todos os serviços gerados automaticamente nascem com:
- ✅ Container **non-root** (segurança shift-left)
- ✅ Métricas **Prometheus** (\`/metrics\`)
- ✅ Health check para **Kubernetes** (\`/health\`)
- ✅ Pipeline **CI/CD** com scan de vulnerabilidades
- ✅ Documentação **TechDocs** integrada ao portal
`;

const gettingStartedWidget = HomePageWidgetBlueprint.make({
  name: 'getting-started',
  params: {
    name: 'GettingStarted',
    title: 'Plataforma Interna de Desenvolvimento',
    description: 'Visão geral da IDP e ações rápidas',
    components: async () => ({
      Content: () => <MarkdownContent content={content} />,
    }),
  },
});

export const homeModule = createFrontendModule({
  pluginId: 'home',
  extensions: [gettingStartedWidget],
});

