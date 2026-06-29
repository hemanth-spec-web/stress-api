from fastapi import FastAPI
from routers import students, predictions
from database.connection import engine
from database import models

# Create all tables on startup
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Stress Detection API",
    description="Physiological stress detection using ECG, EDA and temperature signals",
    version="2.0.0"
)

app.include_router(students.router)
app.include_router(predictions.router)


@app.get("/", tags=["Health"])
def read_root():
    return {"message": "Stress Detection API v2", "status": "ok"}


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}