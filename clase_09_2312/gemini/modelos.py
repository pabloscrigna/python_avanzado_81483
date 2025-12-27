from google import genai


API_KEY = "AIzaSyCvoL_0jWoEwocyFI4V9p0z7Hi7STdBHdo"


client = genai.Client(api_key=API_KEY)

modelos = client.models.list()

for modelo in modelos:
    print(modelo.name)