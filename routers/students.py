from fastapi import APIRouter
from models.student import StudentInput, StudentResponse

router = APIRouter(prefix="/student", tags=["Students"])


@router.get("/{name}")
def get_student(name: str):
    return {
        "name": name,
        "college": "NIT Warangal",
        "branch": "ECE"
    }


@router.post("", response_model=StudentResponse)
def create_student(student: StudentInput):
    return StudentResponse(
        name=student.name,
        age=student.age,
        cgpa=student.cgpa,
        eligible=student.cgpa >= 7.5
    )