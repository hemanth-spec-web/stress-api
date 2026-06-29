from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import students, predictions
from database.connection import engine
from database import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Stress Detection API",
    description="Physiological stress detection using ECG, EDA and temperature signals",
    version="2.0.0"
)

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # in production, specify exact domain
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(students.router)
app.include_router(predictions.router)

@app.get("/", tags=["Health"])
def read_root():
    return {"message": "Stress Detection API v2", "status": "ok"}

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}