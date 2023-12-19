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
            <!-- <div class="items-list" v-for="index in items" :key="index">
                <label>{{ index.display() }}</label>
            </div> -->
            <div class="items-list" v-if="currentItem">
                <label>{{ currentItem.display() }}</label>

                <!-- Persons Buttons on the Right -->
                <div class="name-buttons">
                    <div v-for="person in listOfPeople" :key="index">
                        <input type="checkbox" :name="`checkbox_${index}`" /> {{ person.name }}
                    </div>
                </div>
            </div>

            <!-- <button @click="nextItem" :disabled="isLastItem">Next</button> -->
            <button v-if="!isLastItem" type="button" @click="nextItem" :disabled="isLastItem">Next</button>
            <button v-else @click="submitForm">Done</button>
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

.third-form {
    flex-direction: row;
}

.items-list {
    width: 40%;
    /* take up remaining space */
}

.name-buttons {
    width: 40%;
    /* take up remaining space */
}
</style>

<script>
import { Person } from './People';
import Item from './Item.js';

export default {
    data() {
        return {
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
            mainItem: null,
            currentIndex: 0 // Loops through items in the third form
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
        },
        items: {
            immediate: true,  // This ensures the handler gets called immediately upon registration
            handler(newValue) {
                if (newValue.length > 0) {
                    this.mainItem = newValue[0];
                    (console.log(this.mainItem));
                }
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
        },
        currentItem() {
            return this.items[this.currentIndex] || null;
        },
        isLastItem() {
            return this.currentIndex === this.items.length - 1;
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
        nextItem() {
            if (this.currentIndex < this.items.length) {
                this.currentIndex += 1;
            }
        }
    }
}

</script>