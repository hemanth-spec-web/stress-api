from fastapi import FastAPI
from routers import students, predictions

app = FastAPI(
    title="Stress Detection API",
    description="Physiological stress detection using ECG, EDA and temperature signals",
    version="1.0.0"
)

# Register routers
app.include_router(students.router)
app.include_router(predictions.router)


@app.get("/", tags=["Health"])
def read_root():
    return {"message": "Stress Detection API v1", "status": "ok"}


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}