from typing import List, Optional
from fastapi import FastAPI, Form, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from src.models import FormItem
import logging

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


# @app.post("/form")
# async def submit_form_data(
#     people: List[str] = Form(...),
#     numOfPeople: int = Form(...),
#     amountDue: List[float] = Form(...),
#     tipAndTax: List[int] = Form(...)
# ):
#     new_form_data = FormItem(
#         people=people,
#         numOfPeople=numOfPeople,
#         amountDue=amountDue,
#         tipAndTax=tipAndTax
#     )
#     logging.info("THIS IS RUNNING")
#     return {"data": new_form_data.dict()}

# Takes an image file and returns its name
@app.post("/receipt")
async def upload_receipt(file: UploadFile = File(...)):
    # Here, you can use file.file to access the uploaded file object
    # You could use PyTesseract or another library here to process the image
    return {"filename": file.filename}