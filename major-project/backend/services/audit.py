from sqlalchemy.orm import Session

from backend.models.audit_log import AuditLog


def record_audit(
    db: Session,
    current_user: dict,
    action: str,
    details: str
):
    user_id = int(current_user["sub"])

    audit_log = AuditLog(
        user_id=user_id,
        action=action,
        details=details
    )

    db.add(audit_log)
    db.commit()
    db.refresh(audit_log)

    return audit_log