from fastapi import APIRouter, HTTPException
from models.student import StudentInput, StudentResponse

router = APIRouter(prefix="/student", tags=["Students"])

# Fake database for now
STUDENTS_DB = {
    "hemanth": {"name": "Hemanth", "college": "NIT Warangal", "branch": "ECE"},
    "rahul":   {"name": "Rahul",   "college": "IIT Bombay",   "branch": "CS"},
}


@router.get("/{name}")
def get_student(name: str):
    student = STUDENTS_DB.get(name.lower())

    if not student:
        raise HTTPException(
            status_code=404,
            detail=f"Student '{name}' not found"
        )

    return student


@router.post("", response_model=StudentResponse)
def create_student(student: StudentInput):
    if student.name.lower() in STUDENTS_DB:
        raise HTTPException(
            status_code=409,
            detail=f"Student '{student.name}' already exists"
        )

    return StudentResponse(
        name=student.name,
        age=student.age,
        cgpa=student.cgpa,
        eligible=student.cgpa >= 7.5
    )