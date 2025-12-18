import requests

id = "2"

url = "https://jsonplaceholder.typicode.com/comments"

url_id = f"{url}/{id}"

print("url: ", url_id)

response = requests.delete(url=url_id)

datos = response.json()

print("datos: ", datos)
print("status code: ", response.status_code)