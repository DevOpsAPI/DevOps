# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel

# app = FastAPI()

# games_db = {
#     1: {"id": 1, "title": "The Witcher 3", "genre": "RPG"},
#     2: {"id": 2, "title": "Red Dead Redemption 2", "genre": "Action-Adventure"},
#     3: {"id": 3, "title": "Call off Duty black ops 2", "genre": "First person shooter- third person shooting"}, # heb Orhan erbij gezet
#     4: {"id": 4, "title": "Call off Duty black ops 3", "genre": "First person shooter- third person shooting"} # heb Orhan erbij gezet 
# }

# class Game(BaseModel):
#     title: str
#     genre: str

# @app.get("/games/")
# async def get_games():
#     return games_db 

# @app.get("/games/{game_id}")
# async def get_game(game_id: int):
#     return games_db.get(game_id)

# @app.post("/games/")
# async def create_game(game: Game):
#     game_id = max(games_db.keys()) + 1
#     games_db[game_id] = game.dict()
#     return {"game_id": game_id, **game.dict()}

# @app.put("/games/{game_id}")
# async def update_game(game_id: int, game: Game):
#     if game_id not in games_db:
#         return {"error": "Game not found"}
#     games_db[game_id] = game.dict()
#     return games_db[game_id]

# @app.delete("/games/{game_id}")
# async def delete_game(game_id: int):
#     if game_id not in games_db:
#         return {"error": "Game not found"}
#     deleted_game = games_db.pop(game_id)
#     return deleted_game

# # Voorbeeld van een database als eenpip lijst
# users_db = []


# # Model voor gebruikersgegevens
# class User:
#     def __init__(self, username: str, email: str):
#         self.username = username
#         self.email = email


# # Endpoint om een nieuwe gebruiker toe te voegen
# @app.post("/users/")
# def create_user(username: str, email: str):
#     new_user = User(username=username, email=email)
#     users_db.append(new_user)
#     return new_user


# # Endpoint om een specifieke gebruiker op te halen
# @app.get("/users/{user_id}")
# def read_user(user_id: int):
#     if user_id < 0 or user_id >= len(users_db):
#         raise HTTPException(status_code=404, detail="Gebruiker niet gevonden")
#     return users_db[user_id]


# # Endpoint om alle gebruikers op te halen
# @app.get("/users/")
# def read_users(skip: int = 0, limit: int = 10):
#     return users_db[skip : skip + limit]

# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel

# app = FastAPI()

# games_db = {
#     1: {"id": 1, "title": "The Witcher 3", "genre": "RPG", "reviews": ["Great game!", "Best RPG ever!"]},
#     2: {"id": 2, "title": "Red Dead Redemption 2", "genre": "Action-Adventure", "reviews": ["Amazing graphics!", "Open world masterpiece!"]},
#     3: {"id": 3, "title": "Call of Duty: Black Ops 2", "genre": "First person shooter", "reviews": ["Addictive multiplayer!", "Great campaign!"]},
#     4: {"id": 4, "title": "Call of Duty: Black Ops 3", "genre": "First person shooter", "reviews": ["Zombies mode is awesome!", "Great graphics!"]}
# }

# class Game(BaseModel):
#     title: str
#     genre: str

# class Review(BaseModel):
#     review: str

# @app.get("/games/")
# async def get_games():
#     return games_db 

# @app.get("/games/{game_id}")
# async def get_game(game_id: int):
#     return games_db.get(game_id)

# @app.post("/games/")
# async def create_game(game: Game):
#     game_id = max(games_db.keys()) + 1
#     games_db[game_id] = game.dict()
#     return {"game_id": game_id, **game.dict()}

# @app.put("/games/{game_id}")
# async def update_game(game_id: int, game: Game):
#     if game_id not in games_db:
#         return {"error": "Game not found"}
#     games_db[game_id] = game.dict()
#     return games_db[game_id]

# @app.delete("/games/{game_id}")
# async def delete_game(game_id: int):
#     if game_id not in games_db:
#         return {"error": "Game not found"}
#     deleted_game = games_db.pop(game_id)
#     return deleted_game

# # Endpoint om reviews op te halen voor een specifiek spel
# @app.get("/games/{game_title}/reviews/")
# async def get_game_reviews(game_title: str):
#     for game_id, game in games_db.items():
#         if game['title'] == game_title:
#             return {"reviews": game.get('reviews', [])}
#     raise HTTPException(status_code=404, detail="Spel niet gevonden")

# # Voorbeeld van een database als een lege lijst
# users_db = []

# # Model voor gebruikersgegevens
# class User(BaseModel):
#     username: str
#     email: str

# # Endpoint om een nieuwe gebruiker toe te voegen
# @app.post("/users/")
# async def create_user(user: User):
#     users_db.append(user)
#     return user

# # Endpoint om een specifieke gebruiker op te halen
# @app.get("/users/{user_id}")
# async def read_user(user_id: int):
#     if user_id < 0 or user_id >= len(users_db):
#         raise HTTPException(status_code=404, detail="Gebruiker niet gevonden")
#     return users_db[user_id]

# # Endpoint om alle gebruikers op te halen
# @app.get("/users/")
# async def read_users(skip: int = 0, limit: int = 10):
#     return users_db[skip : skip + limit]


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

games_db = {
    1: {"id": 1, "title": "The Witcher 3", "genre": "RPG", "reviews": ["Great game!", "Best RPG ever!"]},
    2: {"id": 2, "title": "Red Dead Redemption 2", "genre": "Action-Adventure", "reviews": ["Amazing graphics!", "Open world masterpiece!"]},
    3: {"id": 3, "title": "Call of Duty: Black Ops 2", "genre": "First person shooter", "reviews": ["Addictive multiplayer!", "Great campaign!"]},
    4: {"id": 4, "title": "Call of Duty: Black Ops 3", "genre": "First person shooter", "reviews": ["Zombies mode is awesome!", "Great graphics!"]}
}

class Game(BaseModel):
    id: int  # Verandering: toevoegen van id
    title: str
    genre: str

class Review(BaseModel):
    review: str

@app.get("/games/")
async def get_games():
    return games_db 

@app.get("/games/{game_id}")
async def get_game(game_id: int):
    return games_db.get(game_id)

@app.post("/games/")
async def create_game(game: Game):
    game_id = max(games_db.keys()) + 1
    game_data = game.dict()
    game_data["id"] = game_id  # Verandering: toevoegen van id aan de game data
    games_db[game_id] = game_data
    return {"game_id": game_id, **game_data}

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

@app.get("/games/{game_id}/reviews/")  
async def get_game_reviews(game_id: int):  
    game = games_db.get(game_id)
    if game:
        return {"title": game["title"], "reviews": game.get('reviews', [])}
    else:
        raise HTTPException(status_code=404, detail="Spel niet gevonden")

users_db = []

# Model voor gebruikersgegevens
class User(BaseModel):
    username: str
    email: str

# Endpoint om een nieuwe gebruiker toe te voegen
@app.post("/users/")
async def create_user(user: User):
    users_db.append(user)
    return user

# Endpoint om een specifieke gebruiker op te halen
@app.get("/users/{user_id}")
async def read_user(user_id: int):
    if user_id < 0 or user_id >= len(users_db):
        raise HTTPException(status_code=404, detail="Gebruiker niet gevonden")
    return users_db[user_id]

# Endpoint om alle gebruikers op te halen
@app.get("/users/")
async def read_users(skip: int = 0, limit: int = 10):
    return users_db[skip : skip + limit]
