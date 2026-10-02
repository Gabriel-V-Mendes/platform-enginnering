from fastapi import FastAPI, Request, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time

app = FastAPI(title="${{ values.name }}")

# -----------------
# Métricas Prometheus
# -----------------
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total de requisições HTTP recebidas",
    ["method", "endpoint", "status"],
)
REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "Latência das requisições HTTP em segundos",
    ["method", "endpoint"],
)


@app.middleware("http")
async def prometheus_middleware(request: Request, call_next):
    """Middleware que coleta métricas de cada requisição automaticamente."""
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time

    endpoint = request.url.path
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=endpoint,
        status=response.status_code,
    ).inc()
    REQUEST_LATENCY.labels(
        method=request.method,
        endpoint=endpoint,
    ).observe(duration)

    return response


# ------
# Rotas
# ------
@app.get("/health")
def health_check():
    """Health check padrão para readiness/liveness probes do Kubernetes."""
    return {"status": "up", "service": "${{ values.name }}"}


@app.get("/metrics")
def metrics():
    """Endpoint de métricas no formato Prometheus (text/plain)."""
    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST,
    )
