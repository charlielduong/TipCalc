<template>
    <div class="form-container">
        <form> <!-- Main form -->

            <!-- Looping through each field in the formFields array. -->
            <div v-for="(field, index) in formFields" :key="index">
                <label :for="field.label" class="form-label">{{ field.label }}</label>
                <!-- Printing the label (the prompt) -->

                <!-- these template sections will print out either textarea, an input, or an input with an additional call to createInputs() -->
                <template v-if="field.type === 'textarea'">
                    <textarea :id="field.label" v-model="field.value" class="form-input"></textarea>
                </template>
                <template v-else-if="field.type === 'number'">
                    <input :type="field.type" :id="field.label" v-model="field.value" class="form-input"
                        @input="createInputs">
                </template>
                <template v-else>
                    <input :type="field.type" :id="field.label" v-model="field.value" class="form-input">
                </template>
                <!-- END input printing section -->
            </div>

            <!-- Creating the button once the form fields are filled out -->
            <button v-if="isFormValid" @click="submitForm">Submit</button>

        </form> <!-- END Main Form -->
    </div>

    <!-- TODO: Add in Footer with social media -->
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
            formFields: [
                {
                    label: 'Number of people splitting the bill',
                    type: 'number',
                    value: ''
                }
            ],
            people: []
        }
    },
    computed: {
        isFormValid() {
            return this.formFields.every(field => field.value !== '')
        }
    },
    methods: {
        createInputs() {
            const numberOfPeople = parseInt(
                this.formFields.find(
                    field => field.label === 'Number of people splitting the bill'
                ).value
            )

            // Resets the form if the Num People input is empty
            if (!numberOfPeople) {
                // Resets the form fields and people array to their initial values
                this.formFields = [
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
            this.formFields.splice(1) // Remove any existing dynamic fields. 1 so that it doesn't remove the first question

            // Generate new form fields
            for (let i = 0; i < numberOfPeople; i++) {
                this.formFields.push({
                    label: `Person ${i + 1} name`,
                    type: 'text',
                    value: ''
                })
            }
        }, //END createInputs()
        submitForm() {
            // Handle form submission here
            console.log('Form submitted!')
            // Reset the form to its initial state
            this.formFields.forEach(field => {
                field.value = ''
            })
            this.people = []
        }
    }
}
</script>