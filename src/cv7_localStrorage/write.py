import json

F_NAME = "config.json"

cnf = {"num1": 20, "num2": 50}

with open(F_NAME, "w") as f:
    f.write(json.dumps(cnf))
