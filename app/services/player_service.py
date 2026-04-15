from datetime import date
from sqlalchemy.orm import Session

from app.models.player import Player


def get_player(
    session: Session,
    first_name: str,
    last_name: str,
    birth_date: date,
    team_id: int,
):
    return (
        session.query(Player)
        .filter_by(
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            team_id=team_id,
        )
        .first()
    )


def create_player(
        session: Session,
        first_name: str,
        last_name: str,
        birth_date: date,
        team_id: int,
        position: str | None = None,
        weight: float | None = None):
    existing = get_player(
        session=session,
        first_name=first_name,
        last_name=last_name,
        birth_date=birth_date,
        team_id=team_id,
    )

    if existing:
        return existing
    else:
        new_player = Player(
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            team_id=team_id,
            weight=weight,
            position=position
        )
        session.add(new_player)
        session.commit()

        return new_player


def delete_player():
    pass
