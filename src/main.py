from dotenv import load_dotenv
import os

import uvicorn

from fastapi import FastAPI
from routers import movies_router, books_router

api_description = """
A simple API to demonstrate Behave testing.

This application does not persist state; all data is stored in memory.

Whenever the service restarts, the data returns to its original state.
"""

app = FastAPI(
    title="Behave Demo API",
    description=api_description,
)

app.include_router(movies_router.router)
app.include_router(books_router.router)

load_dotenv()

host = os.getenv("HOST", "127.0.0.1")
port = int(os.getenv("PORT", 8000))

if __name__ == "__main__":
    print (f"Starting server at http://{host}:{port}/docs")
    uvicorn.run("main:app", host=host, port=port, reload=True)
