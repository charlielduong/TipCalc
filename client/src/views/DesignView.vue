<template>
    <div class="design">

        <section class="form section">

            <div class="form__container container grid">

                <!-- FORM NAME INPUT -->
                <div class="form__screen" v-if="currentFormStep === 1">
                    <h2 class="form__label">Who owes you money?</h2>
                    <form action="" class="receipt__form" id="receipt-form" @submit.prevent>
                        <div class="form__group grid">
                            <div class="form__box">
                                <input class="form__item" type="text" placeholder="Enter Name" v-model="newName"
                                    @keyup.esc="addName">
                                <button type="button" class="form__box-button" @click="addName">Add Person</button>
                            </div>
                            <ul class="form__list">
                                <div class="form__list-names" v-for="(item, index) in formData.names" :key="index">
                                    <li class="form__list-names-{{ index }}" @click="deleteName(index)">{{ item }}</li>
                                </div>
                            </ul>
                            <!-- <button class="form__group-button button" @click.prevent="nextStep">Next</button> -->
                        </div>
                    </form>
                </div>

                <!-- FORM ITEM INPUT -->
                <div class="form__screen" v-else-if="currentFormStep === 2">
                    <h2 class="form__label">What items were purchased?</h2>
                    <form action="" class="receipt__form" id="receipt-form">
                        <div class="form__group grid">
                            <div class="form__box">
                                <!-- CSS ISNT CONSISTENT WITH FIRST FORM (Fix later) -->
                                <!-- Be able to enter IF both inputs are filled (Fix later) -->
                                <input class="form__item form__item-name" type="text" placeholder="Enter Name"
                                    v-model="newItemName">
                                <input class="form__item form__item-cost" type="text" placeholder="Enter Cost"
                                    v-model.number="newItemCost">
                                <button type="button" class="form__box-button" @click="addItem">Add Item</button>
                            </div>
                            <ul class="form__list">
                                <div class="form__list-names" v-for="(item, index) in formData.items" :key="index">
                                    <li class="form__list-names-{{ index }}" @click="deleteItem(index)">{{ item.itemName
                                        }} - {{ item.itemCost }}
                                    </li>
                                </div>
                            </ul>
                            <!-- <button type="button" class="form__box-button button" @click="addPerson">Add Person</button> -->
                            <!-- <button class="form__group-button button" @click.prevent="nextStep">Next</button> -->
                        </div>
                    </form>
                </div>

                <!-- FORM NAME TO ITEM INPUT -->
                <div class="form__screen" v-else-if="currentFormStep === 3">
                    <form action="" class="receipt__form" id="receipt-form">
                        <template v-for="(name, index) in formData.names">
                            <div class="form__label" v-if="index === currentNameIndex">
                                <h2 class="form__label-text">What did </h2>
                                <div class="form__label-name form__list-names">{{ name }}</div>
                                <h2 class="form__screen-text"> purchase?</h2>
                            </div>

                            <div class="form__group" v-if="index === currentNameIndex">
                                <div class="form__list-purchases" v-for="item in formData.items">
                                    <label class="checkbox__label">
                                        <input class="checkbox__input" type="checkbox"
                                            @change="updatePurchases(item, name)" :value="item"
                                            v-model="item.selected" />
                                        <span class="label__text">{{ item.itemName }}</span>
                                    </label>
                                </div>
                            </div>
                        </template>
                        <div class="button-container">
                            <button class="form__group-button button" @click.prevent="previousPerson">Previous</button>
                            <button class="form__group-button button" @click.prevent="nextPerson">Next</button>
                        </div>
                    </form>
                </div>

                <!-- FORM UNASSIGNED ITEM FALLBACK -->
                <!-- TODO: Currently only allows one person to be assigned. Needs to be multiple -->
                <div class="form__screen" v-else-if="currentFormStep === 4">
                    <h2 v-if="this.unassignedItems.length > 0" class="form__screen-label">Warning!</h2>
                    <template v-for="item in unassignedItems">
                        <div class="form__label">
                            <p>{{ item.itemName }} wasn't accounted for.</p>
                            <p>Who bought {{ item.itemName }}?</p>
                        </div>
                        <div class="form__group">
                            <label class="checkbox__label" v-for="name in formData.names" :key="name">
                                <input class="checkbox__input" type="checkbox" @change="updatePurchases(item, name)" :value="name"
                                    v-model="item.selected" />
                                <span class="label__text">{{ name }}</span>
                            </label>
                        </div>
                    </template>
                </div>

                <!-- FORM TIP AND TAX INPUT -->
                <div class="form__screen" v-else-if="currentFormStep === 5">
                    <h2>Enter Tip, Tax, and Other Fees</h2>
                    <form action="" class="receipt__form" id="receipt-form">
                        <div class="form__box">
                            <input class="form__item" type="text" placeholder="Enter Tip" style="display: block;"
                                v-model="this.formData.tip" />
                            <input class="form__item" type="text" placeholder="Enter Tax" style="display: block;"
                                v-model="this.formData.tax" />
                        </div>
                        <!-- <button class="form__group-button button" @click.prevent="nextStep">Next</button> -->
                    </form>
                </div>

                <!-- FORM SUMMARY -->
                <div class="form__screen" v-else="currentFormStep === 6">
                    <h1>Success!</h1>
                    <div v-for="(amount, name) in amountsOwed" :key="name">
                        <p>{{ name }} owes ${{ amount.toFixed(2) }}</p>
                    </div>
                </div>

                <!-- FORM NEXT/PREV BUTTON -->
                <div class="button-container" v-if="currentFormStep < 6 && currentFormStep !== 3">
                    <button class="form__group-button button" @click.prevent="previousStep"
                        v-if="currentFormStep > 1">Previous</button>
                    <button class="form__group-button button" @click.prevent="nextStep">Next</button>
                </div>
            </div>

            <!-- FORM RECEIPT -->
            <div class="form__receipt" v-if="currentFormStep >= 2">
                <h1 class="form__receipt-logo">Receipt</h1>

                <div v-for="item in receiptItems" :key="item.itemName">
                    <div style="font-weight: bold;" class="form__receipt-item">{{ item.itemName }} - ${{ item.itemCost.toFixed(2) }}</div>
                    <ul class="form__receipt-buyers" v-if="item.buyers.length > 0" style="margin-left: 20px; list-style-type: circle;">
                        <li class="form__receipt-buyer" v-for="buyer in item.buyers" :key="buyer">{{ buyer }}</li>
                    </ul>
                </div>

                <div class="form__receipt-summary" v-if="currentFormStep === 6 || currentFormStep === 5">
                    <hr style="margin: 10px 0;">
                    <div class="form__receipt-subtotal">Subtotal: ${{ receiptTotals.subtotal.toFixed(2) }}</div>
                    <div class="form__receipt-tip">Tip: ${{ receiptTotals.tip.toFixed(2) }}</div>
                    <div class="form__receipt-tax">Tax: ${{ receiptTotals.tax.toFixed(2) }}</div>
                    <div class="form__receipt-total" style="font-weight: bold;">Total: ${{ receiptTotals.total.toFixed(2) }}</div>
                </div>
                <div class="button-container">
                            <button class="form__group-button button" @click.prevent="submitForm">Next</button>
                        </div>
            </div>



        </section>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    // name: 'DesignView',
    data() {
        return {
            currentFormStep: 1,
            currentNameIndex: 0,
            newName: '',
            newItemName: '',
            newItemCost: undefined,
            formData: {
                names: ['Charlie', 'Isaac', 'Jason', 'Tobin'],
                items: [{ itemName: "Apples", itemCost: 11.00 }, { itemName: "Banana", itemCost: 15.00 },
                { itemName: "Cherry", itemCost: 4.50 }, { itemName: "Drink", itemCost: 3.25 }
                ],
                purchases:
                {
                },
                tax: undefined,
                tip: undefined,
                fees: 0
                // splitTipAndTax: false
            }
        }
    },
    computed: {
        
        // In "FORM NAME TO ITEM INPUT," keeps track of the current person being processed.
        currentName() {
            return this.formData.names[this.currentNameIndex];
        },

        // Ccalculates how much each person owes for all the items they are currently assigned to.
        amountsOwed() {
            const totals = {};
            const subtotal = this.formData.items.reduce((sum, item) => sum + item.itemCost, 0); // Calculates subtotal.

            // Calculate tip and tax percentages based on the subtotal
            const tipPercent = this.formData.tip / subtotal || 0;
            const taxPercent = this.formData.tax / subtotal || 0;

            // Calculate amounts owed per item
            for (const itemName in this.formData.purchases) {
                const buyers = this.formData.purchases[itemName];
                const itemCost = this.formData.items.find(i => i.itemName === itemName).itemCost; // Finds cost of the item in formData.purchases through formData.items

                const costPerPerson = itemCost / buyers.length;
                const tipPerPerson = costPerPerson * tipPercent;
                const taxPerPerson = costPerPerson * taxPercent;

                buyers.forEach(buyer => { // For each person who bought this particular item

                    // Take how much they already owe, and add this new item to their balance.
                    totals[buyer] = (totals[buyer] || 0) + costPerPerson + tipPerPerson + taxPerPerson;
                });
            }

            // Add fees proportionally if not split on each item (this should be the default behavior)
            // if (!this.formData.splitTipAndTax) {
            //     for (const name in totals) {
            //         const proportion = totals[name] / subtotal;
            //         totals[name] += this.formData.fees * proportion;
            //     }
            // }

            // Round to the nearest cent
            for (const name in totals) {
                totals[name] = Math.round(totals[name] * 100) / 100;
            }

            return totals;
        },

        // Fetches the items in formData.purchases with their associated name, cost, and buyers for real-time display.
        receiptItems() {
            const items = this.formData.items.map(item => ({
                itemName: item.itemName,
                itemCost: item.itemCost,
                buyers: this.formData.purchases[item.itemName] || []
            }));
            return items;
        },

        // Fetches the subtotal, tip, tax, and full total values for real-time display.
        receiptTotals() {
            const subtotal = this.formData.items.reduce((sum, item) => sum + item.itemCost, 0);
            return {
                subtotal: subtotal,
                tip: parseFloat(this.formData.tip) || 0,
                tax: parseFloat(this.formData.tax) || 0,
                total: subtotal + (parseFloat(this.formData.tip) || 0) + (parseFloat(this.formData.tax) || 0)
            };
        },

        // Checks if all items are assigned to at least one person.
        unassignedItems() { // Step 4
            return this.formData.items.filter(item => !this.formData.purchases[item.itemName]?.length);
        }
    },
    methods: {

        // Moves the form to the next phase.
        nextStep() { 
            this.currentFormStep++;
        },

        // Moves the form to the previous phase. 
        previousStep() {
            if (this.currentFormStep > 1) {
                this.currentFormStep--;

                // Reset currentNameIndex if returning to step 3
                // TODO: When entering currentFormStep === 3 with Previous,
                // formData.purchases should be entered backwards.
                if (this.currentFormStep === 3) {
                    this.currentNameIndex = 0;
                }
            }
        },

        // While in currentFormStep === 3, Move to the next person that needs items assigned.
        nextPerson() {
            if (this.currentNameIndex < this.formData.names.length - 1) { // Normal Functionality
                this.currentNameIndex++;
            } else if (this.unassignedItems.length === 0) { // Go to the Tip/Tax Section if all items are assigned.
                this.currentFormStep = 5;
            } else { // Go to "UNASSIGNED ITEM FALLBACK" if there are unassigned items.
                this.currentFormStep++;
                this.currentNameIndex = 0;
            }

            // Restore checkbox states based on purchases
            this.formData.items.forEach(item => {

                // Checks if this.currentName is in the currently looped item.
                item.selected = this.formData.purchases[item.itemName]?.includes(this.currentName) || false;
            });
        },

        // While in currentFormStep === 3, Move to the previous person that items were assigned to.
        previousPerson() {
            if (this.currentNameIndex > 0) { // Default behavior
                this.currentNameIndex--;

                // Restore checkbox states based on purchases
                this.formData.items.forEach(item => {
                    item.selected = this.formData.purchases[item.itemName]?.includes(this.currentName) || false;
                });
            } else { // Handling the very first next person button to navigate back to "FORM ITEM INPUT".
                this.currentFormStep--;
            }
        },

        // Adds a new name into formData.names
        addName() {
            if (this.newName.trim() !== '') {
                this.formData.names.push(this.newName); // Push data into names list
                this.newName = ''; // Clear the input field
            }
        },

        // Adds a new item into formData.items
        addItem() {
            if (this.newItemName.trim() !== '' && this.newItemCost >= 0) {
                this.formData.items.push({
                    itemName: this.newItemName,
                    itemCost: this.newItemCost
                });
                this.newItemName = '';
                this.newItemCost = 0;
            } else {
                alert("Please enter a valid item name and cost.");
            }
        },

        // Maintains formData.purchases by adding/removing people based on changes to "FORM NAME TO ITEM INPUT"
        updatePurchases(item, name) {
            const purchases = this.formData.purchases;
            if (!purchases[item.itemName]) {
                purchases[item.itemName] = [];
            }
            const index = purchases[item.itemName].indexOf(name); // Index of the name who bought the currently looped item.
            item.selected ? purchases[item.itemName].push(name) : purchases[item.itemName].splice(index, 1);
        },

        // Deletes a name from formData.name
        deleteName(index) {
            this.formData.names.splice(index, 1);
        },

        // Deletes an item from formData.item
        deleteItem(index) {
            this.formData.items.splice(index, 1);
        },

        submitForm() {
            // Handle form submission
            const formDataJson = JSON.stringify(this.formData);
            axios.post('/process_form', formDataJson) // Fast API already expects JSON data by default
                .then(response => {
                    // THE NEWLY UPDATED JSON SHOULD BE ACCESSIBLE HERE AFTER POST REQUEST
                    // Something like response.data.message?? 
                    console.log('SUBMITTED YUHH');
                    console.log(response.data);
                    this.processedData = response.data;
                })
                .catch(error => {
                    console.log('NOT SUUBMITTED');
                    console.error(error);
                });
                console.log("UHHHH");
        }
    }
}
</script>

