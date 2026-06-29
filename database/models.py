from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.sql import func
from database.connection import Base


class StudentDB(Base):
    __tablename__ = "students"

    id         = Column(Integer, primary_key=True, index=True)
    name       = Column(String, unique=True, index=True)
    age        = Column(Integer)
    cgpa       = Column(Float)
    eligible   = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())


class PredictionDB(Base):
    __tablename__ = "predictions"

    id               = Column(Integer, primary_key=True, index=True)
    heart_rate       = Column(Float)
    skin_conductance = Column(Float)
    temperature      = Column(Float)
    stress_score     = Column(Float)
    stress_level     = Column(String)
    created_at       = Column(DateTime, server_default=func.now())