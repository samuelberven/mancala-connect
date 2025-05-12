# Use official Python image
FROM python:3.10-slim
# FROM python:3.10

# Set the working directory
WORKDIR /app

# Create a non-root user
RUN adduser --disabled-password appuser && chown -R appuser /app
USER appuser

# Copy dependencies
COPY requirements.txt .

# Switch to root for package installation
USER root
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get remove -y gcc python3-dev && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

# Switch back to the application user
USER appuser
COPY . .

# Run the FastAPI server with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]


# FROM python:3.10-slim

# WORKDIR /app

# # Create a non-root user and set ownership of the working directory
# RUN adduser --disabled-password appuser && chown -R appuser /app
# USER appuser

# # Install build dependencies, install requirements, then remove build dependencies
# COPY requirements.txt .
# USER root
# RUN apt-get update && \
#     apt-get install -y --no-install-recommends gcc python3-dev && \
#     pip install --no-cache-dir -r requirements.txt && \
#     apt-get remove -y gcc python3-dev && \
#     apt-get autoremove -y && \
#     rm -rf /var/lib/apt/lists/*

# COPY . .

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]


