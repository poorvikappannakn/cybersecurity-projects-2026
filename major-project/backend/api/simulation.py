from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from backend.database.connection import SessionLocal
from backend.models.campaign import Campaign
from backend.models.participant import Participant
from backend.models.event import Event


router = APIRouter(
    prefix="/api/simulation",
    tags=["Simulation"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def validate_simulation(
    campaign_id: int,
    participant_id: int,
    db: Session
):
    campaign = db.query(Campaign).filter(
        Campaign.id == campaign_id
    ).first()

    if not campaign:
        raise HTTPException(
            status_code=404,
            detail="Campaign not found"
        )

    participant = db.query(Participant).filter(
        Participant.id == participant_id
    ).first()

    if not participant:
        raise HTTPException(
            status_code=404,
            detail="Participant not found"
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

    return campaign, participant


@router.get("/click/{campaign_id}/{participant_id}")
def simulate_link_click(
    campaign_id: int,
    participant_id: int,
    db: Session = Depends(get_db)
):
    campaign, participant = validate_simulation(
        campaign_id,
        participant_id,
        db
    )

    existing_event = db.query(Event).filter(
        Event.participant_id == participant.id,
        Event.campaign_id == campaign.id,
        Event.event_type == "link_clicked"
    ).first()

    if existing_event:
        return {
            "message": "Simulation interaction already recorded",
            "event_id": existing_event.id,
            "participant_id": participant.id,
            "campaign_id": campaign.id,
            "event_type": existing_event.event_type
        }

    event = Event(
        participant_id=participant.id,
        campaign_id=campaign.id,
        event_type="link_clicked"
    )

    db.add(event)
    db.commit()
    db.refresh(event)

    return {
        "message": "Simulation interaction recorded",
        "event_id": event.id,
        "participant_id": participant.id,
        "campaign_id": campaign.id,
        "event_type": event.event_type
    }


@router.get(
    "/landing/{campaign_id}/{participant_id}",
    response_class=HTMLResponse
)
def simulation_landing_page(
    campaign_id: int,
    participant_id: int,
    db: Session = Depends(get_db)
):
    campaign, participant = validate_simulation(
        campaign_id,
        participant_id,
        db
    )

    existing_event = db.query(Event).filter(
        Event.participant_id == participant.id,
        Event.campaign_id == campaign.id,
        Event.event_type == "link_clicked"
    ).first()

    if not existing_event:
        event = Event(
            participant_id=participant.id,
            campaign_id=campaign.id,
            event_type="link_clicked"
        )

        db.add(event)
        db.commit()

    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Security Awareness Simulation</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f7fb;
                margin: 0;
                padding: 0;
            }

            .container {
                max-width: 700px;
                margin: 80px auto;
                background: white;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
                text-align: center;
            }

            .warning {
                font-size: 48px;
                margin-bottom: 20px;
            }

            h1 {
                color: #222;
            }

            p {
                color: #555;
                font-size: 18px;
                line-height: 1.6;
            }

            .notice {
                margin-top: 30px;
                padding: 20px;
                background: #fff3cd;
                border-radius: 8px;
                color: #664d03;
            }

            .tips {
                text-align: left;
                margin-top: 30px;
            }

            .tips li {
                margin-bottom: 12px;
            }
        </style>
    </head>

    <body>

        <div class="container">

            <div class="warning">⚠️</div>

            <h1>Security Awareness Simulation</h1>

            <p>
                You have reached a simulated phishing-awareness page.
            </p>

            <div class="notice">
                <strong>This was a simulation.</strong>
                <br><br>
                No real credentials were requested or collected.
            </div>

            <div class="tips">
                <h2>Security Tips</h2>

                <ul>
                    <li>Check the sender before trusting an email.</li>
                    <li>Inspect links before clicking them.</li>
                    <li>Be cautious with urgent requests.</li>
                    <li>Never provide passwords through suspicious links.</li>
                    <li>Report suspicious messages to your organization.</li>
                </ul>
            </div>

            <p>
                This interaction has been recorded for the
                security-awareness assessment.
            </p>

        </div>

    </body>
    </html>
    """


@router.get(
    "/email/{campaign_id}/{participant_id}",
    response_class=HTMLResponse
)
def simulation_email(
    campaign_id: int,
    participant_id: int,
    db: Session = Depends(get_db)
):
    campaign, participant = validate_simulation(
        campaign_id,
        participant_id,
        db
    )

    existing_event = db.query(Event).filter(
        Event.participant_id == participant.id,
        Event.campaign_id == campaign.id,
        Event.event_type == "email_opened"
    ).first()

    if not existing_event:
        event = Event(
            participant_id=participant.id,
            campaign_id=campaign.id,
            event_type="email_opened"
        )

        db.add(event)
        db.commit()

    simulation_link = (
        f"/api/simulation/landing/"
        f"{campaign.id}/{participant.id}"
    )

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Simulation Email</title>

        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #eeeeee;
                margin: 0;
                padding: 40px;
            }}

            .email {{
                max-width: 650px;
                margin: auto;
                background: white;
                border: 1px solid #dddddd;
                border-radius: 8px;
                overflow: hidden;
            }}

            .header {{
                padding: 20px;
                border-bottom: 1px solid #dddddd;
            }}

            .content {{
                padding: 35px;
            }}

            .subject {{
                font-size: 22px;
                font-weight: bold;
                margin-bottom: 25px;
            }}

            .button {{
                display: inline-block;
                margin-top: 25px;
                padding: 14px 24px;
                background: #2563eb;
                color: white;
                text-decoration: none;
                border-radius: 6px;
            }}

            .footer {{
                padding: 20px;
                background: #f7f7f7;
                color: #777777;
                font-size: 13px;
            }}
        </style>
    </head>

    <body>

        <div class="email">

            <div class="header">
                <strong>Security Notification</strong>
            </div>

            <div class="content">

                <div class="subject">
                    Important Account Notification
                </div>

                <p>
                    Hello,
                </p>

                <p>
                    We noticed recent activity associated with your
                    account. Please review the activity using the
                    button below.
                </p>

                <a
                    class="button"
                    href="{simulation_link}"
                >
                    Review Account
                </a>

                <p style="margin-top: 30px;">
                    Please review this notification at your earliest
                    convenience.
                </p>

            </div>

            <div class="footer">
                This page is part of a controlled security-awareness
                simulation.
            </div>

        </div>

    </body>
    </html>
    """