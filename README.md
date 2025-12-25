# 🧾 Intelligent Expense Extractor

Proste, ale potężne narzędzie CLI do strukturyzacji nieuporządkowanych danych finansowych przy użyciu AI. Projekt realizowany w ramach ścieżki **AI Engineer 2026**.

## 💡 O projekcie

Celem tego projektu jest rozwiązanie problemu "brudnych danych" w wydatkach osobistych. Zamiast ręcznie wpisywać dane do Excela, użytkownik podaje opis w języku naturalnym (np. *"Kupiłem kawę i ciastko w Starbucksie za 25 zeta"*), a system:

1.  Interpretuje intencję użytkownika przy użyciu modelu LLM.
2.  Wyciąga kluczowe informacje (kwota, waluta, kategoria).
3.  Zwraca ściśle typowany obiekt JSON, gotowy do zapisu w bazie danych.

Projekt kładzie nacisk na **Type Safety** i **Clean Code**, unikając halucynacji AI poprzez wymuszone schematy (Structured Outputs).

## 🛠️ Tech Stack

* **Python 3.12+**
* **OpenAI API** (Structured Outputs / `gpt-4o-mini`)
* **Pydantic** (Walidacja danych i definicja schematów)
* **Pydantic Settings** (Zarządzanie konfiguracją i sekretami)
* **uv** (Nowoczesny menedżer pakietów i środowiska wirtualnego)

## 📂 Struktura Projektu

```text
.
├── src/
│   ├── config.py       # Konfiguracja i ładowanie zmiennych (.env)
│   ├── extractor.py    # Logika biznesowa i komunikacja z OpenAI
│   ├── schemas.py      # Modele danych Pydantic i Enumy
│   └── main.py         # Entrypoint aplikacji (CLI)
├── .env.example        # Szablon zmiennych środowiskowych
├── pyproject.toml      # Definicja zależności (uv)
└── README.md

```
## 🚀 Instalacja i Uruchomienie
Projekt wykorzystuje uv do błyskawicznego zarządzania zależnościami.

### Sklonuj repozytorium:

``` Bash

git clone [https://github.com/twoj-user/expense-extractor.git](https://github.com/twoj-user/expense-extractor.git)
cd expense-extractor
```
### Skonfiguruj środowisko: Utwórz plik .env na podstawie przykładu:

``` Bash

cp .env.example .env
```
### Następnie wklej swój klucz API w pliku .env:

``` Ini, TOML

OPENAI_API_KEY=sk-proj-...
```
### Zainstaluj zależności:

``` Bash

uv sync
``` 
### Uruchom aplikację:

``` Bash

uv run ./main.py
``` 
## 🧠 Przykłady Użycia
### Input:

"Zatankowałem samochód służbowy na Orlenie za 250 zł"

### Output (Internal Object):

``` Python

Expense(
    description='Paliwo na stacji Orlen',
    amount=250.0,
    currency='PLN',
    category=<Category.TRAVEL: 'travel'>,
    is_business=True
)
```
## 🗺️ Roadmapa (AI Engineer Path)
[x] Krok 1: Foundations & Structured Data (Pydantic + OpenAI)

[ ] Krok 2: System Design (Oddzielenie logiki od I/O)

[ ] Krok 3: API Backend (Migracja do FastAPI + Docker)

[ ] Krok 4: Baza Danych (Zapis wyników do PostgreSQL)