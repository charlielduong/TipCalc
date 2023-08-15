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
            <div v-for="(person, index) in listOfPeople" :key="index">
                <label>{{ listOfPeople[index] }}'s Amount: </label>
                <input type="number" step="0.01" v-model="listOfAmounts[index]" required>
            </div>
            <button type="submit">Next</button>
        </form>

        <form @submit.prevent="submitForm" v-if="showThirdForm">
            <!-- Third form using input values from the first form -->
            <h2>Third Form</h2>
            <label>Tip %: </label>
            <input type="number" step="0.01" v-model="tip" required>
            <label>Tax %: </label>
            <input type="number" step="0.01" v-model="tax" required>

            <button type="submit">Submit</button>
        </form>

        <div v-if="!showFirstForm && !showSecondForm && !showThirdForm">
            <h3>Summary</h3>

            <div v-for="(person, index) in combinedLists" :key="index">
                <p>{{combinedLists[index][0]}} owes ${{ this.calculateTipTax(combinedLists[index][1]) }}</p>
            </div>
            <p></p>
            <p>Sub-Total: {{ this.calculateSubTotal }}</p>
            <p>Tip: {{ this.calculateTip }}</p>
            <p>Tax: {{ this.calculateTax }}</p>
            <p>Total: {{ this.calculateTotal }}</p>

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
export default {
    data() {
        return {
            numberOfPeople: null,
            listOfPeople: [],
            listOfAmounts: [],
            showFirstForm: true,
            showSecondForm: false,
            showThirdForm: false,
            tip: 0,
            tax: 0
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
        calculateTipTax(itemAmount){
            let output = itemAmount + (itemAmount * (this.tip * .01)) + (itemAmount * (this.tax * .01))
            return output.toFixed(2).padEnd(4, '0')
        }
    }

}

</script>