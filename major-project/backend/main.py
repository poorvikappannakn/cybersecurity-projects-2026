from fastapi import FastAPI
from backend.api.health import router as health_router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Phishing Awareness Simulation API"}

app.include_router(health_router)