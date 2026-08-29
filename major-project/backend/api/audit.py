from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database.connection import SessionLocal
from backend.models.audit_log import AuditLog
from backend.services.rbac import require_role


router = APIRouter(
    prefix="/api/audit",
    tags=["Audit Logs"]
)


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.get("/")
def list_audit_logs(
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_role("admin"))
):
    logs = db.query(AuditLog).order_by(
        AuditLog.timestamp.desc()
    ).all()

    return [
        {
            "id": log.id,
            "user_id": log.user_id,
            "action": log.action,
            "details": log.details,
            "timestamp": log.timestamp
        }
        for log in logs
    ]