<template>
    <div class="form-container">
        <form class="first-form" @submit.prevent="submitForm" v-if="showFirstForm">
            <label for="numberOfPeople"><p>Number of people splitting the bill</p></label>

            <!-- Start form -->
            <input type="number"
            id="numberOfPeople"
            v-model="numberOfPeople"
            min="1"
            :max="maxNumberOfPeople"
            onkeydown="return event.keyCode !== 69 && event.keyCode !== 189"
            required>

            <template v-if="numberOfPeople">
                <div v-for="index in numberOfPeople" :key="index">
                    <label>Person {{ index }} name:</label>
                    <input type="text" v-model="listOfPeople[index - 1].name" placeholder="" required>
                </div>

            </template>

            <button type="submit">Next</button>            
        </form>

        <form class="second-form" @submit.prevent="submitForm" v-if="showSecondForm">
            <h2>Second Form</h2>

            <div>
                <!-- Fields to add a new item -->
                <input v-model="newItemName" placeholder="Enter item name" />
                <input type="number" v-model.number="newItemCost" placeholder="Enter item cost" />

                <div v-for="index in items" :key="index">
                    <label>{{ index.display() }}</label>
                </div>
                <button type="button" @click="addItem">Add Item</button>

                <button @click="submitForm">Done</button>
            </div>
        </form>
        <form class="third-form" @submit.prevent="submitForm" v-if="showThirdForm">
            <div class="items-list" v-for="index in items" :key="index">
                <label>{{ index.display() }}</label>
            </div>

            <!-- Persons Buttons on the Right -->
            <div class="name-buttons">
                <div v-for="person in numberOfPeople" :key="index">
                    <button type="button" @click="addToPerson">{{ person }}</button>
                </div>
            </div>

        </form>
    </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Young+Serif&display=swap');
:root{
    --blue: #7C98B3;
    --light-blue: #ACCBE1;
    --grey: #637081;
    --black:#536B78;
    --white:#CEE5F2;
}

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Young Serif', serif;
    scroll-behavior: smooth;
    overscroll-behavior: none;
}

.form-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: var(--black);
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
    background-color: var(--blue);
    border-radius: 10px;
    box-shadow: rgba(0, 0, 0, 0.16) 0px 3px 3px, rgba(0, 0, 0, 0.20) 0px 3px 6px;
    max-height: 80vh;
    overflow-y: scroll;
}

input{
    background-color: var(--white);
    border: none;
    border-radius: 5px;
    margin: 5px;
    padding-top: 2.5px;
    padding-bottom: 2.5px;
    max-width: fit-content;
    align-self: center;
    text-align: center;
}

input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

input::placeholder{
    color: var(--black);
}
input[type=text]{
    color: var(--grey);
}

p{
    color: var(--white);
    border-bottom: solid;
    border-width: 0.5px;
}

button{
    color: var(--black);
    background-color: var(--light-blue);
    /* box-shadow: rgba(0, 0, 0, 0.16) 0px 3px 3px, rgba(0, 0, 0, 0.20) 0px 3px 6px; */
    border-color: black;
    border-style: solid;
    border-width: 0.5px;
    border-radius: 5px;
    padding: 5px;
    margin-top: 10px;
}


label{
    color: var(--white);
}

.second-form {
    flex-direction: column;
    background-color: var(--blue);
    border-radius: 10px;
    box-shadow: rgba(0, 0, 0, 0.16) 0px 3px 3px, rgba(0, 0, 0, 0.20) 0px 3px 6px;
    max-height: 80vh;
    overflow-y: scroll;
}

.third-form{
    flex-direction:row;
}

.items-list {   
    width: 40%; /* take up remaining space */
}

.name-buttons {
    width: 40%; /* take up remaining space */
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
            maxNumOfPeople: 20,
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
            mainItem: null
        };
    },
    watch: {
        numberOfPeople(newVal, oldVal) {
            if (newVal > oldVal) {
                if(newVal >= this.maxNumOfPeople){
                    newVal = this.maxNumOfPeople;
                    this.numberOfPeople = this.maxNumOfPeople;
                }
                for (let i = oldVal; i < newVal; i++) {
                    this.listOfPeople.push({ name: '' });
                }
            } else {
                this.listOfPeople = this.listOfPeople.slice(0, newVal);
            }
            
        },
        items:{
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
        addItem() {
            if (this.newItemName.trim() !== '') {
                const newItem = new Item(this.newItemName, this.newItemCost);
                this.items.push(newItem);
                this.newItemName = '';
                this.newItemCost = 0;
            }
        },
        personButton(){

        }
    }
}

</script>