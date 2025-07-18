import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from contextlib import asynccontextmanager

# Load the model and dataset
class PredictionInput(BaseModel):
    text: str

# Lifespan context
@asynccontextmanager
async def lifespan(app: FastAPI):
    global model, dataset
    try:
        model = joblib.load("sentiment_model.pkl")
        print("Model loaded.")
    except FileNotFoundError as e:
        print(f"Could not load model 'sentiment_model.pkl': {e}")
        print("Please run the 'train.py' script first to generate the model file.")
        model = None

    try:
        dataset = pd.read_csv("IMDB Dataset.csv")
        print("Dataset loaded.")
    except Exception as e:
        print(f"Could not load dataset: {e}")
        dataset = None

    yield
    # Cleanup if needed on shutdown

# FastAPI app
app = FastAPI(
    title="Sentiment Analysis API",
    lifespan=lifespan
)

@app.get("startup")
def startup_event():
    """
    A startup event handler. It checks if the model was loaded correctly.
    If not, it prints a persistent warning.
    """
    if model is None:
        print("WARNING: Model is not loaded. Prediction endpoints will not work.")

@app.get("/health")
def health_check():
    """
    Health Check Endpoint
    This endpoint is used to verify that the API server is running and responsive.
    It's a common practice for monitoring services.
    """
    return {"status": "ok", "message": "API is running"}

@app.post("/predict")
def predict(input_data: PredictionInput):
    """
    Prediction Endpoint
    Takes a feature vector and returns a sentiment prediction (0 or 1).
    """
    if model is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Model is not loaded. Cannot make predictions."
        )

    # Get the prediction  
    prediction = model.predict([input_data.text])[0]
    
    return {"sentiment": prediction}

@app.post("/predict_proba")
def predict_proba(input_data: PredictionInput):
    """
    Probability Prediction Endpoint
    Takes a feature vector and returns the probability of the positive class.
    """
    if model is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Model is not loaded. Cannot make predictions."
        )

    # Get the prediction and probabilities
    prediction = model.predict([input_data.text])[0]  
    probabilities = model.predict_proba([input_data.text])[0]
    
    # Get the index for the sentiment based on the prediction
    sentiment_index = 1 if prediction == 'positive' else 0

    return {
        "sentiment": prediction,
        "probability": probabilities[sentiment_index]
    }

@app.get("/example")
def example():
    """
    Example Endpoint
    Returns an example input and its expected output.
    """
    if dataset is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Dataset is not loaded. Cannot provide example."
        )
    
    # Randomly select an example from the dataset
    example_row = dataset.sample().iloc[0]
    return {"review": example_row["review"]}