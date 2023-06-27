<template>
    <div class="form-container">
        <form @submit.prevent="submitForm" v-if="!showSecondForm">
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
            <button type="submit">Submit</button>
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
            showSecondForm: false
        }
    },
    methods: {
        submitForm() {
        
            if(!this.showSecondForm){
                console.log(this.listOfPeople)   
            }else{
                console.log(this.listOfAmounts)
            }
            this.showSecondForm = true 
        }
    }

}

</script>