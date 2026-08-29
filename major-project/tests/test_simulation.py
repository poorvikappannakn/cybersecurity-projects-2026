from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from backend.database.connection import Base
from backend.main import app
from backend.api.simulation import get_db
from backend.models.campaign import Campaign
from backend.models.participant import Participant
from backend.models.event import Event


TEST_DATABASE_URL = "sqlite://"

engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


def override_get_db():
    db = TestingSessionLocal()

    try:
        yield db

    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def setup_campaign_and_participant(
    campaign_status="active"
):
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()

    campaign = Campaign(
        name="Test Campaign",
        description="Automated simulation test",
        status=campaign_status
    )

    db.add(campaign)
    db.commit()
    db.refresh(campaign)

    participant = Participant(
        campaign_id=campaign.id,
        identifier="test-participant"
    )

    db.add(participant)
    db.commit()
    db.refresh(participant)

    campaign_id = campaign.id
    participant_id = participant.id

    db.close()

    return campaign_id, participant_id


def test_simulation_email_records_email_open():
    campaign_id, participant_id = setup_campaign_and_participant()

    response = client.get(
        f"/api/simulation/email/{campaign_id}/{participant_id}"
    )

    assert response.status_code == 200
    assert "Simulation Email" in response.text

    db = TestingSessionLocal()

    event = db.query(Event).filter(
        Event.campaign_id == campaign_id,
        Event.participant_id == participant_id,
        Event.event_type == "email_opened"
    ).first()

    db.close()

    assert event is not None


def test_simulation_landing_records_link_click():
    campaign_id, participant_id = setup_campaign_and_participant()

    response = client.get(
        f"/api/simulation/landing/{campaign_id}/{participant_id}"
    )

    assert response.status_code == 200
    assert "Security Awareness Simulation" in response.text

    db = TestingSessionLocal()

    event = db.query(Event).filter(
        Event.campaign_id == campaign_id,
        Event.participant_id == participant_id,
        Event.event_type == "link_clicked"
    ).first()

    db.close()

    assert event is not None


def test_completed_campaign_cannot_run_simulation():
    campaign_id, participant_id = setup_campaign_and_participant(
        campaign_status="completed"
    )

    response = client.get(
        f"/api/simulation/email/{campaign_id}/{participant_id}"
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Campaign is not active"


def test_participant_from_wrong_campaign_is_rejected():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()

    campaign_one = Campaign(
        name="Campaign One",
        description="First campaign",
        status="active"
    )

    campaign_two = Campaign(
        name="Campaign Two",
        description="Second campaign",
        status="active"
    )

    db.add_all([
        campaign_one,
        campaign_two
    ])

    db.commit()

    db.refresh(campaign_one)
    db.refresh(campaign_two)

    participant = Participant(
        campaign_id=campaign_one.id,
        identifier="participant-one"
    )

    db.add(participant)
    db.commit()
    db.refresh(participant)

    campaign_two_id = campaign_two.id
    participant_id = participant.id

    db.close()

    response = client.get(
        f"/api/simulation/email/{campaign_two_id}/{participant_id}"
    )

    assert response.status_code == 400
    assert response.json()["detail"] == (
        "Participant does not belong to this campaign"
    )