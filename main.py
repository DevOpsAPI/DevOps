from fastapi import FastAPI, HTTPException

app = FastAPI()

# Voorbeeld van een database als een lijst
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