<style>
button {
    padding: .75rem 1rem;
    border-radius: 8px;
    font-weight: var(--font-medium);
}

/* Acts as a "main" */
.design {
    /* overflow: hidden; */
}

form__box {
    display: flex;
    justify-content: flex-end;
}

.form__box-button {
    background-color: var(--first-color);
    color: var(--white-color);
    font-size: var(--small-font-size);
    transition: background-color 0.4s;
}

.form__box-button:hover {
    cursor: pointer;
    background-color: var(--first-color-alt);
}

.form__container {
    background-color: transparent;
    grid-template-columns: 2fr 1fr;
    height: 100%;
    display: flex;
    align-items: center;
    flex: 0 0 50%;
}

.form__group-button {
    color: var(--white-color);
    padding: .75rem 1rem;
    background-color: var(--first-color);
    transition: opacity 0.3s ease-in-out, background-color .3s;
    margin-top: 1rem;
}

.form__group-button:hover {
    cursor: pointer;
    background-color: var(--first-color-alt);
}

.form__screen {
    grid-column: 1;
    background-color: transparent;
    flex-grow: 2;
}

.form__receipt {
    flex-grow: 1;
    grid-column: 2;
    background-color: var(--white-color);
    border-radius: 8px;
    border: 1px solid var(--gray-color);
    box-shadow: 2px 2px 5px var(--shadow-color);
    /* Adjust the values here */
}

