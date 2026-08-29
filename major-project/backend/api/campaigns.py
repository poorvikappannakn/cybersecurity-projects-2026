from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.database.connection import SessionLocal
from backend.models.campaign import Campaign
from backend.models.participant import Participant
from backend.models.event import Event
from backend.services.rbac import require_role
from backend.services.security import get_current_user
from backend.services.audit import record_audit


router = APIRouter(
    prefix="/api/campaigns",
    tags=["Campaigns"]
)


class CampaignCreateRequest(BaseModel):
    name: str
    description: str


class CampaignStatusRequest(BaseModel):
    status: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_campaign(
    request: CampaignCreateRequest,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_role("admin"))
):
    campaign = Campaign(
        name=request.name,
        description=request.description,
        status="draft"
    )

    db.add(campaign)
    db.commit()
    db.refresh(campaign)

    record_audit(
        db,
        current_user,
        "CREATE_CAMPAIGN",
        f"Created campaign {campaign.id}: {campaign.name}"
    )

    return {
        "message": "Campaign created successfully",
        "campaign_id": campaign.id,
        "name": campaign.name,
        "status": campaign.status
    }


@router.get("/")
def list_campaigns(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return db.query(Campaign).all()


@router.get("/{campaign_id}")
def get_campaign(
    campaign_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    campaign = db.query(Campaign).filter(
        Campaign.id == campaign_id
    ).first()

    if not campaign:
        raise HTTPException(
            status_code=404,
            detail="Campaign not found"
        )

    return campaign


@router.patch("/{campaign_id}/status")
def update_campaign_status(
    campaign_id: int,
    request: CampaignStatusRequest,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_role("admin"))
):
    campaign = db.query(Campaign).filter(
        Campaign.id == campaign_id
    ).first()

    if not campaign:
        raise HTTPException(
            status_code=404,
            detail="Campaign not found"
        )

    allowed_statuses = {
        "draft",
        "active",
        "completed"
    }

    if request.status not in allowed_statuses:
        raise HTTPException(
            status_code=400,
            detail="Invalid campaign status"
        )

    old_status = campaign.status

    campaign.status = request.status

    db.commit()
    db.refresh(campaign)

    record_audit(
        db,
        current_user,
        "UPDATE_CAMPAIGN_STATUS",
        f"Campaign {campaign.id} changed from "
        f"{old_status} to {campaign.status}"
    )

    return {
        "message": "Campaign status updated",
        "campaign_id": campaign.id,
        "status": campaign.status
    }


@router.get("/{campaign_id}/analytics")
def get_campaign_analytics(
    campaign_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    campaign = db.query(Campaign).filter(
        Campaign.id == campaign_id
    ).first()

    if not campaign:
        raise HTTPException(
            status_code=404,
            detail="Campaign not found"
        )

    total_participants = db.query(Participant).filter(
        Participant.campaign_id == campaign_id
    ).count()

    total_events = db.query(Event).filter(
        Event.campaign_id == campaign_id
    ).count()

    emails_opened = db.query(Event).filter(
        Event.campaign_id == campaign_id,
        Event.event_type == "email_opened"
    ).count()

    links_clicked = db.query(Event).filter(
        Event.campaign_id == campaign_id,
        Event.event_type == "link_clicked"
    ).count()

    credentials_submitted = db.query(Event).filter(
        Event.campaign_id == campaign_id,
        Event.event_type == "credential_submitted"
    ).count()

    return {
        "campaign_id": campaign_id,
        "campaign_name": campaign.name,
        "campaign_status": campaign.status,
        "total_participants": total_participants,
        "total_events": total_events,
        "emails_opened": emails_opened,
        "links_clicked": links_clicked,
        "credentials_submitted": credentials_submitted
    }


@router.get("/{campaign_id}/report")
def get_campaign_report(
    campaign_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_role("admin"))
):
    campaign = db.query(Campaign).filter(
        Campaign.id == campaign_id
    ).first()

    if not campaign:
        raise HTTPException(
            status_code=404,
            detail="Campaign not found"
        )

    total_participants = db.query(Participant).filter(
        Participant.campaign_id == campaign_id
    ).count()

    links_clicked = db.query(Event).filter(
        Event.campaign_id == campaign_id,
        Event.event_type == "link_clicked"
    ).count()

    credentials_submitted = db.query(Event).filter(
        Event.campaign_id == campaign_id,
        Event.event_type == "credential_submitted"
    ).count()

    if total_participants > 0:
        click_rate = round(
            (links_clicked / total_participants) * 100,
            2
        )

        credential_submission_rate = round(
            (credentials_submitted / total_participants) * 100,
            2
        )
    else:
        click_rate = 0
        credential_submission_rate = 0

    return {
        "campaign_id": campaign.id,
        "campaign_name": campaign.name,
        "campaign_status": campaign.status,
        "total_participants": total_participants,
        "links_clicked": links_clicked,
        "credentials_submitted": credentials_submitted,
        "click_rate_percent": click_rate,
        "credential_submission_rate_percent": credential_submission_rate
    }


@router.get("/{campaign_id}/dashboard")
def get_campaign_dashboard(
    campaign_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_role("admin"))
):
    campaign = db.query(Campaign).filter(
        Campaign.id == campaign_id
    ).first()

    if not campaign:
        raise HTTPException(
            status_code=404,
            detail="Campaign not found"
        )

    participants = db.query(Participant).filter(
        Participant.campaign_id == campaign_id
    ).all()

    total_participants = len(participants)

    total_events = db.query(Event).filter(
        Event.campaign_id == campaign_id
    ).count()

    emails_opened = db.query(Event).filter(
        Event.campaign_id == campaign_id,
        Event.event_type == "email_opened"
    ).count()

    links_clicked = db.query(Event).filter(
        Event.campaign_id == campaign_id,
        Event.event_type == "link_clicked"
    ).count()

    credentials_submitted = db.query(Event).filter(
        Event.campaign_id == campaign_id,
        Event.event_type == "credential_submitted"
    ).count()

    participant_results = []

    for participant in participants:
        events = db.query(Event).filter(
            Event.participant_id == participant.id,
            Event.campaign_id == campaign_id
        ).all()

        score = 0

        for event in events:
            if event.event_type == "email_opened":
                score += 10

            elif event.event_type == "link_clicked":
                score += 30

            elif event.event_type == "credential_submitted":
                score += 60

        if score >= 60:
            risk_level = "high"

        elif score >= 30:
            risk_level = "medium"

        elif score > 0:
            risk_level = "low"

        else:
            risk_level = "no_risky_interaction"

        participant_results.append({
            "participant_id": participant.id,
            "identifier": participant.identifier,
            "risk_score": score,
            "risk_level": risk_level,
            "events_recorded": len(events)
        })

    return {
        "campaign": {
            "id": campaign.id,
            "name": campaign.name,
            "description": campaign.description,
            "status": campaign.status
        },
        "summary": {
            "total_participants": total_participants,
            "total_events": total_events,
            "emails_opened": emails_opened,
            "links_clicked": links_clicked,
            "credentials_submitted": credentials_submitted
        },
        "participants": participant_results
    }