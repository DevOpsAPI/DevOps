from fastapi import FastAPI, HTTPException

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

# Voorbeeld van een database als eenpip lijst
users_db = []


# Model voor gebruikersgegevens
class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email


# Endpoint om een nieuwe gebruiker toe te voegen
@app.post("/users/")
def create_user(username: str, email: str):
    new_user = User(username=username, email=email)
    users_db.append(new_user)
    return new_user


# Endpoint om een specifieke gebruiker op te halen
@app.get("/users/{user_id}")
def read_user(user_id: int):
    if user_id < 0 or user_id >= len(users_db):
        raise HTTPException(status_code=404, detail="Gebruiker niet gevonden")
    return users_db[user_id]


# Endpoint om alle gebruikers op te halen
@app.get("/users/")
def read_users(skip: int = 0, limit: int = 10):
    return users_db[skip : skip + limit]

