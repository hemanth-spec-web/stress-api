from fastapi import APIRouter
from models.prediction import PredictionInput, PredictionResponse
from services.stress_calculator import calculate_stress

router = APIRouter(prefix="/predict", tags=["Predictions"])


@router.post("", response_model=PredictionResponse)
def predict_stress(data: PredictionInput):
    return calculate_stress(data)