from fastapi import FastAPI, Response, status, HTTPException
from typing import Union
from pydantic import BaseModel
from fastapi.params import Body
from random import randrange


app = FastAPI()

# Using Pydantic schema to creat our registeration model
class AccountCreating(BaseModel):
    firstname: str
    lastname: str
    age: int
    email: str
    address: str



# Creating a unique reg number
reg = randrange(0, 9999)

# storing users
users = [{"firstname": "Tony", "lastname": "Chi", "age": 21, "email": "pentesting2022@gmail.com", "location": "Ohio", "regnumber": reg, "id": 1},{"name": "Chuks", "age": 11, "location": "Alaska", "regnumber": reg, "id": 2}]

# looping through users to get ID
def get_user_id(id):
    for user in users:
        if user["id"] == id:
            return user
        

# Getting the user index
def user_index(id):
    for i, u in enumerate(users):
        if u["id"] == id:
            return i

@app.get("/")
def home():
    return {"task": "Anniversary"}


# Post New Users to database
@app.post("/user", status_code=status.HTTP_201_CREATED)
def signup(newuser: AccountCreating):
    list_user = newuser.model_dump()
    list_user["regNum"] = reg
    users.append(list_user)
    return {"Users": users}


# Getting a user by ID
@app.get("/user/{id}")
def get_users(id: int, response: Response):
    user_id = get_user_id(id)
    if not user_id: # If the ID doesn't exist
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User with id: {id} not found")
    print(user_id)
    return {"User No": user_id}


# Deleting a User
@app.delete("/user/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int):
    user_to_delete = user_index(id)
    if user_to_delete == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id: {id} not found or already deleted")
    users.pop(user_to_delete)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
