from fastapi import HTTPException
from models.prediction import PredictionInput, PredictionResponse

STRESS_THRESHOLD    = 5.0
HEART_RATE_BASELINE = 70.0
TEMP_BASELINE       = 36.5

# Physiologically valid ranges
HEART_RATE_MIN, HEART_RATE_MAX       = 30.0,  220.0
SKIN_CONDUCTANCE_MIN, SKIN_CONDUCTANCE_MAX = 0.0, 100.0
TEMPERATURE_MIN, TEMPERATURE_MAX     = 34.0,  42.0


def validate_sensor_data(data: PredictionInput):
    """Raise 422 if any sensor reading is physiologically impossible."""
    errors = []

    if not HEART_RATE_MIN <= data.heart_rate <= HEART_RATE_MAX:
        errors.append(
            f"heart_rate {data.heart_rate} outside valid range "
            f"[{HEART_RATE_MIN}, {HEART_RATE_MAX}]"
        )

    if not SKIN_CONDUCTANCE_MIN <= data.skin_conductance <= SKIN_CONDUCTANCE_MAX:
        errors.append(
            f"skin_conductance {data.skin_conductance} outside valid range "
            f"[{SKIN_CONDUCTANCE_MIN}, {SKIN_CONDUCTANCE_MAX}]"
        )

    if not TEMPERATURE_MIN <= data.temperature <= TEMPERATURE_MAX:
        errors.append(
            f"temperature {data.temperature} outside valid range "
            f"[{TEMPERATURE_MIN}, {TEMPERATURE_MAX}]"
        )

    if errors:
        raise HTTPException(
            status_code=422,
            detail={"errors": errors}
        )


def calculate_stress(data: PredictionInput) -> PredictionResponse:
    """
    Calculate stress score from physiological signals.

    Formula weights:
    - Heart rate deviation: 40%
    - Skin conductance:     40%
    - Temperature deviation: 20%
    """
    validate_sensor_data(data)

    heart_rate_deviation = data.heart_rate - HEART_RATE_BASELINE
    temp_deviation       = data.temperature - TEMP_BASELINE

    stress_score = (
        heart_rate_deviation * 0.4 +
        data.skin_conductance * 0.4 +
        temp_deviation * 0.2
    )

    stress_level = "high" if stress_score > STRESS_THRESHOLD else "low"

    return PredictionResponse(
        stress_score=round(stress_score, 2),
        stress_level=stress_level,
        input_received=data
    )