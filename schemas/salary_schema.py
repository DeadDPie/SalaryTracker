from typing import List, Union
from pydantic import BaseModel, validator, constr


class Salary(BaseModel):
    salary: str
    salary_rise_date: constr(regex=r'^[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]$') = "2023-09-22"
