from typing import Optional
from fastapi import FastAPI, Depends, HTTPException
from datetime import datetime, timedelta
import jwt
import json
from fastapi.responses import JSONResponse
from database.database import DB as data
from schemas.user_schema import User

SECRET_KEY = "wow3man3i3love3dancing5and2eating8also9i8am3keen7on8cats"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class Service:

    def get_users(self) -> list[User]:
        items = []
        for item in data.data:
            items.append(
                User(
                    id=item['id'],
                    email=item['email'],
                    username=item['username']
                )
            )
        return items

service = Service()