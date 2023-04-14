<template>
    <div class="form-container">
      <form>
        <div v-for="(field, index) in formFields" :key="index">
          <label :for="field.label" class="form-label">{{ field.label }}</label>
          <template v-if="field.type === 'textarea'">
            <textarea :id="field.label" v-model="field.value" class="form-input"></textarea>
          </template>
          <template v-else-if="field.type === 'number'">
            <input :type="field.type" :id="field.label" v-model="field.value" class="form-input" @change="createInputs">
          </template>
          <template v-else>
            <input :type="field.type" :id="field.label" v-model="field.value" class="form-input">
          </template>
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
            },          
        ],
        people: []
      }
    },
    methods: {
    createInputs() {
      const numberOfPeople = parseInt(
        this.formFields.find(
          field => field.label === 'Number of people splitting the bill'
        ).value
      )
      if (isNaN(numberOfPeople) || numberOfPeople <= 0) {
        // Return early if NaN Is inputted
        return
      }
      this.people = new Array(numberOfPeople).fill('')
      this.formFields.splice(1) // Remove any existing dynamic fields
      
      // Generate new form fields
      for (let i = 0; i < numberOfPeople; i++) {
        this.formFields.push({
          label: `Person ${i + 1} name`,
          type: 'text',
          value: ''
        })
      }
    }
  }
  }
  </script>