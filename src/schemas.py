from pydantic import BaseModel
from enum import Enum


class Category(str, Enum):
    FOOD = "food"
    TRAVEL = "travel"
    OFFICE = "office"
    OTHER = "other"


class Expense(BaseModel):
    description: str
    amount: float  # TODO: dodać wartość decimal do wdrozenia produkcyjnego
    currency: str
    category: Category
    is_business: bool
