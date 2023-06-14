from datetime import date
from pydantic import BaseModel

class Salary(BaseModel):
    salary: str
    salary_rise_date: date #"2023-09-22"
