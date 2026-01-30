from fastapi import FastAPI
from datetime import datetime

app = FastAPI()
hora = datetime.now()

@app.get("/")
async def root():
    return {"Mensaje" : "Hola mundo"}

@app.get("/time")
async def time():
    return {"message": f"Hola, FastAPI! la hora es {hora}"}

