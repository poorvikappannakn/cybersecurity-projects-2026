from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.database.connection import SessionLocal
from backend.models.event import Event
from backend.models.participant import Participant
from backend.models.campaign import Campaign
from backend.services.security import get_current_user


router = APIRouter(
    prefix="/api/events",
    tags=["Events"]
)


class EventCreateRequest(BaseModel):
    participant_id: int
    campaign_id: int
    event_type: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_event(
    request: EventCreateRequest,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    allowed_event_types = {
        "email_delivered",
        "email_opened",
        "link_clicked",
        "credential_submitted"
    }

    if request.event_type not in allowed_event_types:
        raise HTTPException(
            status_code=400,
            detail="Invalid event type"
        )

    participant = db.query(Participant).filter(
        Participant.id == request.participant_id
    ).first()

    if not participant:
        raise HTTPException(
            status_code=404,
            detail="Participant not found"
        )

    campaign = db.query(Campaign).filter(
        Campaign.id == request.campaign_id
    ).first()

    if not campaign:
        raise HTTPException(
            status_code=404,
            detail="Campaign not found"
        )

    if participant.campaign_id != campaign.id:
        raise HTTPException(
            status_code=400,
            detail="Participant does not belong to this campaign"
        )

    if campaign.status != "active":
        raise HTTPException(
            status_code=400,
            detail="Campaign is not active"
        )

    event = Event(
        participant_id=participant.id,
        campaign_id=campaign.id,
        event_type=request.event_type,
        timestamp=datetime.now(timezone.utc)
    )

    db.add(event)
    db.commit()
    db.refresh(event)

    return {
        "message": "Event recorded successfully",
        "event_id": event.id,
        "participant_id": event.participant_id,
        "campaign_id": event.campaign_id,
        "event_type": event.event_type,
        "timestamp": event.timestamp
    }


@router.get("/")
def list_events(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return db.query(Event).all()


@router.get("/{event_id}")
def get_event(
    event_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    event = db.query(Event).filter(
        Event.id == event_id
    ).first()

    if not event:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    return event