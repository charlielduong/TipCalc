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

app = FastAPI()

class FormData(BaseModel):
    # TODO Define form data model here
    field1:str

# client = MongoClient("mongodb://your_mongo_server_address:27017/")
# db = client["your_database_name"]
# collection = db["your_collection_name"]


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

@app.post("/process_form")
async def process_form(data: FormData):
    # data is now an instance of FormData
    response_dict = {"message": "Data processed successfully"}
    return Response(content=response_dict, media_type="application/json")


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