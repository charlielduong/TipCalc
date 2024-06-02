from typing import List, Optional
from fastapi import FastAPI, Form, UploadFile, File, Request, Depends, Response, HTTPException, Cookie
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pymongo import MongoClient
from datetime import datetime


# from src.models import FormItem
import logging
import io
import json
import re
import requests
import pymongo
import os
from pydantic import BaseModel
from typing import List

app = FastAPI()

origins = [
    "http://localhost:8080",
    "http://localhost:5000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # Allow all ports
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def home():
    return "This is connected to the backend: main.py"

logging.basicConfig(level=logging.INFO)

try:
    client = MongoClient("mongodb+srv://isaacrhong:RSjG23Javdjp49HA@testcluster.bea5cko.mongodb.net/")
    db = client["purchases"]
    collection = db["reciepts"]
    items = list(collection.find({}))
    if db.counters.find_one({"_id": "itemId"}) is None:
        db.counters.insert_one({"_id": "itemId", "seq": 1})
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

@app.get("/get_items")
async def get_items():
    try:
        items = list(collection.find({}))  # Fetch all items from the collection
        # Serialize MongoDB documents to JSON
        serialized_items = []
        for item in items:
            item['_id'] = str(item['_id'])  # Convert ObjectId to string
            item["created_at"] = item["created_at"].isoformat()
            serialized_items.append(item)
        return JSONResponse(content={"items": serialized_items})
    except Exception as e:
        logging.error(f"Error fetching items: {e}")
        raise HTTPException(status_code=500, detail=f"Error fetching items: {e}")
    
@app.get("/get_id")
async def get_id():
    try:
        counter_document = db['counters'].find_one({"_id": "itemId"})
        if counter_document:
            return counter_document["seq"] + 1
        else:
            return None  # Counter not found
    except Exception as e:
        print(f"Error getting counter value: {e}")
        return None
    
# Helper Function to Get the Next Sequence Value
def get_next_sequence_value(sequence_name):
    try:
        sequence_document = db.counters.find_one_and_update(
            {"_id": sequence_name},
            {"$inc": {"seq": 1}},
            return_document=True  # Use 'return_document=ReturnDocument.AFTER' for pymongo<4.0
        )
        return sequence_document["seq"]
    except Exception as e:
        print(f"Error getting next sequence value: {e}")
        raise

def get_cookie(cookie_name: str = Cookie(None)):
    return {cookie_name}

# Submit all the data to MongoDB
@app.post("/process_form")
async def process_form(request: Request):
    # Get all the data from the front end and parse it into a JSON file
    try:
        data = await request.json()
    except Exception as e:
        print(f"Error parsing JSON data: {e}")
        return JSONResponse(content={"error": f"Error parsing JSON data: {e}"}, status_code=400)

    # Get the current Date and Time
    try:
        created_at = datetime()
    except Exception as e:
        print(f"Error generating timestamp: {e}")
        return JSONResponse(content={"error": f"Error generating timestamp: {e}"}, status_code=500)
    
    try:
        cookie = get_cookie()
    except Exception as e:
        print(f"Error generating timestamp: {e}")
        return JSONResponse(content={"error": f"Error generating timestamp: {e}"}, status_code=500)

        # Get the next ID in the sequence
    try:
        next_id = get_next_sequence_value("itemId")
    except Exception as e:
        print(f"Error generating next ID: {e}")
        return JSONResponse(content={"error": f"Error generating next ID: {e}"}, status_code=500)
    
    # Create a document to store in the MongoDB
    try:
        document = {
            "_id": next_id,
            "data": data,
            "created_at": created_at,
            "cookie": cookie,
        }
        result = collection.insert_one(document)
    except Exception as e:
        print(f"Error inserting document into MongoDB: {e}")
        return JSONResponse(content={"error": f"Error inserting document into MongoDB: {e}"}, status_code=500)

    return JSONResponse(content={"message": "Data processed and stored", "document_id": str(result.inserted_id)})

if __name__ == '__main__':
    app.run(debug=True)

    # # Iterate through each item in the purchases
    # for item_name, buyers in data["purchases"].items():
    #     item_cost = next(item["itemCost"] for item in data["items"] if item["itemName"] == item_name)
    #     num_buyers = len(buyers)
    #     cost_per_buyer = item_cost / num_buyers  # Calculate the cost per buyer
    #     for buyer in buyers:
    #         if buyer in name_cost_dict:
    #             name_cost_dict[buyer] += cost_per_buyer
    #         else:
    #             name_cost_dict[buyer] = cost_per_buyer
    # # Calculate the total cost of the items
    # total_cost = sum(name_cost_dict.values())
    # # Calculate the total cost of the purchases, including the tip and tax
    # total_cost_with_tip_and_tax = total_cost + data["tip"] + data["tax"]
    # # Calculate the percentage of the tip and tax
    # tip_percentage = (data["tip"] / total_cost) * 100
    # tax_percentage = (data["tax"] / total_cost) * 100

    # for purchase in name_cost_dict:
    #     purchase_cost = name_cost_dict[purchase]
    #     increase_amount = (purchase_cost * tip_percentage / 100) + (purchase_cost * tax_percentage / 100)
    #     name_cost_dict[purchase] += increase_amount
    # return(name_cost_dict)
    # data is now an instance of FormData
    # formData = data
    # if formData:
    #     return {"message": "Data processed successfully"}
    # else:
    #     return {"message": "No formData found in the request"}

# @app.post("/process_form")
# async def process_form(data: FormData):
#     # data is now an instance of FormData
#     response_dict = {"message": "Data processed successfully"}
#     return Response(content=response_dict, media_type="application/json")


    # # Initialize variables for total tax, tip, and other fees
    # total_tax = 0
    # total_tip = 0
    # total_other_fees = 0  # Replace this with your actual other fees calculation

    # # Calculate the total amount owed by each customer
    # total_customers_amount = 0
    # for customer in json_data["customers"]:
    #     customer_total = 0
    #     for order in customer["orders"]:
    #         item_price = order["price"]
    #         customer_total += item_price

    #     # Add tax and tip to the customer's total
    #     customer_tax = customer_total * json_data["tax_percentage"] / 100
    #     customer_tip = customer_total * json_data["tip_percentage"] / 100
    #     customer_total += customer_tax + customer_tip + total_other_fees

    #     # Update the total tax, tip, and individual total amount owed
    #     total_tax += customer_tax
    #     total_tip += customer_tip
    #     total_customers_amount += customer_total

    # # Calculate the total bill amount
    # total_bill_amount = total_customers_amount + total_tax + total_tip + total_other_fees

    # # Return a JSON response with the calculated values
    # return JSONResponse(
    #     content={
    #         "total_tax": total_tax,
    #         "total_tip": total_tip,
    #         "total_other_fees": total_other_fees,
    #         "total_customers_amount": total_customers_amount,
    #         "total_bill_amount": total_bill_amount,
    #     }
    # )