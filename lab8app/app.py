from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import mlflow
import mlflow.sklearn
from mlflow.tracking import MlflowClient
import os

app = FastAPI()

class InputVector(BaseModel):
    vector: list

@app.on_event("startup")
def load_model():
    global model
    tracking_dir = os.path.abspath("../labs/mlruns")
    mlflow.set_tracking_uri(f"file://{tracking_dir}")
    client = MlflowClient()
    model_name = "best-rf-model-fastapi"
    versions = client.get_latest_versions(model_name)
    latest_version = max(versions, key=lambda v: int(v.version))
    model = mlflow.sklearn.load_model(f"models:/{model_name}/{latest_version.version}")
    print(f"Loaded model: {model_name} version {latest_version.version}")

@app.post("/predict")
def predict(input_data: InputVector):
    features = np.array(input_data.vector).reshape(1, -1)
    prediction = model.predict(features)[0]
    # Convert numpy.int64 to a native Python int
    prediction = int(prediction)
    return {"prediction": prediction}
