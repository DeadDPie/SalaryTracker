import uuid
from typing import List, Union
from pydantic import BaseModel, validator, EmailStr


class User(BaseModel):
    id: uuid.UUID
    email: EmailStr
    username: str
