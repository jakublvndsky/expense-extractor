from fastapi import FastAPI
from src.schemas import ExpenseRequest
from src.extractor import extract_expense

app = FastAPI()

@app.post("/extract-expense")
async def extract_expense_endpoint(request: ExpenseRequest):
    expense = await extract_expense(request.text)
    return expense