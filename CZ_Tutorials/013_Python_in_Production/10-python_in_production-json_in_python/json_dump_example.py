import json

file_path = "C:/Users/syurskyi/PycharmProjects/TD/__syurskyi_repository__/maya/tutorials/Maya_Programming/CZ_Tutorials/013_Python in Production/10-python_in_production-json_in_python/data.json"

data = {
    "assetId": 25,
    "assetName": "Lighthouse",
    "assetCode": "zur_lighthouse",
    "projectId": 1,
    "dependencies": [
        3,
        4,
        5
    ],
    "metadata": {
        "creator": "Serhii Yurskyi",
        "created": "2020/01/01",
        "modified": "2020/02/02"
    }
}

with open(file_path, "w") as file_for_write:
    json.dump(data, file_for_write, indent=4, sort_keys=True)

# json_string = json.dumps(data)
# print(json_string)
# print(type(json_string))

# data_from_json = json.loads(json_string)
# print(data_from_json)
# print(type(data_from_json))
