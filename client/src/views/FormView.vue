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
                                        }} ${{ item.itemCost }}
                                    </li>
                                </div>
                            </ul>
                        </div>
                    </form>
                </div>

                <!-- FORM NAME TO ITEM INPUT -->
                <div class="form__screen" v-else-if="currentFormStep === 3">
                    <form action="" class="form__name-to-item">
                        <template v-for="(name, index) in formData.names">
                            <div class="form__label" v-if="index === currentNameIndex">
                                <h2 class="form__label-text">What did </h2>
                                <div class="form__label-name form__list-names">{{ name }}</div>
                                <h2 class="form__screen-text"> purchase?</h2>
                            </div>

                            <div class="form__group form__group-name-to-item" v-if="index === currentNameIndex">
                                <div class="form__list-purchases" v-for="item in formData.items">
                                    <label class="checkbox__label" :class="{ 'checked': item.selected }">
                                        <input class="checkbox__input" type="checkbox"
                                            @change="updatePurchases(item, name)" :value="item"
                                            v-model="item.selected" />
                                        <span class="label__text">{{ item.itemName }}</span>
                                    </label>
                                </div>
                            </div>
                        </template>
                        <div class="button__container">
                            <button class="form__container-button form__container-button-previous button"
                                @click.prevent="previousPerson">Previous</button>
                            <button class="form__container-button form__container-button-next button"
                                @click.prevent="nextPerson">Next</button>
                        </div>
                    </form>
                </div>

                <!-- FORM UNASSIGNED ITEM FALLBACK -->
                <!-- TODO: Currently only allows one person to be assigned. Needs to be multiple -->
                <div class="form__screen" v-else-if="currentFormStep === 4">
                    <h2 v-if="this.unassignedItems.length > 0" class="form__screen-label-warning">Warning!</h2>
                    <h3 v-if="this.unassignedItems.length > 0" class="form__screen-label-message">Some items weren't
                        accounted for.</h3>
                    <template v-for="item in unassignedItems">
                        <div class="form__label form__label-fallback">
                            <p>Who bought</p>
                            <div class="form__label-name form__list-names">{{ item.itemName }}</div>
                            <p>?</p>
                        </div>
                        <div class="form__group form__group-item-to-name">
                            <label class="checkbox__label" v-for="name in formData.names" :key="name">
                                <input class="checkbox__input" type="checkbox" @change="updatePurchases(item, name)"
                                    :value="name" v-model="item.selected" />
                                <span class="label__text">{{ name }}</span>
                            </label>
                        </div>
                    </template>
                </div>

                <!-- FORM TIP AND TAX INPUT -->
                <div class="form__screen" v-else-if="currentFormStep === 5">
                    <h2 class="form__label">Enter Tip, Tax, and Other Fees</h2>
                    <form action="" class="receipt__form" id="receipt-form">
                        <div class="form__box form__box-tip-tax">
                            <input class="form__item form__item-tip" type="text" placeholder="Enter Tip"
                                style="display: block;" v-model="this.formData.tip" />
                            <input class="form__item form__item-tax" type="text" placeholder="Enter Tax"
                                style="display: block;" v-model="this.formData.tax" />
                        </div>
                    </form>
                </div>

                <!-- FORM SUMMARY -->
                <div class="form__success" v-else="currentFormStep === 6">
                    <h1 class="form__success-title">Success!</h1>
                    <div class="form__success-buttons">
                        <i class="ri-file-copy-line form__success-button" @click="copyToClipboard"></i>
                        <i class="ri-share-box-line form__success-button"></i>
                        <a href="/"><i class="ri-close-line"></i></a>

                    </div>
                </div>

                <!-- FORM NEXT/PREV BUTTON -->
                <div class="button__container" v-if="currentFormStep < 6 && currentFormStep !== 3">
                    <button class="form__group-button form__group-button-previous button" @click.prevent="previousStep"
                        v-if="currentFormStep > 1">Previous</button>
                    <button class="form__group-button form__group-button-next button" @click.prevent="nextStep"
                        :disabled="isButtonDisabled()" :class="{ 'disabled-button': isButtonDisabled() }"
                        @mouseover="showTooltip" @mouseleave="hideTooltip">Next
                    </button>
                </div>
            </div>

            <!-- FORM RECEIPT -->
            <div class="receipt__container container">
                <div class="form__receipt" v-if="currentFormStep >= 1">
                    <h1 class="form__receipt-logo">Receipt</h1>
                    <div class="form__receipt-items">
                        <div class="form__receipt-item-entry" v-for="item in receiptItems" :key="item.itemName">
                            <div class="form__receipt-item">
                                <div class="form__receipt-item-name">{{ item.itemName }}</div>
                                <div class="form__receipt-buyers">
                                    <ul v-if="item.buyers.length > 0">
                                        <li class="form__receipt-buyer" v-for="buyer in item.buyers" :key="buyer">{{
                    buyer
                }}
                                        </li>
                                    </ul>
                                </div>

                            </div>
                            <div class="form__receipt-price">${{ item.itemCost.toFixed(2) }}</div>
                        </div>
                    </div>
                    <div class="form__owes" v-if="currentFormStep === 6">
                        <h2 class="form__owes-title">Individual Totals</h2>
                        <div class="form__owes-summary" v-for="(amount, name) in amountsOwed" :key="name">
                            <p class="form__owes-item-name">{{ name }}</p>
                            <p class="form__owes-item-cost">${{ amount.toFixed(2) }}</p>
                        </div>
                    </div>

                    <div class="form__receipt-summary">
                        <div class="form__receipt-subtotal">
                            <div class="form__receipt-subtotal-title">Subtotal</div>
                            <div class="form__Receipt-subtotal-price">${{ receiptTotals.subtotal.toFixed(2) }}</div>
                        </div>
                        <div class="form__receipt-tip-tax" v-if="currentFormStep === 5 || currentFormStep === 6">
                            <div class="form__receipt-tip">
                                <div class="form__receipt-tip-title">Tip</div>
                                <div class="form__receipt-tip-price">${{ receiptTotals.tip.toFixed(2) }}</div>
                            </div>
                            <div class="form__receipt-tax">
                                <div class="form__receipt-tax-title">Tax</div>
                                <div class="form__receipt-tax-price">${{ receiptTotals.tax.toFixed(2) }}</div>
                            </div>
                        </div>

                        <div class="form__receipt-total">
                            <div class="form_receipt-total-title">Total</div>
                            <div class="form__receipt-total-price">${{receiptTotals.total.toFixed(2) }}</div>
                        </div>
                    </div>
                    <!-- SUBMIT BUTTON TO SUBMIT THE DATA TO MONGO??? -->
                    <!-- <div class="button-container">
                        <button class="form__group-button button" @click.prevent="submitForm">Next</button>
                    </div> -->
                </div>
            </div>

        </section>
    </div>
