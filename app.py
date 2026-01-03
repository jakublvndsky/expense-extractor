"""Entry point for API server."""
import uvicorn


def main():
    """Main function for API server."""
    uvicorn.run("src.api:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()

