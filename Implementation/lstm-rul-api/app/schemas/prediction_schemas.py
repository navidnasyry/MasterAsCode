from pydantic import BaseModel, Field
from typing import List


class EngineData(BaseModel):
    data: List[List[float]] = Field(
        ...,
        description="List of time steps with feature values for RUL prediction."
    )


class PredictionResponse(BaseModel):
    predicted_rul: float


class EngineRULResponse(BaseModel):
    engine_number: int
    predicted_rul: float
