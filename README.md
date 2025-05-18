# Transformer Deployment Prototype

This project demonstrates how to deploy a Hugging Face transformer model (`distilbert-base-uncased-finetuned-sst-2-english`) using FastAPI. It includes Docker support and Prometheus monitoring.

## Features

- GPU-based inference (if available)
- Sentiment analysis using Hugging Face Transformers
- FastAPI REST API
- Prometheus metrics
- Docker containerization

## Setup

### Run locally

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

### Run with Docker

```bash
docker build -t bert-api .
docker run -p 8000:8000 --gpus all bert-api
```

### Test the API

```bash
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{"text": "I love this!"}'
```

Prometheus metrics available at `http://localhost:8001`
