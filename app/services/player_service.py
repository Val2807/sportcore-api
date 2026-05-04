from datetime import date
from sqlalchemy.orm import Session

from app.models.player import Player


def get_player_by_identity_fields(
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
    existing = get_player_by_identity_fields(
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


def serialize_player(player: Player) -> dict:
    return {
        "id": player.id,
        "first_name": player.first_name,
        "last_name": player.last_name,
        "birth_date": str(player.birth_date),
        "team_id": player.team_id,
        "weight": player.weight,
        "position": player.position
    }


def get_all_players(session: Session):
    players = session.query(Player).all()
    return [serialize_player(player) for player in players]


def get_player_by_id(
    session: Session,
    player_id: int
):
    return session.query(Player).filter(Player.id == player_id).first()


def update_player_weight_by_id(
        session: Session,
        player_id: int,
        weight: float,
):
    player = get_player_by_id(session, player_id)
    if not player:
        return None

    player.weight = weight
    session.commit()

    return player


def delete_player_by_id(session, player_id):
    player = get_player_by_id(session, player_id)
    if not player:
        return None

    session.delete(player)
    session.commit()
    return player
