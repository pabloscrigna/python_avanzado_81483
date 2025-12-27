from google import genai


API_KEY = "AIzaSyCvoL_0jWoEwocyFI4V9p0z7Hi7STdBHdo"

modelo = "models/gemini-flash-latest"

client = genai.Client(api_key=API_KEY)

chat = client.chats.create(model=modelo)

respuesta = chat.send_message("Quien fue el primer hombre en pisar la luna?")

print("respuesta: ", respuesta.text)


