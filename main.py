from fastapi import FastAPI
from datetime import datetime
import zoneinfo

app = FastAPI()
country_timezones = {
    "CO": "America/Bogota",
    "MX": "America/Mexico_City",
    "AR": "America/Argentina/Buenos_Aires",
    "BR": "America/Sao_Paulo",
    "PE": "America/Lima",
}


@app.get("/")
async def root():
    return {"Mensaje" : "Hola mundo"}

@app.get("/time/{iso_code}")
async def time(iso_code: str):
    iso_code = iso_code.upper() #para transformar todo a mayúsculas
    timezone_Str = country_timezones.get(iso_code) #esto lo que hace es que me trae la zona teniendo en cuenta el iso_code que le pasamos en la variable al endpoint Y LO CONVIERTE A STRING
    tz = zoneinfo.ZoneInfo(timezone_Str) #recibe la zona y devuelve info sobre ella para poder luego obtener la hora
    hora = datetime.now(tz)
    return {f"Hora en {timezone_Str}": f"la hora es {hora}"}


