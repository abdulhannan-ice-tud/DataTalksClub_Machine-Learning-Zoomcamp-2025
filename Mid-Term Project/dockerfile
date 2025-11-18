# Use official lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies (for pandas, sklearn, numpy)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app/

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir pandas matplotlib scikit-learn uvicorn FastAPI seaborn

# Expose FastAPI portu
EXPOSE 8000

# Run FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
