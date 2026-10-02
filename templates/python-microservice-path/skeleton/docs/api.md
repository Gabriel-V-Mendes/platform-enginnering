# API Reference — ${{ values.name }}

## `GET /health`

Health check padrão para readiness/liveness probes do Kubernetes.

**Resposta:**
```json
{
  "status": "up",
  "service": "${{ values.name }}"
}
```

## `GET /metrics`

Endpoint de métricas no formato Prometheus (text/plain).

### Métricas Expostas

| Métrica | Tipo | Descrição |
|---------|------|-----------|
| `http_requests_total` | Counter | Total de requisições HTTP recebidas |
| `http_request_duration_seconds` | Histogram | Latência das requisições HTTP |

### Labels

- `method`: Método HTTP (GET, POST, etc.)
- `endpoint`: Path da rota
- `status`: Código HTTP de resposta (apenas em `http_requests_total`)
