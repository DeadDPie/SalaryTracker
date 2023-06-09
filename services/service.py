from fastapi import HTTPException
import jwt
import json

class Service:
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

    def get_salary():
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing', 'authenticated': False}), 401

        try:
            # Проверка токена и извлечение имени пользователя
            data = jwt.decode(token.split()[1], app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = data['sub']
        except:
            return jsonify({'message': 'Token is invalid', 'authenticated': False}), 401

        # Получение информации о заработной плате и следующем повышении
        salary_info = {
            'current_salary': 50000,
            'next_promotion': '2024-01-01'
        }

        return jsonify({'salary_info': salary_info, 'authenticated': True})
