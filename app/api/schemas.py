from pydantic import BaseModel


class PlayerCreate(BaseModel):
    first_name: str
    last_name: str
    birth_date: str
    team_id: int
    weight: float | None = None
    position: str | None = None


class PlayerWeightUpdate(BaseModel):
    weight: float


class PlayerResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    birth_date: str
    team_id: int
    weight: float | None = None
    position: str | None = None
