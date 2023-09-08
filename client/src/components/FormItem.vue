<template>
    <div class="form-container">
        <form @submit.prevent="submitForm" v-if="showFirstForm">
            <label for="numberOfPeople">Number of people splitting the bill</label>

            <!-- Start form -->
            <input type="number" id="numberOfPeople" v-model="numberOfPeople" min="1" max="20" required>

            <template v-if="numberOfPeople">
                <div v-for="index in numberOfPeople" :key="index">
                    <label>Person {{ index }} name:</label>
                    <input type="text" v-model="listOfPeople[index - 1].name" placeholder="Enter person's name" required>
                </div>

            </template>

            <button type="button" @click="resetForm">Reset</button>
            <button type="submit">Next</button>
        </form>

        <form @submit.prevent="submitForm" v-if="showSecondForm">
            <h2>Second Form</h2>

            <div>
                <!-- Fields to add a new item -->
                <input v-model="newItemName" placeholder="Enter item name" />
                <input type="number" v-model.number="newItemCost" placeholder="Enter item cost" />

                <div v-for="index in items" :key="index">
                    <label>{{ index }}</label>
                </div>
                <button type="button" @click="addItem">Add Item</button>
                
                <button @click="submitForm">Done</button>
            </div>
        </form>

        <!-- <form @submit.prevent="submitForm" v-if="showThirdForm">

            <h2>Third Form</h2>
            <div>
                <ul>
                    <li v-for="(string, index) in stringList" :key="index">{{ string }}</li>
                </ul>
            </div>

            <button type="submit">Submit</button>
        </form> -->

        <form @submit.prevent="submitForm" v-if="showThirdForm">
            <h2>Third Form</h2>

            <div class="draggable-container">
                <!-- Items Area (Left Side) -->
                <draggable v-model="items" :group="{ name: 'items', pull: 'clone', put: false }" tag="ul" class="items">
                    <template #item="{ element }">
                        <li class="draggable-item">{{ element.name }} - ${{ element.cost.toFixed(2) }}</li>
                    </template>
                </draggable>
                
                <!-- People Area (Right Side) -->
                <div class="people-container">
                    <div v-for="(person, index) in listOfPeople" :key="index" class="person-drop-zone" @drop.prevent="handleDrop($event, person)" @dragover.prevent>
                        <p>{{ person.name }}</p>
                        <ul>
                            <li v-for="item in person.items" :key="item.id">{{ item.name }} - ${{ item.cost.toFixed(2) }}</li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <button type="submit">Submit</button>
        </form>

        <!-- <form @submit.prevent="submitForm" v-if="showThirdForm">
                <h2>Third Form</h2>
                <label>Tip %: </label>
                <input type="number" step="0.01" v-model="tip" required>
                <label>Tax %: </label>
                <input type="number" step="0.01" v-model="tax" required>

                <button type="submit">Submit</button>
            </form> -->

        <div v-if="!showFirstForm && !showSecondForm && !showThirdForm">
            <h3>Summary</h3>

            <div v-for="(person, index) in combinedLists" :key="index">
                <p>{{ combinedLists[index][0] }} owes ${{ this.calculateTipTax(combinedLists[index][1]) }}</p>
            </div>
            <p></p>
            <p>Sub-Total: {{ this.calculateSubTotal }}</p>
            <p>Tip: {{ this.calculateTip }}</p>
            <p>Tax: {{ this.calculateTax }}</p>
            <p>Total: {{ this.calculateTotal }}</p>

            <div id="showScroll" class="container">
                <div class="receipt">
                    <h1 class="logo">I PAID FOR MY FRIENDS</h1>
                    <div class="address">
                        2920 District Ave, Fairfax VA
                    </div>
                    <div class="transactionDetails">
                        Helped by: Duong
                    </div>
                    <div class="centerItem bold">
                        <div class="item">Hong&Duong Card #: *********1875</div>
                    </div>
                    <div class="transactionDetails">
                        <div class="detail">1</div>
                        <div class="detail">ITEM ONE</div>
                        <div class="detail">3.99</div>
                    </div>
                    <div class="transactionDetails">
                        <div class="detail">2</div>
                        <div class="detail">ITEM TWO BUT WITH A REALLY LONG NAME</div>
                        <div class="detail">7.49</div>
                    </div>
                    <div class="transactionDetails">
                        <div class="detail">1</div>
                        <div class="detail">ITEM NUMBER THREE</div>
                        <div class="detail">5.00</div>
                    </div>
                    <div class="paymentDetails bold">
                        <div class="detail">SUBTOTAL</div>
                        <div class="detail">3.99</div>
                    </div>
                    <div class="paymentDetails">
                        <div class="detail">TIP</div>
                        <div class="detail">3.99</div>
                    </div>
                    <div class="paymentDetails">
                        <div class="detail">TAX</div>
                        <div class="detail">3.99</div>
                    </div>
                    <div class="paymentDetails bold">
                        <div class="detail">TOTAL</div>
                        <div class="detail">3.99</div>
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>

