from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# Khởi tạo app
app = FastAPI(title="MLOps Lab 3 API", version="1.0")

# Load model khi app khởi động
try:
    model = joblib.load("app/model_dummy.pkl")
except Exception as e:
    model = None

# Định nghĩa cấu trúc dữ liệu đầu vào (Features của hoa Iris)
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def health_check():
    return {"status": "ok", "message": "API đang hoạt động"}

@app.post("/predict")
def predict(features: IrisFeatures):
    if model is None:
        raise HTTPException(status_code=500, detail="Mô hình chưa được tải.")
    
    # Chuyển đổi input thành mảng numpy để đưa vào model
    input_data = np.array([[
        features.sepal_length, 
        features.sepal_width, 
        features.petal_length, 
        features.petal_width
    ]])
    
    prediction = model.predict(input_data)
    
    # Trả về kết quả
    classes = ["Setosa", "Versicolor", "Virginica"]
    return {
        "prediction_class": int(prediction[0]),
        "prediction_label": classes[prediction[0]]
    }