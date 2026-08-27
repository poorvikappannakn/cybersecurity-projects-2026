from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "sqlite:///./major_project.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)
from sqlalchemy.orm import Session, sessionmaker
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    pass