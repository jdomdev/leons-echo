# Backend (skeleton)

## Requisitos

- Python 3.12
- [uv](https://docs.astral.sh/uv/)

## Ejecutar en local (<= 5 minutos)

```bash
cd backend
uv sync --group dev
uv run uvicorn app.main:app --app-dir src --reload
```

Health check:

```bash
curl http://127.0.0.1:8000/health
```

Respuesta esperada:

```json
{"status":"ok"}
```

## Validación rápida

```bash
cd backend
uv run ruff check .
uv run mypy .
uv run pytest -q
```
