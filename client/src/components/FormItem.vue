<template>
        <div class="container" style="min-height: 87vh;">
            <div class="row">
            <div class="col-12">
                <div class="card" style="width: 800px; height: 400px;">
                    <div class="card-body">
                        <form @submit.prevent="submitForm" novalidate>
                            <div v-if="currentStep === 1">
                                <h2 class="form-h2">I paid for my friends</h2>

                                <label class="form-label">Number of people splitting the
                                    bill</label>

                                <div v-if="formData.names">
                                    <div v-for="index in formData.names.length" :key="index">
                                        <label class="form-label">Person {{ index }} name:</label>
                                        <input type="text" class="form-control" v-model="formData.names[index - 1]"
                                            required>
                                    </div>
                                </div>
                                <button type="button" class="btn btn-primary" @click="removePerson">Remove
                                    Person</button>
                                <button type="button" class="btn btn-primary" @click="addPerson">Add Person</button>
                                <button type="button" class="btn btn-primary" @click="nextStep">Next</button>
                            </div>
                            <div v-else-if="currentStep === 2">
                                <h2>i paid for my friends</h2>
                                <div v-for="(item, index) in Object.entries(formData.items)" :key="index" class="mb-3">
                                    <label :for="'item_name_' + index" class="form-label">Item Name {{ index + 1
                                        }}</label>
                                    <input type="text" :id="'item_name_' + index" class="form-control"
                                        v-model="formData.items[index].itemName" required>

                                    <label :for="'item_cost_' + index" class="form-label">Item Cost</label>
                                    <input type="number" :id="'item_cost_' + index" class="form-control"
                                        v-model="formData.items[index].itemCost" required>
                                </div>
                                <button type="button" class="btn btn-primary" @click="addItem">Add Item</button>
                                <button type="button" class="btn btn-secondary" @click="prevStep">Previous</button>
                                <button type="button" class="btn btn-primary" @click="nextStep">Next</button>
                            </div>
                            <div v-else-if="currentStep === 3">
                                <h2>i paid for my friends</h2>
                                <div>
                                    <h2>{{ currentName }}</h2>
                                    <button type="button" class="btn btn-secondary" @click="prevStep">Previous</button>
                                    <div v-if="currentName != null">
                                        <div v-for="(item, itemIndex) in this.formData.items" :key="itemIndex">
                                            <input type="checkbox" :id="'item' + itemIndex" v-model="item.selected"
                                                @change="updatePurchases(item)" />
                                            <label :for="'item' + itemIndex">{{ item.itemName }}</label>
                                        </div>
                                        <button @click="nextPerson">Next Person</button>
                                    </div>
                                    <div v-else>
                                        <button type="submit" class="btn btn-success" @click="nextStep">Next</button>
                                    </div>
                                </div>

                            </div>
                            <div v-else-if="currentStep === 4">
                                <h2>i paid for my friends</h2>
                                <div class="mb-3">
                                    <label>Tax:</label>
                                    <input type="number" v-model="this.formData.tax" placeholder="Tax amount">
                                </div>

                                <!-- Input field for tip -->
                                <div class="mb-3">
                                    <label>Tip:</label>
                                    <input type="number" v-model="this.formData.tip" placeholder="Tip amount">
                                </div>

                                <!-- Input field for optional fees -->
                                <div class="mb-3">
                                    <label>Optional Fees:</label>
                                    <input type="number" v-model="this.formData.fees" placeholder="Optional fees">
                                </div>
                                <button type="submit" class="btn btn-success" @click="nextStep">Next</button>
                            </div>
                            <div v-else-if="currentStep === 5">
                                <h1>Processed Data</h1>
                                <ul>
                                    <li v-for="(value, name) in processedData" :key="name">
                                        {{ name }}: ${{ Number(value).toFixed(2) }}
                                    </li>
                                </ul>
                                <button type="submit" class="btn btn-success" @click="checkTipTaxandFees">Next</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="card">
                    <div class="card-body">
                        <div id="receipt">
                            <h2>receipt</h2>
                            <div v-if="Object.keys(formData.purchases).length !== 0">
                                <!-- Render your content here when purchases is not null or empty -->
                                <div v-for="(item, itemName) in formData.purchases" :key="itemName">
                                    {{ itemName }}
                                    <ul>
                                        <li v-for="(person, index) in item" :key="index">
                                            {{ person }}
                                        </li>
                                    </ul>
                                </div>
                                Subtotal: $ {{ subtotal }}
                            </div>
                            <div v-else>
                                <h2>No items added yet</h2>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.css';
