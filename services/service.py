from database.database import DB as data
from schemas.user_schema import User

import os
class Service:
    def get_users(self) -> list[User]:
        items = []
        cwd = os.getcwd()
        print(cwd)
        for item in data.data.values():
            items.append(
                User(
                    id=item['id'],
                    email=item['email'],
                    username=item['username']
                )
            )
        return items

service = Service()
