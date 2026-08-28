from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.database.connection import SessionLocal
from backend.models.participant import Participant
from backend.models.campaign import Campaign
from backend.services.rbac import require_role
from backend.services.security import get_current_user


router = APIRouter(
    prefix="/api/participants",
    tags=["Participants"]
)


class ParticipantCreateRequest(BaseModel):
    campaign_id: int
    identifier: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_participant(
    request: ParticipantCreateRequest,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_role("admin"))
):
    campaign = db.query(Campaign).filter(
        Campaign.id == request.campaign_id
    ).first()

    if not campaign:
        raise HTTPException(
            status_code=404,
            detail="Campaign not found"
        )

    participant = Participant(
        campaign_id=request.campaign_id,
        identifier=request.identifier
    )

    db.add(participant)
    db.commit()
    db.refresh(participant)

    return {
        "message": "Participant created successfully",
        "participant_id": participant.id,
        "campaign_id": participant.campaign_id,
        "identifier": participant.identifier
    }


@router.get("/")
def list_participants(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return db.query(Participant).all()


@router.get("/{participant_id}")
def get_participant(
    participant_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    participant = db.query(Participant).filter(
        Participant.id == participant_id
    ).first()

    if not participant:
        raise HTTPException(
            status_code=404,
            detail="Participant not found"
        )

    return participant