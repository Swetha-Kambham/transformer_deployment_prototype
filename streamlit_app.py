import streamlit as st
import requests

st.set_page_config(page_title="BERT Sentiment Inference", layout="centered")

st.title("🤖 Transformer Inference Demo")
st.markdown("Enter text below and get predictions from your FastAPI model.")

text_input = st.text_area("Enter Text", height=150)

if st.button("Predict"):
    if text_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Getting prediction..."):
            try:
                response = requests.post("http://localhost:8000/predict", json={"text": text_input})
                result = response.json()
                label = result.get("label")
                score = round(result.get("score", 0) * 100, 2)
                st.success(f"**Prediction:** {label} ({score}%)")
            except Exception as e:
                st.error(f"Error: {str(e)}")

st.markdown("---")
st.caption("Model: distilBERT SST-2 | Powered by FastAPI + Hugging Face")