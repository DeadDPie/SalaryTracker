import json
import os


class DB:
    cwd = os.getcwd()
    # cwd = cwd[:cwd.index("SalaryTracker")+13]
    # print(cwd)
    with open(cwd+"/database/fake_db.json") as f:
        data = json.load(f)
