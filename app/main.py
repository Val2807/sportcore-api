from datetime import date
from app.db import engine, Base, SessionLocal
from app.services.player_service import create_player, get_player, delete_player


Base.metadata.create_all(bind=engine)

session = SessionLocal()

first_name = "Ivan"
last_name = "Ivanov"
birth_date = date(2008, 5, 1)
team_id = 1
position = "forward"
weight: 50.4

player = create_player(session, first_name, last_name,
                       birth_date, team_id, position, weight)

if player:
    print(f"Player {player.first_name} {player.last_name} was created")

found_player = get_player(session, first_name, last_name, birth_date, team_id,)

if found_player:
    print(
        f"Player {found_player.first_name} {found_player.last_name} was founded")
else:
    print("Player not found")

deleted_player = delete_player(
    session, first_name, last_name, birth_date, team_id,)


if player:
    print(
        f"Player {deleted_player.first_name} {deleted_player.last_name} was deleted")
else:
    print("Player not found")
