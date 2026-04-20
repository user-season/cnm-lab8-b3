1. Yêu cầu
Hệ điều hành: Linux, macOS, hoặc Windows (nên dùng WSL2).

Công cụ cần cài đặt:

Python 3.10+: Phù hợp nhất với các thư viện ML hiện tại.

Git: Để quản lý mã nguồn và đẩy lên GitHub (Hướng dẫn cài đặt từ git-scm.com).

Docker Desktop: Dùng để build và chạy container ở local trước khi đẩy lên cloud (Hướng dẫn cài đặt từ docs.docker.com).

Tài khoản: 1 tài khoản GitHub (chứa code) và 1 tài khoản Docker Hub (chứa Docker Image miễn phí).


2. Cấu trúc thư mục

Mô tả nhanh cấu trúc dự án và ý nghĩa các tệp/thư mục chính:

```
.
├── .github/
│   └── workflows/
│       ├── ci_cd.yml        # CI/CD: build, test, deploy tự động
│       └── rollback.yml     # Pipeline thủ công để rollback
├── app/
│   ├── main.py              # FastAPI server (entrypoint của API)
│   └── model_dummy.pkl      # Ví dụ file model (hoặc copy model thật vào đây)
├── tests/
│   ├── test_api.py          # Unit/integration tests cho API
│   └── test_model.py        # Tests cho logic/model
├── Dockerfile               # Đóng gói ứng dụng vào container
├── requirements.txt         # Danh sách dependencies (pip)
└── README.md                # Tài liệu dự án (bạn đang đọc)
```

Ghi chú ngắn:
- Thư mục `app/` chứa mã nguồn server và file model mẫu.
- `tests/` chứa các kịch bản kiểm thử tự động (pytest).
- `.github/workflows/` chứa các workflow CI/CD nếu bạn muốn tích hợp với GitHub Actions.

## Train model

```python
python train_model.py
```

## chạy thử (Local)

1. Clone repository về máy.
2. Tạo môi trường ảo và cài đặt thư viện:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Trên Windows dùng: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Chạy test
`pytest tests/`

4. Khởi chạy server FastAPI:
`uvicorn app.main:app --reload`

Truy cập: http://localhost:8000/docs để xem giao diện Swagger UI và test API.

