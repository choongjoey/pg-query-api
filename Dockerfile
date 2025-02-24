FROM python:3.13-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy application code
COPY app/ .

# Expose the FastAPI default port
EXPOSE 8000

# Command to run the FastAPI app
CMD ["fastapi", "run", "main.py", "--port", "8000"]
