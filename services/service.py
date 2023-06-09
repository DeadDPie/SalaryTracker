from typing import Optional
from fastapi import FastAPI, Depends, HTTPException
from datetime import datetime, timedelta
from jose import JWTError, jwt
import jwt
import json

SECRET_KEY = "wow3man3i3love3dancing5and2eating8also9i8am3keen7on8cats"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class Service:


    # Функция для создания JWT-токена
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    # Функция для проверки JWT-токена
    def decode_access_token(token: str):
        try:
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username = decoded_token.get("sub")
            if username is None:
                raise HTTPException(status_code=401, detail="Invalid token")
            return username
        except JWTError:
            raise HTTPException(status_code=401, detail="Invalid token")

    def read_salary_info(token: str = Depends(decode_access_token)):
        if token in fake_salary_db:
            salary_info = fake_salary_db[token]
            return SalaryInfo(salary_info["salary"], salary_info["next_increase_date"].strftime("%Y-%m-%d"))
        else:
            raise HTTPException(status_code=404, detail="Salary info not found")

        # Простая функция для проверки имени пользователя и пароля
        def authenticate(self, username, password):
            if username in users and users[username] == password:
                return True
            return False

        def login(self):
            auth = request.authorization
            if not auth or not authenticate(auth.username, auth.password):
                return jsonify({'message': 'Invalid credentials', 'authenticated': False}), 401

            # Издание токена с ограниченным временем действия
            token = jwt.encode({'sub': auth.username, 'exp': datetime.utcnow() + timedelta(minutes=30)},
                               app.config['SECRET_KEY'])

            return jsonify({'token': token.decode('UTF-8')})