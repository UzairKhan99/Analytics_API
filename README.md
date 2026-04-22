
# Analytics API

A FastAPI-based Analytics API with Docker support, built for learning and scalable backend development.

## 🚀 Features

- FastAPI REST API
- Modular routing structure
- Dockerized environment
- Docker Compose support
- Development mode with auto-reload
- Jupyter notebooks for API testing

---

## ⚙️ Setup & Run

### 🔹 Using Docker Compose (Recommended)

```bash
docker compose up --build
````

Then open:

* API: [http://127.0.0.1:8002](http://127.0.0.1:8002)
* Docs: [http://127.0.0.1:8002/docs](http://127.0.0.1:8002/docs)

---

### 🔹 Without Docker

```bash
pip install -r requirements.txt
uvicorn src.main:app --reload
```

---

## 🧪 Testing API

You can test endpoints using:

* Swagger UI → `/docs`
* Jupyter notebooks inside `nbs/`
* Tools like Postman

Example endpoint:

```
GET /api/events
```

---

## 🐳 Docker Overview

* `Dockerfile.web` → builds the app environment
* `compose.yaml` → runs and manages the container
* `docker-run.sh` → starts the application

---

## 📌 Tech Stack

* FastAPI
* Uvicorn / Gunicorn
* Docker & Docker Compose
* Python 3.14

---

## 📈 Future Improvements

* Database integration (PostgreSQL / TimescaleDB)
* Authentication & authorization
* Logging & monitoring
* Deployment (AWS / Docker Hub)

---

## 👨‍💻 Author

Uzair Khan

---

