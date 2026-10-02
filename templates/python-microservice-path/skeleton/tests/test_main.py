"""
Testes automatizados para o microsserviço ${{ values.name }}.
Utiliza pytest + httpx para testar a API FastAPI.
"""

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


class TestHealthEndpoint:
    """Testes do endpoint /health."""

    def test_health_returns_200(self):
        response = client.get("/health")
        assert response.status_code == 200

    def test_health_returns_status_up(self):
        response = client.get("/health")
        data = response.json()
        assert data["status"] == "up"

    def test_health_returns_service_name(self):
        response = client.get("/health")
        data = response.json()
        assert "service" in data


class TestMetricsEndpoint:
    """Testes do endpoint /metrics (formato Prometheus)."""

    def test_metrics_returns_200(self):
        response = client.get("/metrics")
        assert response.status_code == 200

    def test_metrics_returns_prometheus_format(self):
        response = client.get("/metrics")
        content_type = response.headers.get("content-type", "")
        assert "text/plain" in content_type or "text/plain" in content_type

    def test_metrics_contains_http_requests_total(self):
        # Faz uma requisição primeiro para gerar métricas
        client.get("/health")
        response = client.get("/metrics")
        assert b"http_requests_total" in response.content
