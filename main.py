### expense_extractor
# CEL ZADANIA: Zwracać ustrukturyzowany output, który został zrealizowany przez AI
# 1. Wrzucamy dane do przetworzenia
# 2. AI przetwarza te dane
# 3. Przypisuje do odpowiednich key: value w takiej strukturze jak sobie tego zyczymy
# 4. mamy ustrukturyzowany output w postaci JSON, który mozemy przetwarzać dalej, a moze dodac jakis Pandas
# Potrzebujemy importu biblioteki openai, aby mieć dostęp do ustrukturyzowanych danych
# Dane wejściowe mozemy umieścić w klasie, która przygotuje te dane do AI lub właśnie sprawdzi za pomocą try...except... czy jest to w ogóle JSON i czy wszyzstko się zgadza
# Środowisko, którego uzywam to uv. Obecnie moja struktura plików jest prosta, posiada .gitignore, .python-version, main.py, pyproject.toml, readme.md oraz folder src, a takze .venv
import asyncio
import uvicorn
from src.extractor import extract_expense
from src.api import app

if __name__ == "__main__":
    user_input = input("Podaj wydatek: ")
    dane = asyncio.run(extract_expense(user_input))

    print("--- Oto Twoje dane: ---")
    print(
        f"Kategoria: {dane.category.value}\nOpis: {dane.description}\nWartość: {dane.amount} {dane.currency}"
    )
    uvicorn.run(app, host="0.0.0.0", port=8000)