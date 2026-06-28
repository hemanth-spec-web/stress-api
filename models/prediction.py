from pydantic import BaseModel, Field


class PredictionInput(BaseModel):
    heart_rate: float = Field(gt=0, description="Heart rate in BPM")
    skin_conductance: float = Field(ge=0, description="Skin conductance in microsiemens")
    temperature: float = Field(gt=0, description="Body temperature in Celsius")


class PredictionResponse(BaseModel):
    stress_score: float
    stress_level: str
    input_received: PredictionInput