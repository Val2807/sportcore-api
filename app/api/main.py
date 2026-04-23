from datetime import date

from fastapi import FastAPI
from fastapi import HTTPException

from app.api.schemas import PlayerCreate
from app.db import SessionLocal

from app.services.player_service import create_player, get_all_players, get_player_by_id, serialize_player


app = FastAPI()


@app.get("/")
def root():
    return {"message": "SportCore API is running"}


@app.get("/players")
def get_players():
    session = SessionLocal()
    players = get_all_players(session)
    return players


@app.post("/players")
def create_player_endpoint(player: PlayerCreate):
    session = SessionLocal()

    new_player = create_player(
        session=session,
        first_name=player.first_name,
        last_name=player.last_name,
        birth_date=date.fromisoformat(player.birth_date),
        team_id=player.team_id,
        position=player.position,
        weight=player.weight,
    )

    return {
        "id": new_player.id,
        "first_name": new_player.first_name,
        "last_name": new_player.last_name,
        "birth_date": str(new_player.birth_date),
        "team_id": new_player.team_id,
        "position": new_player.position,
        "weight": new_player.weight,
    }


@app.get("/players/{player_id}")
def get_player_by_id_endpoint(player_id: int):
    session = SessionLocal()
    found_player_by_id = get_player_by_id(session, player_id)
    if not found_player_by_id:
        raise HTTPException(status_code=404, detail="Player not found")
    return serialize_player(found_player_by_id)
