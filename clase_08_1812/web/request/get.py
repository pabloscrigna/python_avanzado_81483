import requests

url = "https://jsonplaceholder.typicode.com/comments"


response = requests.get(url=url)

datos = response.json()

print("datos: ", datos[0])
print("status code: ", response.status_code)



