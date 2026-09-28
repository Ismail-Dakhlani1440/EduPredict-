FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:0.12.13 /uv /bin/uv
RUN apt-get update && apt-get install -y --no-install-recommends libgomp1 \ 
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev --no-install-project

COPY src/ ./src/
COPY app.py ./
COPY models/ ./models/
RUN uv sync --locked --no-dev

ENV PATH="/app/.venv/bin:$PATH"
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501"]
