import json

class DB:
    with open("..\\SalaryTracker\\database\\fake_db.json") as f:
        data = json.load(f)
