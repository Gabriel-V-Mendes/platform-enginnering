# Estágio 1: Build
FROM python:3.11-slim AS build
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Estágio 2: Produção Segura
FROM python:3.11-slim
WORKDIR /app
# Criação de usuário non-root (Regra de Ouro)
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
COPY --from=build /install /usr/local
COPY src/ /app/src/
USER appuser
EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
