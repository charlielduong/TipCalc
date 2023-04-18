from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allows requests that originate from a different protocol
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return "This is connected to the backend: main.py"

# DOESNT WORK
@app.post("/form")
async def submit_form_data(formData: dict):
    # handle form data
    return {"message": "Form data received"}
