<template>
    <div class="form-container">
        <form @submit.prevent="submitForm" v-if="showFirstForm">
            <label for="numberOfPeople">Number of people splitting the bill</label>

            <!-- Start form -->
            <input type="number" id="numberOfPeople" v-model="numberOfPeople" min="1" required>

            <template v-if="numberOfPeople">
                <div v-for="index in numberOfPeople" :key="index">
                    <label>Person {{ index }} name:</label>
                    <input type="text" v-model="listOfPeople[index - 1]" required>
                </div>

            </template>

            <button type="submit">Next</button>
        </form>

        <form @submit.prevent="submitForm" v-if="showSecondForm">
            <!-- Second form using input values from the first form -->
            <h2>Second Form</h2>
            <!-- <div v-for="(person, index) in listOfPeople" :key="index">
                <label>{{ listOfPeople[index] }}'s Amount: </label>
                <input type="number" step="0.01" v-model="listOfAmounts[index]" required>
            </div>
            <button type="submit">Next</button> -->
            <div>
                <input v-model="newString" placeholder="Enter a string" />
                <button type="button" @click="addItem">Add</button>
                <button @click="submitForm">Done</button>
                <ul>
                    <li v-for="(string, index) in stringList" :key="index">{{ string }}</li>
                </ul>
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

            <!-- Draggable People -->
            <div class="draggable-container">
                <draggable v-model="draggablePeople" :element="'ul'" :options="{ group: 'people', animation: 150 }">
                    <li v-for="(person, index) in listOfPeople" :key="index">{{ person }}</li>
                </draggable>
            </div>

            <!-- Droppable Items -->
            <div class="droppable-container">
                <div v-for="(item, index) in stringList" :key="index" class="droppable-item" @drop="onDrop(index)">
                    {{ item }}
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
</style>

<script>
import draggable from 'vuedraggable';  // Import the vuedraggable component here

export default {
    components: {
        draggable  // Use the imported component here
    },
    data() {
        return {
            numberOfPeople: null,
            listOfPeople: [],
            listOfAmounts: [],
            showFirstForm: true,
            showSecondForm: false,
            showThirdForm: false,
            tip: 0,
            tax: 0,
            newString: '',     // Input field bound to the new string
            stringList: [],     // List to store the entered strings
            draggablePeople: [], // List of draggable people
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
                console.log(this.listOfAmounts)
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
            if (this.newString.trim() !== '') {
                this.stringList.push(this.newString);
                this.newString = ''; // Clear the input field
            }
        },
        onDrop(index) {
            // Handle the drop event when a person is dropped onto an item
            // Here, you can associate the person with the dropped item
            // For example, you might want to update the stringList with the person's name
            this.stringList[index] = this.draggablePeople[0];
        }
    }

}

</script>