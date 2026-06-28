from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# ── Pydantic model — defines shape of incoming data ──
class StudentInput(BaseModel):
    name: str
    age: int
    cgpa: float


class PredictionInput(BaseModel):
    heart_rate: float
    skin_conductance: float
    temperature: float


# ── GET endpoints ─────────────────────────────────────
@app.get("/")
def read_root():
    return {"message": "Stress Detection API v1"}


@app.get("/student/{name}")
def get_student(name: str):
    return {
        "name": name,
        "college": "NIT Warangal",
        "branch": "ECE"
    }


@app.get("/health")
def health_check():
    return {"status": "ok"}


# ── POST endpoints ────────────────────────────────────
@app.post("/student")
def create_student(student: StudentInput):
    return {
        "message": f"Student {student.name} registered",
        "data": {
            "name": student.name,
            "age": student.age,
            "cgpa": student.cgpa,
            "eligible": student.cgpa >= 7.5
        }
    }


@app.post("/predict")
def predict_stress(data: PredictionInput):
    # Simple rule-based prediction (we'll replace with real model later)
    stress_score = (
        (data.heart_rate - 70) * 0.4 +
        data.skin_conductance * 0.4 +
        (data.temperature - 36.5) * 0.2
    )
    level = "high" if stress_score > 5 else "low"

    return {
        "stress_score": round(stress_score, 2),
        "stress_level": level,
        "input_received": {
            "heart_rate": data.heart_rate,
            "skin_conductance": data.skin_conductance,
            "temperature": data.temperature
        }
    }