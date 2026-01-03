"""Entry point for CLI (interactive mode)."""
import asyncio
from src.extractor import extract_expense


def main():
    """Main function for CLI."""
    user_input = input("Enter expense: ")
    data = asyncio.run(extract_expense(user_input))

    print("--- Your data: ---")
    print(
        f"Category: {data.category.value}\n"
        f"Description: {data.description}\n"
        f"Amount: {data.amount} {data.currency}"
    )


if __name__ == "__main__":
    main()

