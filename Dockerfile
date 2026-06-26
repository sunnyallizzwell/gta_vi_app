# Using slim image for a smaller footprint on your server
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY game_info_service.py .

# Expose the internal port
EXPOSE 8001

# Run the application
CMD ["uvicorn", "game_info_service:app", "--host", "0.0.0.0", "--port", "8001"]
