from pydantic import BaseModel
from sqlmodel import SQLModel

class CustomeBase(SQLModel):
    name: str
    description: str | None
    age: int
    email: str

class CustomerCreate(CustomeBase):
    pass

class Customer(SQLModel, table = True):
    id: int|None = None


class Transaction(BaseModel):
    id: int
    amount: float
    description: str 

class Invoice(BaseModel):
    id: int
    amount: float
    description: str
    customer: Customer
    transactions: list[Transaction]
    total_transactions: float

    @property
    def total_transactions(self):
        return sum(transaction.amount for transaction in self.transactions) 