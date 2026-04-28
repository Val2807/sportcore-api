from datetime import date

from fastapi import FastAPI, Response, HTTPException, Depends


from app.api.schemas import PlayerCreate, PlayerWeightUpdate
from app.db import SessionLocal, get_db

from app.services.player_service import create_player, get_all_players, get_player_by_id, serialize_player, update_player_weight_by_id, delete_player_by_id

from sqlalchemy.orm import Session


app = FastAPI()


@app.get("/")
def root():
    return {"message": "SportCore API is running"}


@app.get("/players")
def get_players(db: Session = Depends(get_db)):
    players = get_all_players(db)
    return players


@app.post("/players")
def create_player_endpoint(player: PlayerCreate, db: Session = Depends(get_db)):

    new_player = create_player(
        session=db,
        first_name=player.first_name,
        last_name=player.last_name,
        birth_date=date.fromisoformat(player.birth_date),
        team_id=player.team_id,
        position=player.position,
        weight=player.weight,
    )

    return serialize_player(new_player)


@app.get("/players/{player_id}")
def get_player_by_id_endpoint(player_id: int, db: Session = Depends(get_db)):

    found_player_by_id = get_player_by_id(db, player_id)
    if not found_player_by_id:
        raise HTTPException(status_code=404, detail="Player not found")
    return serialize_player(found_player_by_id)


@app.patch("/players/{player_id}/weight")
def update_player_weight_endpoint(player_id: int, data: PlayerWeightUpdate, db: Session = Depends(get_db)):

    updated_player = update_player_weight_by_id(
        session=db,
        player_id=player_id,
        weight=data.weight,
    )

    if not updated_player:
        raise HTTPException(status_code=404, detail="Player not found")

    return serialize_player(updated_player)


@app.delete("/players/{player_id}")
def delete_player_by_id_endpoint(player_id: int, db: Session = Depends(get_db)):

    deleted_player = delete_player_by_id(
        session=db,
        player_id=player_id
    )
    if not deleted_player:
        raise HTTPException(status_code=404, detail="Player not found")
    return Response(status_code=204)
