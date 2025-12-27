import requests

datos = {
    "name": "desde request",
    "email": "prueba@mail.com",
    "message" : "prueba"
}


url = "localhost:8880/form"
resultado  = requests.post("localhost:8880/form", data=datos)

print(resultado.status_code)