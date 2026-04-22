from app.services.player_service import get_all_players
from app.db import SessionLocal
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "SportCore API is running"}


@app.get("/players")
def get_players():
    session = SessionLocal()
    players = get_all_players(session)
    return players
