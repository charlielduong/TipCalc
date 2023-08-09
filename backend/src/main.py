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

app = FastAPI()

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

def clean_ocr_output(text):
    # Remove any form feed characters
    text = text.replace("\f", "")
    
    # Split text into lines and clean each line
    lines = text.split("\n")
    cleaned_lines = []

    for line in lines:
        line = line.strip()  # Strip whitespace
        
        # Replace multiple spaces with single space
        line = re.sub(r'\s+', ' ', line)
        
        # Only include lines with at least one alphabetic character (filter out lines that are just artifacts)
        if re.search(r'[A-Za-z]', line):
            cleaned_lines.append(line)

    # Join the cleaned lines back into a single string
    cleaned_text = "\n".join(cleaned_lines)
    
    return cleaned_text

# Takes an image file and returns its name
@app.post("/receipt")
async def upload_receipt(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    raw_text = pytesseract.image_to_string(image)
    cleaned_text = clean_ocr_output(raw_text)

    # Convert newline characters to spaces for a more legible response
    legible_text = cleaned_text.replace('\n', ' ').strip()

    # Construct the data dictionary
    data = {
        "filename": file.filename,
        "text": legible_text  # Use the legible_text here
    }

    # Serialize the dictionary to a JSON string
    json_str = json.dumps(data, indent=4)

    # Define the name for the JSON file
    json_filename = "output.json"

    # Write the JSON string to a file
    with open(json_filename, 'w') as json_file:
        json_file.write(json_str)
    
    # Return the legible text
    return {"text": legible_text}