// import BootstrapVue from 'bootstrap-vue'
// import 'bootstrap-vue/dist/bootstrap-vue.css'

export default {
    data() {
        return {
            currentStep: 1,
            currentItem: null,
            currentNameIndex: 0,
            formData: {
                names: ["Isaac", "Charlie", "Katherine"],
                items: [{ itemName: "Apples", itemCost: 20 }, { itemName: "Oranges", itemCost: 30 }],
                purchases:
                {
                },
                tax: 0,
                tip: 0,
                fees: 0,
            },
            processedData: {},

            // currentStep: 1,
            // currentItem: null,
            // currentNameIndex: 0,
            // tax: 0,
            // tip: 0,
            // fees: 0,
            // formData: {
            //     names: [''],
            //     items: [{}],
            //     purchases:
            //     {
            //     }
            // }
        };
    },
    computed: {
        currentName() {
            return this.formData.names[this.currentNameIndex] || null;
        },
        reversedData() {
            const reversedData = {};
            for (const person of this.formData.names) {
                reversedData[person] = [];
                for (const item of this.formData.items) {
                    if (this.formData.purchases[item.itemName] && this.formData.purchases[item.itemName].includes(person)) {
                        reversedData[person].push(item);
                    }
                }
            }
            return reversedData;
        },
        subtotal() {
            // Calculate subtotal by summing up itemCost for each item in formData.items
            return this.formData.items.reduce((total, item) => total + item.itemCost, 0);

        }
    },
    methods: {
        addItem() {
            this.formData.items.push({ itemName: '', itemCost: 0 });
        },
        nextStep() {
            this.currentStep++;
            console.log(this.formData.purchases)
        },
        prevStep() {
            this.currentStep--;
        },
        nextName() {
            if (this.currentName < this.items.length) {
                this.currentName += 1;
            }
        },
        addPerson() {
            this.formData.names.push("");
            this.numberOfPeople++;
        },
        removePerson() {
            this.formData.names.splice(-1, 1)
            this.numberOfPeople--;
        },
        nextPerson(event) {
            event.preventDefault();
            this.currentNameIndex = (this.currentNameIndex + 1);
            this.formData.items.forEach(item => (item.selected = false));
        },
        updatePurchases(item) {
            const itemName = item.itemName;
            const personName = this.currentName;

            if (!this.formData.purchases[itemName]) {
                this.formData.purchases[itemName] = []; // Create purchases[itemName] if it doesn't exist
            }

            const purchasesList = this.formData.purchases[itemName];
            const index = purchasesList.indexOf(personName);

            if (item.selected && index === -1) {
                purchasesList.push(personName); // Add personName to purchasesList if selected and not already present
            } else if (!item.selected && index !== -1) {
                purchasesList.splice(index, 1); // Remove personName from purchasesList if not selected and present

            }
        },
        checkTipTaxandFees() {
            console.log("tax " + this.formData.tax);
            console.log("tip: " + this.formData.tip);
            console.log("fees: " + this.formData.fees);
            console.log("purchases: " + JSON.stringify(this.formData.purchases));
        },
        isLastName() {
            return this.currentNameIndex === this.names.length - 1;
        },
        submitForm() {
            // Handle form submission
            const formDataJson = JSON.stringify(this.formData);
            axios.post('/process_form', formDataJson) // Fast API already expects JSON data by default
                .then(response => {
                    // THE NEWLY UPDATED JSON SHOULD BE ACCESSIBLE HERE AFTER POST REQUEST
                    // Something like response.data.message?? 
                    console.log('SUBMITTED YUHH')
                    console.log(response.data);
                    this.processedData = response.data;
                })
                .catch(error => {
                    console.log('NOT SUUBMITTED')
                    console.error(error);
                });
        }
    }
};
</script>

<style scoped>
.navbar {
    margin-bottom: 0;
    border-radius: 0;
}
#receipt {
    float: inherit;
    margin-top: 10%;
    outline-style: dotted;
}

.container {
    display: flex;
    justify-content: center; /* Centers horizontally */
    align-items: center; /* Centers vertically */
    min-height: 100vh;
}

.card {
    background-color: #F3F3F3;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}
</style>