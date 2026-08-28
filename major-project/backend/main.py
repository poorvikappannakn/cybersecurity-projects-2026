from fastapi import FastAPI
from backend.models.participant import Participant
from backend.models.event import Event
from backend.models.user import User

from backend.api.health import router as health_router
from backend.database.connection import Base, engine
from backend.models.campaign import Campaign
from backend.api.auth import router as auth_router
from backend.api.campaigns import router as campaigns_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth_router)
app.include_router(campaigns_router)
@app.get("/")
def home():
    return {"message": "Phishing Awareness Simulation API"}

app.include_router(health_router)