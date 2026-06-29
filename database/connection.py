from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# SQLite database file — created automatically
DATABASE_URL = "sqlite:///./stress_api.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # needed for SQLite only
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    """
    Dependency that provides a database session per request.
    Automatically closes session when request is done.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()