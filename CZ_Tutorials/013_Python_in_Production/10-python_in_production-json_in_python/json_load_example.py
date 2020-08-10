import json

file_path = "C:/Users/syurskyi/PycharmProjects/TD/__syurskyi_repository__/maya/tutorials/Maya_Programming/CZ_Tutorials/013_Python in Production/10-python_in_production-json_in_python/data.json"

with open(file_path, "r") as file_for_read:
    data = json.load(file_for_read)

print(data)
