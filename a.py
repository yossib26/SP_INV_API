import json

with open("sample.json") as f:
    records = json.load(f)

for row in records:
    print(row)
