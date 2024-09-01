from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
from fastapi.params import Body
from random import randrange

app = FastAPI()

class AccountCreating(BaseModel):
    firstname: str
    lastname: str
    age: int
    email: str
    address: str
    regNum: int



# Creating a unique reg number
reg = randrange(0, 100)
# storing users
users = [{"firstname": "Tony", "lastname": "Chi", "age": 21, "email": "pentesting2022@gmail.com", "location": "Ohio", "regnumber": reg, "id": 1},{"name": "Chuks", "age": 11, "location": "Alaska", "regnumber": reg, "id": 2}]

# looping through users to get ID
def get_user_id(id):
    for user in users:
        if user["id"] == id:
            return user

@app.get("/")
def home():
    return {"task": "Anniversary"}


# Post New Users to database



@app.get("/item/{id}")
def get_users(id: int):
    user_id = get_user_id(id)
    print(user_id)
    print(reg)
    return {"User No": user_id}