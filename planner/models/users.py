from beanie import Document
from typing import Optional, List
from pydantic import BaseModel, EmailStr
from models.events import Event

class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Event]]

    class Settings:
        name = "users"

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "events": []
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str