import os
from fastapi import FastAPI

app = FastAPI()
PORT = int(os.getenv("PORT", 8080))  # Default to 8080 if unspecified

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!", "port": PORT}



