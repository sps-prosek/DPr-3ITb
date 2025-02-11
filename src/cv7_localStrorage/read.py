import json

F_NAME = "config.json"

try:
    with open(F_NAME, "r") as f:
        cnf = json.load(f)
except OSError:
    cnf = {}

print(cnf)
