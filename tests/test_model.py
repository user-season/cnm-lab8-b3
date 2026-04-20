import joblib
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
import os

def test_model_accuracy():
    # Kiểm tra xem file model có tồn tại không
    assert os.path.exists("app/model_dummy.pkl"), "Không tìm thấy file model"
    
    model = joblib.load("app/model_dummy.pkl")
    data = load_iris()
    
    # Giả lập test trên toàn bộ tập dữ liệu (hoặc bạn có thể chia tập test riêng)
    predictions = model.predict(data.data)
    accuracy = accuracy_score(data.target, predictions)
    
    # Đặt ngưỡng chấp nhận: Accuracy phải lớn hơn 80%
    assert accuracy >= 0.80, f"Độ chính xác của mô hình quá thấp: {accuracy:.2f}"