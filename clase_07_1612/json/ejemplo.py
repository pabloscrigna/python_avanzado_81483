import json

data = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "notas": [ 9, 7, 89],
    "estado": True,
    "est_civil": None
}

data_json = json.dumps(data, indent=4)

print("data dict: ", data)
print("data json:", data_json)


print(type(data))
print(type(data_json))
