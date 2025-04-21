from metaflow import FlowSpec, step, Parameter, JSONType, resources, retry, timeout, catch, conda
import mlflow
import mlflow.sklearn
from mlflow.tracking import MlflowClient
import numpy as np
import os

class RandomForestGCPPredictFlow(FlowSpec):

    vector = Parameter('vector', type=JSONType, required=True)

    @resources(cpu=1, memory=2048)
    @retry(times=2)
    @timeout(seconds=120)
    @step
    def start(self):
        self.features = np.array(self.vector).reshape(1, -1)
        print("Received input vector:", self.features)
        self.next(self.load_model)

    @conda(libraries={"mlflow": "2.3.0", "scikit-learn": "1.2.2"})
    @resources(cpu=2, memory=4096)
    @timeout(seconds=300)
    @retry(times=2)
    @catch(var="load_model_error")
    @step
    def load_model(self):
        mlflow.set_tracking_uri("https://mlflow-run-259594885820.us-west2.run.app")
        mlflow.set_experiment("metaflow-gcp-resources-kubernetes")

        client = MlflowClient()
        model_name = "best-rf-model-gcp"
        versions = client.get_latest_versions(model_name, stages=[])
        latest_version = max(versions, key=lambda v: int(v.version))
        self.model = mlflow.sklearn.load_model(f"models:/{model_name}/{latest_version.version}")
        print(f"Loaded model '{model_name}' version {latest_version.version}")
        self.next(self.predict)

    @resources(cpu=1, memory=2048)
    @step
    def predict(self):
        self.prediction = self.model.predict(self.features)[0]
        print(f"Predicted class: {self.prediction}")
        self.next(self.end)

    @step
    def end(self):
        print(f"Successfully performed prediction!")

if __name__ == '__main__':
    RandomForestGCPPredictFlow()