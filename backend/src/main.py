from typing import List, Optional
from fastapi import FastAPI, Form, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from src.models import FormItem
import logging
import io
from PIL import Image
import pytesseract
import json
import re
import requests
from pymongo import MongoClient
import os

app = FastAPI()

ASPRISE_OCR_URL = "http://ocr.asprise.com/api/v1/receipt"
API_KEY = os.getenv("API_KEY")

client = MongoClient("mongodb://your_mongo_server_address:27017/")
db = client["your_database_name"]
collection = db["your_collection_name"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow all ports
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def home():
    return "This is connected to the backend: main.py"


@app.post("/form")
async def submit_form_data(
    people: List[str] = Form(...),
    numOfPeople: int = Form(...),
    amountDue: List[float] = Form(...),
    tipAndTax: List[int] = Form(...)
):
    new_form_data = FormItem(
        people=people,
        numOfPeople=numOfPeople,
        amountDue=amountDue,
        tipAndTax=tipAndTax
    )
    logging.info("THIS IS RUNNING")
    return {"data": new_form_data.dict()}

def process_receipt_data(data: dict) -> dict:
    # Assuming there's only one receipt for simplicity
    receipt = data['receipts'][0]

    # Extract items
    items = {item['description']: item['amount'] for item in receipt['items']}

    # Extract total
    total = receipt['total']

    # Use a default user_tip_percentage (you can change this as per your requirements)
    user_tip_percentage = 10  # example value
    tip = (user_tip_percentage / 100) * total

    # To calculate tax, subtract the sum of item amounts and the tip from the total
    tax = total - sum(items.values()) - tip

    # Create a dictionary with the processed data
    processed_data = {
        "items": items,
        "total": total,
        "tax": tax,
        "tip": tip
    }

    return processed_data

# Takes an image file and returns its name
@app.post("/receipt")
async def upload_receipt(file: UploadFile = File(...)):
    # Read the file contents
    contents = await file.read()
    
    # Prepare data and headers for the request
    headers = {
        "Ocp-Apim-Subscription-Key": API_KEY,  # The API key header might differ, refer to the API documentation
        # Add other headers as required by the API documentation
    }
    files = {
        "file": (file.filename, contents)
    }

    # Make the request
    response = requests.post(ASPRISE_OCR_URL, headers=headers, files=files)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Process the fetched data
        processed_data = process_receipt_data(data)

        # Store the processed data in MongoDB
        collection.insert_one(processed_data)

        # Save the processed data to an output JSON file
        with open("processed_output.json", "w") as json_file:
            json.dump(processed_data, json_file, indent=4)
        
        return {"message": "Data processed and saved to processed_output.json", "data": processed_data}
    else:
        return {"error": "Failed to process the image", "details": response.text}

@app.get("/receipts")
async def get_all_receipts():
    receipts = list(collection.find())
    for receipt in receipts:
        receipt["_id"] = str(receipt["_id"])  # Convert ObjectId() to string
    return receipts