.form__item {
    width: 70%;
    border-radius: 8px;
    border: 1px solid var(--gray-color);
    padding: .75rem 1rem;
    /* margin: .5rem; */
    font-size: var(--small-font-size);
}

.form__item-name {
    width: 40%;
}

.form__item-cost {
    width: 40%;
}

.form__label {
    display: flex;
    font-size: var(--h1-font-size);
    margin-bottom: 1rem;
}

.form__label-name {
    margin-left: 1rem;
    margin-right: 1rem;
}

.form__list {
    display: flex;
    justify-content: space-evenly;
    flex-wrap: wrap;
    gap: 1rem;
    /* Vertical Gap */
    /* width: 100%; */
}

/* @keyframes shake {
    0% {
        transform: translateX(0);
    }

    10%,
    90% {
        transform: translateX(-2px);
    }

    20%,
    80% {
        transform: translateX(4px);
    }

    30%,
    50%,
    70% {
        transform: translateX(-8px);
    }

    40%,
    60% {
        transform: translateX(8px);
    }
} */

.form__list-names {
    flex: 0 0 auto;
    background-color: var(--black-color);
    color: var(--white-color);
    border-radius: 10px;
    padding: .75rem 1rem;
    transition: opacity 0.3s ease-in-out, background-color .3s;
    font-size: var(--small-font-size);
    font-weight: var(--font-medium);
}

.form__list-names:hover {
    /* animation: shake 0.5s; */
    opacity: 0.5;
    cursor: pointer;
}

.form__box .form__item {
    margin-right: 1.5rem;
}

label {
    padding: .5rem 1rem;
    border-radius: 8px;
    background-color: var(--black-color);
    color: var(--white-color);
    cursor: pointer;
    appearance: none;
}

/* Hide the default checkbox */
.checkbox__input {
    position: absolute;
    opacity: 0;
    width: 0;
    height: 0;
}

.checkbox__label:hover {
    background-color: var(--gray-color);
}

.checkbox__input:checked+.label__text {
    background-color: var(--first-color);
}
</style>