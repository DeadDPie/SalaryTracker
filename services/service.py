from database.database import DB as data
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

service = Service()
