<template>
    <div class="form-container">
        <form class="first-form" @submit.prevent="submitForm" v-if="showFirstForm">
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

        <form class="second-form" @submit.prevent="submitForm" v-if="showSecondForm">
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
        <form class="third-form" @submit.prevent="submitForm" v-if="showThirdForm">
            <h2>Third Form</h2>

            <div class="items-list" v-for="index in items" :key="index">
                <label>{{ index }}</label>
            </div>

            <!-- Persons Buttons on the Right -->
            <div class="persons-buttons">
                <div v-for="(person, index) in combinedLists" :key="index">
                    <button>{{ combinedLists[index][0] }} owes ${{ this.calculateTipTax(combinedLists[index][1]) }}</button>
                </div>
            </div>

        </form>
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
    max-width: 400px;
    width: 400px;
    padding: 20px;
    border: 1px solid #000;
}

.first-form {
    flex-direction: column;
}

.second-form {
    flex-direction: column;
}

.third-form{
    flex-direction:row;
}

.items-list {
    width: 40%; /* take up remaining space */
}

.persons-buttons {
    width: 40%; /* take up remaining space */
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
        resetForm() {
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