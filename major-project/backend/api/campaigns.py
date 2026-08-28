from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.database.connection import SessionLocal
from backend.models.campaign import Campaign
from backend.services.rbac import require_role
from backend.services.security import get_current_user


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

    allowed_statuses = {"draft", "active", "completed"}

    if request.status not in allowed_statuses:
        raise HTTPException(
            status_code=400,
            detail="Invalid campaign status"
        )

    campaign.status = request.status
    db.commit()
    db.refresh(campaign)

    return {
        "message": "Campaign status updated",
        "campaign_id": campaign.id,
        "status": campaign.status
    }