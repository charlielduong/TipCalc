from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from src.models import FormObject, FormItem


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
async def submit_form_data(new_form_data: FormItem):
    return {"data": new_form_data}

# @app.get("/form")
# async def get_form_data(new_form_data: FormObject):
#     return {"data": new_form_data}