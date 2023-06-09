from typing import List, Union
from pydantic import BaseModel, validator


class Salary(BaseModel):
    id: int  # uuid.UUID
    email: str  # TODO: EmailStr (install pydantic[email], then "from pydantic import EmailStr")
