from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import torch
from prometheus_client import start_http_server, Summary

class InputText(BaseModel):
    text: str

app = FastAPI()

# Prometheus metric
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@app.on_event("startup")
def setup_metrics():
    start_http_server(8001)  # Prometheus metrics on port 8001

# Load model
device = 0 if torch.cuda.is_available() else -1
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english", device=device)

@app.post("/predict")
@REQUEST_TIME.time()
def predict(input_data: InputText):
    result = classifier(input_data.text)
    return {"label": result[0]["label"], "score": result[0]["score"]}