<style>
.form-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #fff;
}

form {
    display: flex;
    flex-direction: column;
    max-width: 400px;
    width: 100%;
    padding: 20px;
    border: 1px solid #000;
}

.form-field {
    margin-bottom: 10px;
}

label {
    font-size: 14px;
    color: #000;
}

.form-input {
    border: none;
    background-color: transparent;
    border-bottom: 1px solid #000;
    padding: 5px 0;
    font-size: 16px;
    color: #000;
    width: 100%;
}

.form-input:focus {
    outline: none;
    border-bottom: 1px solid #000;
}

.draggable-container {
    display: flex;
    gap: 20px;
}

.items {
    flex: 1;
    min-height: 200px;
    border: 1px solid #ccc;
    padding: 10px;
    box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.2);
}

.draggable-item {
    margin: 5px 0;
    padding: 5px;
    cursor: pointer;
}

.people-container {
    flex: 1;
}

.person-drop-zone {
    border: 1px dashed #ccc;
    margin: 5px 0;
    padding: 10px;
    box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.2);
    min-height: 100px;
    position: relative;
}
</style>

<script>
import draggable from 'vuedraggable';  // Import the vuedraggable component here
import { Person } from './People.js';
import Item from './Item.js';

export default {
    name: 'DragDropForm',
    components: {
        draggable  // Use the imported component here
    },
    data() {
        return {
        draggablePeople: [],
        listOfPeople: [],
        stringList: [],
        numberOfPeople: null,
        listOfAmounts: [],
        showFirstForm: true,
        showSecondForm: false,
        showThirdForm: false,
        tip: 0,
        tax: 0,
        newString: '',
        newItemName: '',  // For the name of the new item
        newItemCost: 0,   // For the cost of the new item
        items: [],
        };
    },
    watch: {
        numberOfPeople(newVal, oldVal) {
        if (newVal > oldVal) {
            for (let i = oldVal; i < newVal; i++) {
            this.listOfPeople.push({ name: '' });
            }
        } else {
            this.listOfPeople = this.listOfPeople.slice(0, newVal);
        }
        }
    },
    computed: {
        calculateSubTotal() {
            return this.listOfAmounts.reduce((sum, num) => sum + num, 0)
        },
        calculateTotal() {
            return (this.calculateSubTotal + (this.calculateSubTotal * (this.tip * .01)) + (this.calculateSubTotal * (this.tax * .01))).toFixed(2).padEnd(4, '0')
        },
        calculateTip() {
            return (this.calculateSubTotal * (this.tip * .01)).toFixed(2).padEnd(4, '0')
        },
        calculateTax() {
            return (this.calculateSubTotal * (this.tax * .01)).toFixed(2).padEnd(4, '0')
            //Used to wrap this w/ Number(return statement) to return this as a number instead of string
        },
        combinedLists() {
            return this.listOfPeople.map((person, index) => [person, this.listOfAmounts[index]])
        }
    },
    methods: {
        submitForm() {
            if (this.showSecondForm) {
                console.log(this.items)
                this.showSecondForm = false;
                this.showThirdForm = true;
            } else if (this.showThirdForm) {
                console.log(this.tip)
                console.log(this.tax)
                this.showThirdForm = false

            } else {
                console.log(this.listOfPeople)
                this.showFirstForm = false;
                this.showSecondForm = true;
            }
        },
        calculateTipTax(itemAmount) {
            let output = itemAmount + (itemAmount * (this.tip * .01)) + (itemAmount * (this.tax * .01))
            return output.toFixed(2).padEnd(4, '0')
        },
        resetForm(){
            this.numberOfPeople = null;
            this.listOfPeople = [];
        },
        addItem() {
            if (this.newItemName.trim() !== '') {
                const newItem = new Item(this.newItemName, this.newItemCost);
                this.items.push(newItem);
                console.log(this.items);
                this.newItemName = '';
                this.newItemCost = 0;
            }
        },
        handleDrop(event, person) {
        const itemData = (event.dataTransfer.getData("Text"));
        console.log(person.name + " got " + itemData);
        person.items.push(itemData);
        }
    }
}

</script>