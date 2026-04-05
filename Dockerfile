FROM python:3.11-slim

WORKDIR /app

# Copy your files into the container
COPY . .

# Install the same libraries we just installed locally
RUN pip install fastapi uvicorn pydantic openenv-core

# Hugging Face Spaces usually runs on port 7860
EXPOSE 7860

# Start the server
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "7860"]