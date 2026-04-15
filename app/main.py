from datetime import date

from app.db import engine, Base, SessionLocal
from app.models.player import Player


Base.metadata.create_all(bind=engine)

session = SessionLocal()

existing_player = (
    session.query(Player)
    .filter_by(
        first_name="Ivan",
        last_name="Petrov",
        birth_date=date(2010, 5, 1),
        team_id=1
    )
    .first()
)

players = session.query(Player).all()
for player in players:
    print(player.first_name, player.last_name)


if existing_player:
    print("Player already exists")
else:
    new_player = Player(
        first_name="Ivan",
        last_name="Petrov",
        birth_date=date(2010, 5, 1),
        team_id=1, 
        weight=42.5
    )

    session.add(new_player)
    session.commit()
    print("Player saved successfully")


if existing_player:
    session.delete(existing_player)
    session.commit()
    print("Player deleted")