</template>

<script>
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
            }
        }
    },
    computed: {

        // In "FORM NAME TO ITEM INPUT," keeps track of the current person being processed.
        currentName() {
            return this.formData.names[this.currentNameIndex];
        },

        // Calculates how much each person owes for all the items they are currently assigned to.
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
                if (this.currentFormStep === 3) {
                    this.currentNameIndex = 0;

                    // Restore checkbox states based on purchases
                    this.formData.items.forEach(item => {
                        item.selected = this.formData.purchases[item.itemName]?.includes(this.currentName) || false;
                    });
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

        showTooltip() {
            if (this.isButtonDisabled()) {
                this.tooltipVisible = true;
            }
        },

        hideTooltip() {
            this.tooltipVisible = false;
        },

        isButtonDisabled() {
            if (this.currentFormStep === 1) {
                return this.formData.names.length === 0;
            } else if (this.currentFormStep === 2) {
                return this.formData.items.length === 0;
            } else if (this.currentFormStep === 3) {
                // IMPLEMENT THIS
            } else if (this.currentFormStep === 4) {
                return this.unassignedItems.length > 0;
            } else if (this.currentFormStep === 5) {
                return (this.formData.tip === undefined) && (this.formData.tax === undefined);
            }
        },

        copyToClipboard() {
            let amounts = this.amountsOwed
            let textToCopy = 'Individual Totals\n'

            // Copy the amounts owed into the clipboard
            for (let person in amounts) {
                if (amounts.hasOwnProperty(person)) {
                    const name = person; // The key
                    const amount = amounts[person]; // The value
                    textToCopy += `${name} --- $${amount.toFixed(2)}\n`
                }
            }

            navigator.clipboard.writeText(textToCopy).then(() => {
                alert('Receipt data copied to clipboard!');
            }).catch(err => {
                alert('Failed to copy receipt data.', err);
            });
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
/* BUTTON */
button {
    padding: .75rem 1rem;
    border-radius: 8px;
    font-weight: var(--font-medium);
}

.button__container {
    width: 100%;
    display: flex;
    justify-content: space-between;
}

.form__group-button {
    background-color: var(--first-color);
    color: var(--white-color);
    width: 48%;
    transition: background-color 0.4s;
}

.form__group-button:hover {
    cursor: pointer;
    background-color: var(--first-color-alt);

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

.form__container-button {
    color: var(--white-color);
    padding: .75rem 1rem;
    background-color: var(--first-color);
    transition: background-color .4s;
    margin-top: 1rem;
    width: 48%;
}

.form__container-button:hover {
    cursor: pointer;
    background-color: var(--first-color-alt);
}

.form__container-button-previous {
    background-color: var(--medium-gray-color);
}

.form__container-button-previous:hover {
    background-color: hsl(0, 0%, 45%);
}

.form__group-button-previous {
    background-color: var(--medium-gray-color);
}

.form__group-button-previous:hover {
    background-color: hsl(0, 0%, 45%);

}

/* Custom cursor for disabled button */
button:disabled,
button.disabled-button {
    cursor: not-allowed;
    background-color: var(--gray-color);
}

/* Tooltip styling */
.tooltip {
    display: none;
    position: absolute;
    background-color: #333;
    color: #fff;
    padding: 5px;
    border-radius: 3px;
    font-size: 12px;
    z-index: 10;
}

.tooltip-visible {
    display: block;
}

/* Acts as a "main" */
.design {
    overflow: hidden;
}

/* FORM */
.form.section {
    display: flex;
    /* justify-content: space-evenly; */
}

.form__container {
    display: flex;
    flex-direction: column;
    /* justify-content: center; */
    background-color: transparent;
    /* grid-template-columns: 2fr 1fr; */
    /* align-items: center; */
    flex-grow: 2;
    padding-left: 5rem;
    padding-right: 5rem;
}

.form__box {
    display: flex;
    justify-content: space-between;
}

/* TODO: Fix the spacing between form items (the inputs)
uncommenting fixes the spacing, but then tip/tax box doesn't space properly */
.form__box .form__item {
    /* margin: auto; */
}

.form__screen {
    background-color: transparent;
    text-align: center;
}

.form__screen-label-warning {
    font-size: var(--biggest-font-size);
}

.form__screen-label-message {
    font-weight: var(--font-regular);
    margin-bottom: 2rem;
}

.form__receipt {
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

.form__item-tip {
    width: 100%;
    margin-bottom: 2rem;
}

.form__item-tax {
    width: 100%;
}

.form__label {
    display: flex;
    font-size: var(--h1-font-size);
    margin-bottom: 1.5rem;
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
    margin-bottom: 2rem;
}

.form__group-name-to-item {
    width: 100%;
    display: flex;
    justify-content: space-evenly;
    margin-bottom: 2rem;
}

.form__group-item-to-name {
    width: 60%;
    display: flex;
    justify-content: space-evenly;
    margin-bottom: 2rem;
}

.form__list-names {
    flex: 0 0 auto;
    background-color: var(--black-color);
    color: var(--white-color);
    border-radius: 8px;
    padding: .75rem 1rem;
    transition: opacity 0.3s ease-in-out, background-color .3s;
    font-size: var(--small-font-size);
    font-weight: var(--font-medium);
}

.form__list-names:hover {
    opacity: 0.5;
    cursor: pointer;
}

.form__box-tip-tax {
    display: block;
}

.form__success {
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.form__success-title {
    display: flex;
    justify-content: center;
    font-size: var(--biggest-font-size);
    margin-bottom: .3rem;
}

.form__success-buttons {
    display: flex;
    justify-content: center;
    font-size: var(--h1-font-size);
}

.form__success-button {
    padding: .2rem;
    border-radius: 8px;
    cursor: pointer;
    border: 1px solid var(--gray-color);
    margin-left: .5rem;
    margin-right: .5rem;
    display: flex;
    justify-content: center;
    align-items: center;
    color: var(--black-color);
    transition: color 0.3s;
}

.form__success-button:hover {
    color: var(--first-color);
}

.ri-close-line {
    padding: .2rem;
    border-radius: 8px;
    cursor: pointer;
    border: 1px solid var(--gray-color);
    margin-left: .5rem;
    margin-right: .5rem;
    display: flex;
    justify-content: center;
    align-items: center;
    color: var(--black-color);
    transition: color 0.3s;
}

.ri-close-line:hover {
    color: red;
}

label {
    padding: .5rem 1rem;
    border-radius: 8px;
    background-color: var(--black-color);
    color: var(--white-color);
    cursor: pointer;
    appearance: none;
}

.label__text {
    font-weight: var(--font-medium);
}

/* RECEIPT */
.receipt__container {
    display: flex;
    flex-grow: 1;
    /* flex-direction: column; */
    justify-content: center;
    height: 80%;
    font-weight: var(--font-regular);
}

.form__receipt {
    /* padding-left: 5rem;
    padding-right: 5rem; */
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow: auto;
}

.form__receipt-items {
    height: 100%;
}

.form__receipt-price {
    font-weight: var(--font-regular);
}

.form__receipt-logo {
    padding-left: 5rem;
    padding-right: 5rem;
    margin-top: 1rem;
    margin-bottom: 2rem;
    border-bottom: 2px solid var(--gray-color);
    padding-bottom: 1rem;
}

.form__receipt-item-entry {
    display: flex;
    font-weight: var(--font-semi-bold);
    color: var(--dark-gray-color);
    justify-content: space-between;
    margin-left: 1rem;
    margin-right: 1rem;
    margin-bottom: 1rem;
}

.form__receipt-buyers {
    width: 100%;
    margin-left: 20px;
    font-weight: var(--font-regular);
    margin-top: .5rem;
    font-size: var(--smallest-font-size);
}

.form__owes {
    margin-bottom: 1rem;
}

.form__owes-title {
    display: flex;
    justify-content: center;
    margin-top: 1rem;
    /* margin-bottom: .5rem; */
    /* border-bottom: 2px solid var(--gray-color); */
    padding-bottom: 1rem;
    font-size: var(--h3-font-size);
}

.form__owes-item {
    display: flex;
    justify-content: center;
}

.form__owes-item-cost {
    font-weight: var(--font-regular);
}

.form__owes-summary {
    display: flex;
    font-weight: var(--font-semi-bold);
    color: var(--dark-gray-color);
    justify-content: space-between;
    margin-left: 1rem;
    margin-right: 1rem;
    margin-bottom: 1rem;
}

.form__receipt-total {
    font-weight: bold;
    color: var(--first-color);
    font-size: var(--h2-font-size);
    display: flex;
    justify-content: space-between;
}

.form__receipt-tax {
    display: flex;
    justify-content: space-between;
    margin-bottom: 1rem;
    color: var(--dark-gray-color);
}

.form__receipt-tip {
    display: flex;
    justify-content: space-between;
    color: var(--dark-gray-color);
}

.form__receipt-subtotal {
    font-weight: var(--font-semi-bold);
    color: var(--dark-gray-color);
    margin-bottom: .5rem;
    display: flex;
    justify-content: space-between;
}

.form__receipt-summary {
    margin: 0rem 1rem 1rem 1rem;
}

/* CHECKBOX */

.checkbox__input {
    position: absolute;
    opacity: 0;
    width: 0;
    height: 0;
}

.checkbox__label {
    cursor: pointer;
    display: inline-block;
    /* Ensure proper layout */
    padding: 1rem;
    /* Add padding for clickable area */
    transition: background-color 0.3s;
    /* Add transition for smooth color change */
}

.checkbox__label:hover {
    background-color: var(--gray-color);
}

/* Change label background color when checkbox is checked */
.checkbox__label.checked {
    background-color: var(--first-color);
}
</style>