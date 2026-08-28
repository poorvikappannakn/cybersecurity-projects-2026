from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.database.connection import SessionLocal
from backend.models.user import User
from backend.services.auth import hash_password, verify_password
from backend.services.jwt import create_access_token
from backend.services.security import get_current_user
from backend.services.rbac import require_role

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)


class RegisterRequest(BaseModel):
    username: str
    password: str


class LoginRequest(BaseModel):
    username: str
    password: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/admin")
def admin_only(
    current_user: dict = Depends(require_role("admin"))
):
    return {
        "message": "Welcome, admin",
        "user_id": current_user["sub"]
    }

@router.get("/me")
def get_me(current_user: dict = Depends(get_current_user)):
    return {
        "user_id": current_user["sub"],
        "role": current_user["role"]
    }

@router.post("/register")
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(
        User.username == request.username
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    password_hash = hash_password(request.password)

    user = User(
        username=request.username,
        password_hash=password_hash
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "message": "User registered successfully",
        "username": user.username
    }


@router.post("/login")
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.username == request.username
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    if not verify_password(
        request.password,
        user.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    access_token = create_access_token(
        user.id,
        user.role
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }