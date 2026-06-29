from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field


class PredictionInput(BaseModel):
    heart_rate: float = Field(gt=0, description="Heart rate in BPM")
    skin_conductance: float = Field(ge=0, description="Skin conductance in microsiemens")
    temperature: float = Field(gt=0, description="Body temperature in Celsius")


class PredictionResponse(BaseModel):
    stress_score: float
    stress_level: str
    input_received: PredictionInput
from services.stress_calculator import calculate_stress
from database.connection import get_db
from database.models import PredictionDB

router = APIRouter(prefix="/predict", tags=["Predictions"])


@router.post("", response_model=PredictionResponse)
def predict_stress(data: PredictionInput, db: Session = Depends(get_db)):
    result = calculate_stress(data)

    # Save prediction to database
    db_prediction = PredictionDB(
        heart_rate=data.heart_rate,
        skin_conductance=data.skin_conductance,
        temperature=data.temperature,
        stress_score=result.stress_score,
        stress_level=result.stress_level
    )

    db.add(db_prediction)
    db.commit()

    return result


@router.get("/history", response_model=list[PredictionResponse])
def get_prediction_history(db: Session = Depends(get_db)):
    predictions = db.query(PredictionDB).all()
    return [
        PredictionResponse(
            stress_score=p.stress_score,
            stress_level=p.stress_level,
            input_received=PredictionInput(
                heart_rate=p.heart_rate,
                skin_conductance=p.skin_conductance,
                temperature=p.temperature
            )
        )
        for p in predictions
    ]