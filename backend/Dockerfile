FROM python:3.10-slim

WORKDIR /app

# Create a non-root user and set ownership of the working directory
RUN adduser --disabled-password appuser && chown -R appuser /app
USER appuser

# Install build dependencies, install requirements, then remove build dependencies
COPY requirements.txt .
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get remove -y gcc python3-dev && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]


