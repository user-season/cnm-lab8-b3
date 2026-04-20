import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# 1. Tải dữ liệu
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

# 2. Huấn luyện mô hình
model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X_train, y_train)

# 3. Lưu mô hình vào thư mục app/
joblib.dump(model, 'app/model_dummy.pkl')
print("Đã lưu mô hình thành công tại app/model_dummy.pkl")
