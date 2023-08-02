<template>
    <div class="form-container">
        <div v-if="currentForm === 1">
            <form @submit.prevent="submitForm"> <!-- Main form -->
                <!-- Looping through each field in the form1Fields array. -->
                <div v-for="(field, index) in form1Fields" :key="index">
                    <label :for="field.label" class="form-label">{{ field.label }}</label>
                    <!-- Printing the label (the prompt) -->

                    <!-- these template sections will print out either textarea, an input, or an input with an additional call to createInputs() -->
                    <template v-if="field.type === 'number'">
                        <input :type="field.type" :id="field.label" v-model="field.value" class="form-input"
                            @input="createInputs(1)">
                    </template>
                    <template v-else>
                        <input :type="field.type" :id="field.label" v-model="field.value" class="form-input">
                    </template>
                    <!-- END input printing section -->
                </div>
                <!-- Creating the button once the form fields are filled out -->
                <button v-if="isForm1Valid" @click="submitForm(1)">Next</button>
            </form> <!-- END Main Form -->
        </div>

        <div v-else-if="currentForm === 2">
            <div>
                <form v-if="!formSubmitted" @submit.prevent="submitForm">
                    <div v-for="(person, index) in people" :key="index">
                        <label>{{ people }}</label>
                        <input type="number" step="0.01" :value="form2Fields[index].value" @input="createInputs(2)" />
                    </div>
                    <button v-if="isForm2Valid" @click="submitForm(2)">Submit</button>
                </form>

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
import axios from 'axios';

export default {
    data() {
        return {
            currentForm: 1,
            formSubmitted: false,
            formData: null, // Initialize the form data property to null
            people: null,
            form1Fields: [
                {
                    label: 'Number of people splitting the bill',
                    type: 'number',
                    value: ''
                }
            ],
            form2Fields: [
                {
                    label: `amount spent:`,
                    type: 'text',
                    value: ''
                }
            ]

        }
    },
    computed: {
        isForm1Valid() {
            return this.form1Fields.every(field => field.value !== '')
        },
        isForm2Valid() {
            return this.form2Fields.every(field => field.value !== '')
        }
    },
    methods: {
        createInputs(formNumber) {
            const numberOfPeople = parseInt(
                this.form1Fields.find(
                    field => field.label === 'Number of people splitting the bill'
                ).value
            )
            if (formNumber === 1) {
                // Resets the form if the Num People input is empty
                if (!numberOfPeople) {
                    // Resets the form fields and people array to their initial values
                    this.form1Fields = [
                        {
                            label: 'Number of people splitting the bill',
                            type: 'number',
                            value: ''
                        }
                    ]
                    this.people = []
                    return
                }

                // Resetting the people array
                this.people = new Array(numberOfPeople).fill('')
                this.form1Fields.splice(1) // Remove any existing dynamic fields. 1 so that it doesn't remove the first question

                // Generate new form fields
                for (let i = 0; i < numberOfPeople; i++) {
                    this.form1Fields.push({
                        label: `Person ${i + 1} name`,
                        type: 'text',
                        value: ''
                    })
                }
            }
            else if (formNumber === 2) {
                // Generate new form fields
                this.people = this.peopleList()
                for (let i = 0; i < numberOfPeople; i++) {
                    this.form2Fields.push({
                        label: `total amount: `,
                        type: 'text',
                        value: ''
                    })
                }
            }
        }, //END createInputs()

        peopleList() {
            const people = [];
            this.formData.forEach(field => {
                if (field.value) {
                    people.push(field.value);
                }
            });
            return people;
        },
        submitForm(formNumber) {
            if (formNumber === 1) {

                // Set the form data property to the submitted data
                this.formData = this.form1Fields
                this.formData.shift() // Removing first item in array
                this.people = this.formData
                this.currentForm = 2;
            } else if (formNumber === 2) {
                this.formSubmitted = true;

                const formObject = { form: JSON.stringify(this.formData) };
                axios.post('http://localhost:5000/form', formObject)
                    .then(response => {
                        console.log(response)
                    })
                    .catch(error => {
                        console.log(error)
                    })
            }
        }
    }
}
</script>



