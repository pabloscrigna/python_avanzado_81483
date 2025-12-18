import requests

data = {
    "postId": 4,
    "name": "pablo edu it",
    "email": "pablo@mail.com",
    "body": "Comentario de prueba por requests"
}

id = "1"

url = "https://jsonplaceholder.typicode.com/comments"

url_id = f"{url}/{id}"

headers = {
    "Content-type" : "application/json"
}

response = requests.put(url=url_id, json=data, headers=headers)


print("response data: ", response.json())
print("status code:", response.status_code)