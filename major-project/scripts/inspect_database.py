from backend.database.connection import SessionLocal
from backend.models.campaign import Campaign
from backend.models.participant import Participant
from backend.models.event import Event
from backend.models.audit_log import AuditLog


db = SessionLocal()


print("\n" + "=" * 70)
print("CAMPAIGNS")
print("=" * 70)
print(
    f"{'ID':<6}"
    f"{'NAME':<35}"
    f"{'STATUS':<15}"
)

for campaign in db.query(Campaign).all():
    print(
        f"{campaign.id:<6}"
        f"{campaign.name:<35}"
        f"{campaign.status:<15}"
    )


print("\n" + "=" * 70)
print("PARTICIPANTS")
print("=" * 70)
print(
    f"{'ID':<6}"
    f"{'CAMPAIGN ID':<14}"
    f"{'IDENTIFIER':<35}"
)

for participant in db.query(Participant).all():
    print(
        f"{participant.id:<6}"
        f"{participant.campaign_id:<14}"
        f"{participant.identifier:<35}"
    )


print("\n" + "=" * 70)
print("EVENTS")
print("=" * 70)
print(
    f"{'ID':<6}"
    f"{'CAMPAIGN ID':<14}"
    f"{'PARTICIPANT ID':<17}"
    f"{'EVENT TYPE':<25}"
)

for event in db.query(Event).all():
    print(
        f"{event.id:<6}"
        f"{event.campaign_id:<14}"
        f"{event.participant_id:<17}"
        f"{event.event_type:<25}"
    )


print("\n" + "=" * 70)
print("AUDIT LOGS")
print("=" * 70)
print(
    f"{'ID':<6}"
    f"{'USER ID':<10}"
    f"{'ACTION':<30}"
    f"{'DETAILS':<55}"
    f"{'TIMESTAMP'}"
)

for log in db.query(AuditLog).order_by(
    AuditLog.timestamp.desc()
).all():
    print(
        f"{log.id:<6}"
        f"{log.user_id:<10}"
        f"{log.action:<30}"
        f"{log.details:<55}"
        f"{log.timestamp}"
    )


db.close()