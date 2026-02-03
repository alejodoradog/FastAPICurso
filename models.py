from pydantic import BaseModel

class Customer(BaseModel):
    id: int
    name: str
    description: str | None
    age: int
    email: str

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