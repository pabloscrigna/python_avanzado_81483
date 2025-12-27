from fastapi import FastAPI
from contextlib import asynccontextmanager
from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_URI, DB_NAME

@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- STARTUP ---
    print("🚀 La aplicación se está iniciando...")
    app.state.started = True
    client = AsyncIOMotorClient(MONGO_URI)
    app.state.mongo_client = client
    app.state.db = client[DB_NAME]
    yield
    # --- SHUTDOWN ---
    print("🛑 La aplicación se está apagando...")


app = FastAPI(lifespan=lifespan)


@app.get("/alumnos")
async def get_alumnos():
    alumnos = []
    print("Obteniendo alumnos de la base de datos...")
    cursor = app.state.db.alumnos.find()

    async for alumno in cursor:
        alumno["_id"] = str(alumno["_id"])  # ObjectId → str
        alumnos.append(alumno)

    return {
        "total": len(alumnos),
        "items": alumnos
    }


@app.get("/")
async def root():
    return {"message": "Hello World"}