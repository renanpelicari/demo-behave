# config.py
from dotenv import load_dotenv
import os

load_dotenv()

API_HOST = os.getenv("HOST", "127.0.0.1")
API_PORT = int(os.getenv("PORT", 8000))
API_URL = f"http://{API_HOST}:{API_PORT}"
