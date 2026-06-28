from pydantic import BaseModel, Field


class StudentInput(BaseModel):
    name: str
    age: int
    cgpa: float = Field(ge=0.0, le=10.0)  # must be between 0 and 10


class StudentResponse(BaseModel):
    name: str
    age: int
    cgpa: float
    eligible: bool