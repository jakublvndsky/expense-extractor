# 🧾 Intelligent Expense Extractor

A simple yet powerful CLI and API tool for structuring unstructured financial data using AI. Project developed as part of the **AI Engineer 2026** path.

## 💡 About the Project

The goal of this project is to solve the "dirty data" problem in personal expenses. Instead of manually entering data into Excel, users provide a description in natural language (e.g., *"I bought coffee and a cookie at Starbucks for 25 zloty"*), and the system:

1. Interprets user intent using an LLM model.
2. Extracts key information (amount, currency, category).
3. Returns a strictly typed JSON object, ready for database storage.

The project emphasizes **Type Safety** and **Clean Code**, avoiding AI hallucinations through enforced schemas (Structured Outputs).

## 🛠️ Tech Stack

* **Python 3.12+**
* **FastAPI** (Modern web framework with automatic API documentation)
* **OpenAI API** (Structured Outputs / `gpt-4o-mini`)
* **Pydantic** (Data validation and schema definition)
* **Pydantic Settings** (Configuration and secrets management)
* **Uvicorn** (ASGI server for running FastAPI)
* **uv** (Modern package manager and virtual environment tool)

## 📂 Project Structure

```text
.
├── src/
│   ├── __init__.py
│   ├── api.py          # FastAPI application and REST endpoints
│   ├── config.py       # Configuration and environment variables (.env)
│   ├── extractor.py    # Business logic and OpenAI communication
│   └── schemas.py      # Pydantic data models and Enums
├── app.py              # API server entry point
├── cli.py              # CLI entry point (interactive mode)
├── .python-version     # Python version
├── .env.example        # Environment variables template
├── pyproject.toml      # Dependencies definition (uv)
├── README.md
└── uv.lock             # Lock file with exact package versions
```

## 🚀 Installation and Setup

The project uses `uv` for fast dependency management.

### Clone the repository:

```bash
git clone https://github.com/your-user/expense-extractor.git
cd expense-extractor
```

### Configure environment:

Create a `.env` file based on the example:

```bash
cp .env.example .env
```

Then paste your API key in the `.env` file:

```ini
OPENAI_API_KEY=sk-proj-...
```

### Install dependencies:

```bash
uv sync
```

## 🏃 Running the Application

### Option 1: CLI Mode (Interactive)

Run the interactive command-line interface:

```bash
uv run python cli.py
```

The application will prompt you to enter an expense description in natural language.

### Option 2: API Server (FastAPI)

Start the API server (recommended):

```bash
uv run python app.py
```

This will start the server with auto-reload enabled (changes to code will automatically restart the server).

Alternatively, you can use uvicorn directly:

```bash
uv run uvicorn src.api:app --reload
```

**Note:** The `--reload` flag is only needed when using uvicorn directly. When running `python app.py`, reload is already enabled in the code.

The server will be available at:
- **API**: `http://localhost:8000`
- **Swagger Documentation**: `http://localhost:8000/docs`
- **ReDoc Documentation**: `http://localhost:8000/redoc`

## 📡 API Endpoints

### POST `/extract-expense`

Extracts and structures expense information from natural language text.

**Request Body:**
```json
{
  "text": "I bought coffee for 15 PLN at a café"
}
```

**Response (200 OK):**
```json
{
  "description": "Café",
  "amount": 15.0,
  "currency": "PLN",
  "category": "food",
  "is_business": false
}
```

**Example using curl:**
```bash
curl -X POST "http://localhost:8000/extract-expense" \
     -H "Content-Type: application/json" \
     -d '{"text": "I refueled my company car at Orlen for 250 PLN"}'
```

## 🧠 Usage Examples

### Input:

"I refueled my company car at Orlen for 250 PLN"

### Output (Internal Object):

```python
Expense(
    description='Fuel at Orlen station',
    amount=250.0,
    currency='PLN',
    category=<Category.TRAVEL: 'travel'>,
    is_business=True
)
```

### Output (JSON API Response):

```json
{
  "description": "Fuel at Orlen station",
  "amount": 250.0,
  "currency": "PLN",
  "category": "travel",
  "is_business": true
}
```

## 🗺️ Roadmap (AI Engineer Path)

- [x] Step 1: Foundations & Structured Data (Pydantic + OpenAI)
- [x] Step 2: System Design (Separation of business logic from I/O)
- [x] Step 3: API Backend (Migration to FastAPI)
- [ ] Step 4: Database (Save results to PostgreSQL)
- [ ] Step 5: Docker & Deployment
- [ ] Step 6: Unit and Integration Tests
