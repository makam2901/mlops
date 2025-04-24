import requests

url = "http://127.0.0.1:8000/predict"
data = {
    "vector": [63, 1, 1, 145, 233, 1, 2, 150, 0, 2.3, 0, 0, 1]
}

response = requests.post(url, json=data)
print("Prediction response:", response.json())