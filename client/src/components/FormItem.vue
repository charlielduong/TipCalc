<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#">i paid for my friends</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <!-- <li class="nav-item">
            <router-link :to="{ name: 'home' }" class="nav-link">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link :to="{ name: 'history' }" class="nav-link">History</router-link>
          </li>
          <li class="nav-item">
            <router-link :to="{ name: 'about' }" class="nav-link">About</router-link>
          </li> -->
          <li class="nav-item">
                <button class="btn btn-primary">Log In</button>
            </li>
        </ul>
        <ul class="navbar-nav"> <!-- Changed position of this ul -->
            <li class="nav-item">
                <button class="btn btn-primary">Log In</button>
            </li>
        </ul>
      </div>
    </nav>

    <div class="container">
        <div class="row">
            <div class="col-md-6 offset-md-3">
                <div class="card">
                    <div class="card-body">
                        <form @submit.prevent="submitForm" novalidate>
                            <div v-if="currentStep === 1">
                                <h2>I paid for my friends</h2>
                        
                                <label for="numberOfPeople" class="form-label">Number of people splitting the
                                    bill</label>
                                <input type="number" class="form-control" id="numberOfPeople" v-model="numberOfPeople"
                                    min="1" max="20" required>

                                <div v-if="numberOfPeople">
                                    <div v-for="index in numberOfPeople" :key="index">
                                        <label class="form-label">Person {{ index }} name:</label>
                                        <input type="text" class="form-control" v-model="formData.names[index - 1]" required>
                                    </div>
                                </div>
                                <button type="button" class="btn btn-primary" @click="nextStep">Next</button>
                            </div>
                            <div v-else-if="currentStep === 2">
                                <h2>i paid for my friends</h2>
                                <div v-for="(item, index) in Object.entries(formData.items)" :key="index" class="mb-3">
                                    <label :for="'item_name_' + index" class="form-label">Item Name {{ index + 1 }}</label>
                                    <input type="text" :id="'item_name_' + index" class="form-control"
                                        v-model="formData.items[index].itemName" required>

                                    <label :for="'item_cost_' + index" class="form-label">Item Cost</label>
                                    <input type="number" :id="'item_cost_' + index" class="form-control"
                                        v-model="formData.items[index].itemCost" required>
                                </div>
                                <button type="button" class="btn btn-primary" @click="addItem">Add Item</button>
                                <button type="button" class="btn btn-secondary" @click="prevStep">Previous</button>
                                <button type="button" class="btn btn-primary" @click="nextStep">Next</button>
                            </div>
                            <div v-else>
                                <h2>i paid for my friends</h2>
                                <h3> {{ this.names }}</h3>
                                <!-- <h3>{{ this.items }}</h3> -->
                                <!-- <div class="mb-3" v-if="currentName">
                                    <label>{{ currentName.display() }}</label>

                                    <div class="item-buttons">
                                        <div v-for="item in formData.items" :key="index">
                                            <input type="checkbox" :name="`checkbox_${index}`" /> {{ item.itemName }}
                                        </div>
                                    </div>
                                </div>
                                <button v-if="!isLastItem" type="button" @click="nextName" :disabled="isLastName">Next Person</button> -->
                                <button type="button" class="btn btn-secondary" @click="prevStep">Previous</button>
                                <button type="submit" class="btn btn-success">Submit</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.css';
// import BootstrapVue from 'bootstrap-vue'
// import 'bootstrap-vue/dist/bootstrap-vue.css'

export default {
    data() {
        return {
            numberOfPeople: null,
            currentStep: 1,
            currentItem: null,
            currentNameIndex: 0,
            formData: {
                names: [''],
                items: [{ itemName: '', itemCost: 0 }],
                // purchases: {}
            }
        };
    },
    computed: {
        currentName() {
            return this.formData.names[this.currentNameIndex] || null;
        }
    },
    methods: {
        addName() {
            this.formData.names.push('');
        },
        addItem() {
            this.formData.items.push({ itemName: '', itemCost: 0 });
        },
        // addItem() {
        //     if (this.newItemName.trim() !== '') {
        //         const newItem = new Item(this.newItemName, this.newItemCost);
        //         this.items.push(newItem);
        //         console.log(this.items);
        //         this.newItemName = '';
        //         this.newItemCost = 0;
        //     }
        // },
        nextStep() {
            this.currentStep++;
        },
        prevStep() {
            this.currentStep--;
        },
        nextName() {
            if (this.currentName < this.items.length) {
                this.currentName += 1;
            }
        },
        isLastName() {
            return this.currentNameIndex === this.names.length - 1;
        },
        submitForm() {
            // Handle form submission
            console.log('Form submitted with data:', this.formData);
            // Optionally, you can reset the form data and step here
            // this.formData = {};
            // this.currentStep = 1;
        }
    }
};
</script>

<style scoped>
.navbar {
      margin-bottom: 0;
      border-radius: 0;
    }
</style>