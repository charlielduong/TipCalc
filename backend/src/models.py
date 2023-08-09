from typing import List, Optional
from pydantic import BaseModel

class FormItem(BaseModel):
    people: list[str]
    numOfPeople: int
    amountDue: list[float]
    tip: float
    tax: float

class ReceiptReaderItem(BaseModel):
    imagepath: str
