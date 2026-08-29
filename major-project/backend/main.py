from fastapi import FastAPI

from backend.database.connection import Base, engine

from backend.models.participant import Participant
from backend.models.event import Event
from backend.models.user import User
from backend.models.campaign import Campaign

from backend.api.health import router as health_router
from backend.api.auth import router as auth_router
from backend.api.campaigns import router as campaigns_router
from backend.api.participants import router as participants_router
from backend.api.events import router as events_router
from backend.api.simulation import router as simulation_router


Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(auth_router)
app.include_router(campaigns_router)
app.include_router(participants_router)
app.include_router(events_router)
app.include_router(simulation_router)
app.include_router(health_router)


@app.get("/")
def home():
    return {
        "message": "Phishing Awareness Simulation API"
    }
