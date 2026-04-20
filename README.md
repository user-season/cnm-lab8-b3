1. Yêu cầu
Hệ điều hành: Linux, macOS, hoặc Windows (nên dùng WSL2).

Công cụ cần cài đặt:

Python 3.10+: Phù hợp nhất với các thư viện ML hiện tại.

Git: Để quản lý mã nguồn và đẩy lên GitHub (Hướng dẫn cài đặt từ git-scm.com).

Docker Desktop: Dùng để build và chạy container ở local trước khi đẩy lên cloud (Hướng dẫn cài đặt từ docs.docker.com).

Tài khoản: 1 tài khoản GitHub (chứa code) và 1 tài khoản Docker Hub (chứa Docker Image miễn phí).


2. Cấu trúc thư mục
.
├── .github/
│   └── workflows/
│       ├── ci_cd.yml        # Pipeline tự động Build, Test, Deploy
│       └── rollback.yml     # Pipeline chạy thủ công để Rollback
├── app/
│   ├── main.py              # API server (FastAPI)
│   └── model_dummy.pkl      # File model (bạn tạo 1 file dummy hoặc copy model cũ vào)
├── tests/
│   ├── test_api.py          # Script kiểm thử API
│   └── test_model.py        # Script kiểm thử chất lượng model
├── Dockerfile               # File đóng gói hệ thống
├── requirements.txt         # Các thư viện cần thiết
└── README.md


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

