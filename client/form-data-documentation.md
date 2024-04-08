# IPFMF MVP Documentation

## Introduction
This document outlines the functionality and workflow of the Minimum Viable Product (MVP) for IPFMF(I paid for my friends), which includes handling inputs from users, assigning items to people, calculating tax and tip, and displaying the total costs.

## Features Overview
- **Input Handling:**
  - Accept inputs such as the number of people, their names, items, prices, tax, and tip.
  - Validate and process user inputs to ensure data integrity.

- **Assignment of Items:**
  - Assign items to people based on user inputs.
  - Implement logic to evenly distribute items and prices among the specified number of people.

- **Calculation of Costs:**
  - Calculate the subtotal for each person based on the assigned items and their prices.
  - Calculate the total cost including tax and tip.

- **Display of Results:**
  - Return the calculated costs to the frontend for display to the client.

## User Stories
- As a user, I want to enter the number of people, their names, items, and prices to calculate the total cost per person including tax and tip.
- As a user, I want the item's price to be evenly distributed among the specified number of people.
- As a user, I want to see the calculated costs displayed clearly on the frontend.

## Input Handling
- **Number of People:**
  - Accept the number of people participating in the transaction.

- **Names of People:**
  - Allow users to enter the names of each person.

- **Items and Prices:**
  - Enable users to input items and their corresponding prices.
  - Ensure proper validation of item names and prices.

- **Tax and Tip:**
  - Accept tax and tip amounts as inputs.

## Assignment of Items
- Implement logic to evenly distribute items among the specified number of people.
- Calculate the subtotal for each person based on the assigned items and their prices.

## Calculation of Costs
- Calculate the total cost by summing up individual subtotals.
- Apply tax and tip as percentages to the total cost.
- Calculate the final total including tax and tip.

**Example Calculation:**

Let's consider the following dummy data:
formData: {
    names: ["Name1", "Name2", "Name3"],
    items: [{ itemName: "Item1", itemCost: 20 }, { itemName: "Item2", itemCost: 30 }],
    "purchases": {"Item2":["Name1","Name2","Name3"],"Item1":["Name1","Name2"]}
    tax: 3,
    tip: 10,
    fees: 0
}

When we send the data to the backend using a get request
then we calculate the how much each person pays by dividing the cost of the
item by how many people are buying it.

Then we calculate the tax and tip percentages based off the give flat values.

After that, we calculate the total cost including tax and tip.

Finally, we return this data back to the front end:
name_cost_dict: {
    Name2: 25.2
    Name1: 25.2
    Name3: 12.6
}


## Display of Results
- Return the calculated total


## Known Issues and Limitations
- Issue 1: For amount of people it accepts negative inputs.
- Issue 2: For item prices it accepts negative inputs.
- Issue 3: There is no way to edit the purchases dict once it is initialized.
- Issue 4: Currently Optional Fees does nothing.
- Issue 5: Dummy data used for testing is still being used.
- Issue 6: There is no fail safe for cases where people have the same name.
- Issue 7: There is no fail safe for cases where not all items are assinged a person.
- Issue 8: For taxes, tip and optional fees they accept negative inputs.