from typing import List, Union
from enum import Enum
from pydantic import BaseModel, validator


class User(BaseModel):
    id: int  # uuid.UUID
    email: str  # TODO: EmailStr (install pydantic[email], then "from pydantic import EmailStr")
    username: str
    # tasks: List[Task] = []
