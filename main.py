from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

games_db = {
    1: {"id": 1, "title": "The Witcher 3", "genre": "RPG"},
    2: {"id": 2, "title": "Red Dead Redemption 2", "genre": "Action-Adventure"},
}

class Game(BaseModel):
    title: str
    genre: str

@app.get("/games/")
async def get_games():
    return games_db

@app.get("/games/{game_id}")
async def get_game(game_id: int):
    return games_db.get(game_id)

@app.post("/games/")
async def create_game(game: Game):
    game_id = max(games_db.keys()) + 1
    games_db[game_id] = game.dict()
    return {"game_id": game_id, **game.dict()}

@app.put("/games/{game_id}")
async def update_game(game_id: int, game: Game):
    if game_id not in games_db:
        return {"error": "Game not found"}
    games_db[game_id] = game.dict()
    return games_db[game_id]

@app.delete("/games/{game_id}")
async def delete_game(game_id: int):
    if game_id not in games_db:
        return {"error": "Game not found"}
    deleted_game = games_db.pop(game_id)
    return deleted_game
