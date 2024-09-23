FROM python:3.12-alpine

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy the application into the container.
COPY . /app

# Install the application dependencies.
WORKDIR /app
RUN uv sync --frozen --no-cache

EXPOSE 8000
CMD ["/app/.venv/bin/fastapi", "run", "src/main.py", "--port", "8000"]