# Stress Detection API

A FastAPI backend for physiological stress detection using ECG, EDA, and temperature signals.

## Features
- Student registration and management
- Real-time stress prediction from sensor data
- Persistent SQLite database
- Input validation and error handling

## Tech Stack
- FastAPI — web framework
- SQLAlchemy — ORM
- Pydantic — data validation
- Uvicorn — ASGI server
- SQLite — database

## Running Locally

```bash
# Clone the repo
git clone https://github.com/hemanth-spec-web/stress-api.git
cd stress-api

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Health check |
| GET | /health | Server status |
| POST | /student | Register student |
| GET | /student | Get all students |
| GET | /student/{name} | Get student by name |
| POST | /predict | Predict stress level |
| GET | /predict/history | Get prediction history |

## API Documentation
Visit `/docs` for interactive Swagger UI documentation.