from fastapi import FastAPI, Response, status
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



# Creating a unique reg number
reg = randrange(0, 9999)

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
@app.post("/post")
def signup(newuser: AccountCreating):
    list_user = newuser.model_dump()
    list_user["regNum"] = reg
    users.append(list_user)
    return {"Users": users}



@app.get("/item/{id}")
def get_users(id: int, response: Response):
    user_id = get_user_id(id)
    if not user_id:
        response.status_code = status.HTTP_404_NOT_FOUND
        return "User Not Found"
    print(user_id)
    return {"User No": user_id}