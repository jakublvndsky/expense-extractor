from openai import AsyncOpenAI
from src.config import settings
from src.schemas import Expense
from datetime import datetime
import asyncio
client = AsyncOpenAI(api_key=settings.openai_api_key)


async def extract_expense(text: str) -> Expense:
    current_data = datetime.now().strftime("%d/%m/%Y")
    response = await client.responses.parse(
        model="gpt-4o-mini",
        input=[
            {
                "role": "system",
                "content": f"Jesteś asystentem do kategoryzacji wydatków wedle otrzymanego schematu, dzisiejsza data to {current_data}, masz ustrukturyzowac wiadomość do obiektu JSON.",
            },
            {"role": "user", "content": text},
        ],
        temperature=0.1,
        text_format=Expense,
    )
    categorized_output = response.output_parsed
    return categorized_output


if __name__ == "__main__":
    user_input = input("Podaj wydatek: ")
    wynik = asyncio.run(extract_expense(user_input))

    print("--- ZWRÓCONY OBIEKT ---")
    print(
        f"Kategoria: {wynik.category.value}\nOpis: {wynik.description}\nKwota: {wynik.amount} {wynik.currency}"
    )
