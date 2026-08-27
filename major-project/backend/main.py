from fastapi import FastAPI
from backend.models.participant import Participant
from backend.models.event import Event
from backend.models.user import User

from backend.api.health import router as health_router
from backend.database.connection import Base, engine
from backend.models.campaign import Campaign

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Phishing Awareness Simulation API"}

app.include_router(health_router)