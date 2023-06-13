from typing import Optional
from fastapi import FastAPI, Depends, HTTPException
from database.database import DB as data
from schemas import Salary
from schemas.user_schema import User


class Service:

    def get_users(self) -> list[User]:
        items = []
        for item in data.data.values():
            items.append(
                User(
                    id=item['id'],
                    email=item['email'],
                    username=item['username']
                )
            )
        return items

    def get_salary(self) -> list[User]:
        items = []
        for item in data.data.values():
            items.append(
                Salary(
                    salary=item['salary'],
                    salary_rise_date=item['salary_rise_date'],
                )
            )
        return items


service = Service()
