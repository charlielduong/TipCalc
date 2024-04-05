from typing import List, Optional
from fastapi import FastAPI, Form, UploadFile, File, Request, Depends, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

# from src.models import FormItem
import logging
import io
import json
import re
import requests
# from pymongo import MongoClient
import os
from pydantic import BaseModel
from typing import List

app = FastAPI()
    

# client = MongoClient("mongodb://your_mongo_server_address:27017/")
# db = client["your_database_name"]
# collection = db["your_collection_name"]

origins = [
    "http://localhost:8080",
    "http://localhost:5000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # Allow all ports
    allow_credentials=True,
    allow_methods=["GET", "POST"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def home():
    return "This is connected to the backend: main.py"

@app.post("/process_form")
async def process_form(request: Request):
    data = await request.json()

    name_cost_dict = {}

    # Iterate through each item in the purchases
    for item_name, buyers in data["purchases"].items():
        item_cost = next(item["itemCost"] for item in data["items"] if item["itemName"] == item_name)
        num_buyers = len(buyers)
        cost_per_buyer = item_cost / num_buyers  # Calculate the cost per buyer
        for buyer in buyers:
            if buyer in name_cost_dict:
                name_cost_dict[buyer] += cost_per_buyer
            else:
                name_cost_dict[buyer] = cost_per_buyer
    # Calculate the total cost of the items
    total_cost = sum(name_cost_dict.values())
    # Calculate the total cost of the purchases, including the tip and tax
    total_cost_with_tip_and_tax = total_cost + data["tip"] + data["tax"]
    # Calculate the percentage of the tip and tax
    tip_percentage = (data["tip"] / total_cost) * 100
    tax_percentage = (data["tax"] / total_cost) * 100

    for purchase in name_cost_dict:
        purchase_cost = name_cost_dict[purchase]
        increase_amount = (purchase_cost * tip_percentage / 100) + (purchase_cost * tax_percentage / 100)
        name_cost_dict[purchase] += increase_amount

    return(name_cost_dict)
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