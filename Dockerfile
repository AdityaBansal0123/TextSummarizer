# Use a slim Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies only if required (build-essential is heavy, so skip unless needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first
COPY requirements.txt .

# Install Python dependencies (no cache, no extra bloat)
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy only application source code (not venv, not data, not models)
COPY app.py .
COPY src/ ./src

# Expose FastAPI default port
EXPOSE 8000

# Run FastAPI with Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
