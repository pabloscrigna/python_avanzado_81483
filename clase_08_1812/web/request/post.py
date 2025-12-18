import requests


data = {
    "postId": 4,
    "name": "pablo edu it",
    "email": "pablo@mail.com",
    "body": "Comentario de prueba por requests"
}

url = "https://jsonplaceholder.typicode.com/comments"

headers = {
    "Content-type" : "application/json"
}

response = requests.post(url=url, json=data, headers=headers)


print("response data: ", response.json())
print("status code:", response.status_code)