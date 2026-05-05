from fastapi import FastAPI

from app.api.routers import players


app = FastAPI()

app.include_router(players.router)


@app.get("/")
def root():
    return {"message": "SportCore API is running"}
