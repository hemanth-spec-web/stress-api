from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.student import StudentInput, StudentResponse
from database.connection import get_db
from database.models import StudentDB

router = APIRouter(prefix="/student", tags=["Students"])


@router.get("/{name}", response_model=StudentResponse)
def get_student(name: str, db: Session = Depends(get_db)):
    student = db.query(StudentDB).filter(
        StudentDB.name.ilike(name)  # case-insensitive search
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail=f"Student '{name}' not found"
        )

    return student


@router.post("", response_model=StudentResponse)
def create_student(student: StudentInput, db: Session = Depends(get_db)):
    # Check if already exists
    existing = db.query(StudentDB).filter(
        StudentDB.name.ilike(student.name)
    ).first()

    if existing:
        raise HTTPException(
            status_code=409,
            detail=f"Student '{student.name}' already exists"
        )

    # Create database record
    db_student = StudentDB(
        name=student.name,
        age=student.age,
        cgpa=student.cgpa,
        eligible=student.cgpa >= 7.5
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student


@router.get("", response_model=list[StudentResponse])
def get_all_students(db: Session = Depends(get_db)):
    return db.query(StudentDB).all()