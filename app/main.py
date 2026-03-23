from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
from .schema import ChurnInput, ChurnPrediction
from .model_loader import load_model
import pandas as pd
import uvicorn

app = FastAPI(title="Bank Churn Prediction API")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

try:
    model = load_model()
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open(os.path.join(BASE_DIR, "index.html"), "r") as f:
        return f.read()

@app.post("/predict", response_model=ChurnPrediction)
def predict(data: ChurnInput):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")
    
    input_dict = data.dict()
    df = pd.DataFrame([input_dict])
    
    try:
        prob = model.predict_proba(df)[0, 1]
        prediction = int(prob > 0.5)
        
        return ChurnPrediction(
            churn_probability=float(prob),
            prediction=prediction
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)