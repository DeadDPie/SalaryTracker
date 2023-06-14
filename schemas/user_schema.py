import uuid
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: uuid.UUID
    email: EmailStr
    username: str
