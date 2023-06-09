import json

class DB:
    with open("D:\\PycharmProjects\\SalaryTracker\\database\\fake_db.json") as f:
        data = json.load(f)
