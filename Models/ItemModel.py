from pydantic import BaseModel
class Item():
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    def __init__(self, name, description,price,tax):
        self.name=name
        self.description=description
        self.price=price
        self.tax=tax