# Transformer Deployment Prototype (with Streamlit UI)

This project demonstrates how to deploy a Hugging Face transformer model using FastAPI with GPU support (CUDA), Docker, and Prometheus monitoring. A Streamlit frontend is also included for interactive testing.

---

## 🔧 Features

- BERT-based sentiment analysis using Hugging Face Transformers
- FastAPI backend with `/predict` endpoint
- GPU inference with PyTorch + CUDA
- Prometheus metrics at `http://localhost:8001`
- Streamlit UI frontend for interactive testing
- Dockerized for easy deployment

---

## Local Setup

### 1. Clone the repo and navigate to it
```bash
cd transformer_deployment_prototype
```

### 2. (Optional) Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
pip install streamlit
```

---

##  Run the FastAPI Backend
```bash
uvicorn app:app --reload
```

- API available at: `http://localhost:8000`
- Swagger docs at: `http://localhost:8000/docs`
- Prometheus metrics: `http://localhost:8001`

---

## Run the Streamlit UI
In another terminal:

```bash
streamlit run streamlit_app.py
```

Open browser at: `http://localhost:8501`

Enter your text, click "Predict", and get results from the FastAPI model.

---

## Docker Deployment

To run inside Docker:

```bash
docker build -t bert-api .
docker run -p 8000:8000 --gpus all bert-api
```

---

## Test the API (curl)
```bash
curl -X POST http://localhost:8000/predict \
     -H "Content-Type: application/json" \
     -d '{"text": "This is amazing!"}'
```

---

## Tech Stack

- Python, FastAPI, Uvicorn
- Hugging Face Transformers (BERT SST-2)
- PyTorch with CUDA
- Docker
- Prometheus
- Streamlit

---