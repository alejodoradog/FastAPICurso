from fastapi import FastAPI
from datetime import datetime
import zoneinfo
from models import Customer, CustomerCreate, Transaction, Invoice
from db import SessionDep

    

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

@app.post("/customers",response_model=Customer)
async def create_customer(customer_data: CustomerCreate, session: SessionDep):
    customer = Customer.model_validate(customer_data.model_dump())
    return {"customer": customer}

@app.post("/transactions")
async def create_transaction(transaction_data: Transaction):
    return {"transaction": transaction_data}

@app.post("/invoices")
async def create_invoice(invoice_data: Invoice):
    return {"invoice": invoice_data}


@app.get("/customers",response_model=list[Customer])
async def get_customers():
    return [Customer(id=1,name="Alejandro",description="inge",age=23,email="[EMAIL_ADDRESS]")]