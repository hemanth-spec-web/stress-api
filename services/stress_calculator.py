from models.prediction import PredictionInput, PredictionResponse


STRESS_THRESHOLD = 5.0
HEART_RATE_BASELINE = 70.0
TEMP_BASELINE = 36.5


def calculate_stress(data: PredictionInput) -> PredictionResponse:
    """
    Calculate stress score from physiological signals.

    Formula weights:
    - Heart rate deviation: 40%
    - Skin conductance: 40%
    - Temperature deviation: 20%
    """
    heart_rate_deviation = data.heart_rate - HEART_RATE_BASELINE
    temp_deviation = data.temperature - TEMP_BASELINE

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