<template>
    <div class="design">

        <section class="form section">

            <div class="form__container container grid">
                <!-- FORM__SCREEN -->
                <div class="form__screen" v-if="currentFormStep === 1">
                    <h2 class="form__label">Who owes you money?</h2>
                    <form action="" class="receipt__form" id="receipt-form" @submit.prevent>
                        <div class="form__group grid">
                            <div class="form__box">
                                <input class="form__item" type="text" placeholder="Enter Name" v-model="newName"
                                    @keyup.esc="addName">
                                <button type="button" class="form__box-button" @click="addName">Add Person</button>
                            </div>
                            <ul class="form__list">
                                <div class="form__list-names" v-for="(item, index) in formData.names" :key="index">
                                    <li class="form__list-names-{{ index }}" @click="deleteName(index)">{{ item }}</li>
                                </div>
                            </ul>
                            <!-- <ul class="form__list">
                                <li v-for="(item, index) in formData.names" :key="index" class="form__list-names"
                                    @click="deleteName(index)">
                                    {{ item }}
                                </li>
                            </ul> -->
                            <!-- <button type="button" class="form__box-button button" @click="addPerson">Add Person</button> -->
                            <button class="form__group-button button" @click.prevent="nextStep">Next</button>
                        </div>
                    </form>
                </div>

                <div class="form__screen" v-else-if="currentFormStep === 2">
                    <h2 class="form__label">What items were purchased?</h2>
                    <form action="" class="receipt__form" id="receipt-form">
                        <div class="form__group grid">
                            <div class="form__box">
                                <!-- CSS ISNT CONSISTENT WITH FIRST FORM (Fix later) -->
                                <!-- Be able to enter IF both inputs are filled (Fix later) -->
                                <input class="form__item form__item-name" type="text" placeholder="Enter Name"
                                    v-model="newItemName">
                                <input class="form__item form__item-cost" type="text" placeholder="Enter Cost"
                                    v-model.number="newItemCost">
                                <button type="button" class="form__box-button" @click="addItem">Add Item</button>
                            </div>
                            <ul class="form__list">
                                <div class="form__list-names" v-for="(item, index) in formData.items" :key="index">
                                    <li class="form__list-names-{{ index }}" @click="deleteItem(index)">{{ item.itemName
                                        }} - {{ item.itemCost }}
                                    </li>
                                </div>
                            </ul>
                            <!-- <button type="button" class="form__box-button button" @click="addPerson">Add Person</button> -->
                            <button class="form__group-button button" @click.prevent="nextStep">Next</button>
                        </div>
                    </form>
                </div>

                <div class="form__screen" v-else-if="currentFormStep === 3">
                    <form action="" class="receipt__form" id="receipt-form">
                        <template class="form__screen-container container" v-for="(name, index) in formData.names">
                            <div class="form__label">
                                <h2 class="form__label-text" v-if="index === currentNameIndex">What did </h2>
                                <div class="form__label-name form__list-names" v-if="index === currentNameIndex">{{ name
                                    }}</div>
                                <h2 class="form__screen-text" v-if="index === currentNameIndex"> purchase?</h2>
                            </div>

                            <div class="form__group" v-if="index === currentNameIndex">
                                <div class="form__list-purchases" v-for="item in formData.items">
                                    <label class="checkbox__label">
                                        <input class="checkbox__input" type="checkbox" @change="updatePurchases(item, name)" :value="item"
                                            v-model="item.selected" />
                                        <span class="label__text">{{ item.itemName }}</span>
                                    </label>
                                </div>
                            </div>
                        </template>
                        <button class="form__group-button button" @click.prevent="nextPerson">Next</button>
                    </form>
                </div>

                <div class="form__screen" v-else-if="currentFormStep === 4">
                    <h2>Enter Tip, Tax, and Other Fees</h2>
                    <form action="" class="receipt__form" id="receipt-form">
                        <div class="form__box">
                            <input class="form__item" type="text" placeholder="Enter Tip" style="display: block;" v-model="this.formData.tip" />
                            <input class="form__item" type="text" placeholder="Enter Tax" style="display: block;" v-model="this.formData.tax" />
                            <!-- <input class="form__item" type="text" placeholder="Enter Tip" v-model="newTip" /> -->
                            <!-- <button type="button" class="form__box-button" @click="addName">Add</button> -->
                        </div>
                        <button class="form__group-button button" @click.prevent="nextStep">Next</button>
                    </form>
                </div>

                <div class="form__screen" v-else-if="currentFormStep === 5">
                    <h1>Success!</h1>
                </div>

                <div class="form__screen" v-else>
                    <h2>Success!</h2>
                </div>

                <!-- FORM__RECEIPT -->
                <div class="form__receipt">
                    <h1 class="form__receipt-logo">Receipt</h1>
                </div>
            </div>


        </section>
    </div>
</template>

<script>
export default {
    // name: 'DesignView',
    data() {
        return {
            currentFormStep: 1,
            currentNameIndex: 0,
            newName: '',
            newItemName: '',
            newItemCost: undefined,
            formData: {
                names: ['Charlie','Saechaan','Nathan','Isaac'],
                items: [{ itemName: "Apples", itemCost: 20 }, { itemName: "Oranges", itemCost: 30 }],
                purchases:
                {
                },
                tax: undefined,
                tip: undefined,
                fees: 0,
            }
        }
    },
    computed: {
        currentName() {
            return this.formData.names[this.currentNameIndex] || null;
        }
    },
    methods: {
        nextStep() {
            this.currentFormStep++;
        },
        nextPerson() {
            if (this.currentNameIndex < this.formData.names.length - 1) {
                this.currentNameIndex++;
                this.formData.items.forEach(item => (item.selected = false));
            } else {
                this.currentFormStep++;
                this.currentNameIndex = 0;
                this.formData.items.forEach(item => (item.selected = false));
            }
        },
        nextName() { // SIMPLY FOR DATAANNOTATION
            this.currentNameIndex++;
            if (this.currentNameIndex >= this.formData.names.length) {
                this.currentNameIndex = 0; // Loop back to the beginning
                this.nextStep();
            }
        },
        addName() {
            if (this.newName.trim() !== '') {
                this.formData.names.push(this.newName); // Push data into names list
                this.newName = ''; // Clear the input field
            }
        },
        addItem() {
            if (this.newItemName.trim() !== '' && this.newItemCost >= 0) {
                this.formData.items.push({
                    itemName: this.newItemName,
                    itemCost: this.newItemCost
                });
                this.newItemName = '';
                this.newItemCost = 0;
            } else {
                alert("Please enter a valid item name and cost.");
            }
        },
        updatePurchases(item, name) {

            // Create the purchases index for the item if not created yet.
            if (!this.formData.purchases[item.itemName]) {
                // alert(`Creating list for ${item.itemName}`);
                this.formData.purchases[item.itemName] = [];
            }

            // Now, add or remove the data from purchases based on item.selected
            if (item.selected) {
                // alert(`Adding ${name} to the ${item.itemName} list`);
                this.formData.purchases[item.itemName].push(name);
            } else if (!item.selected) {
                // alert(`Removing ${name} from the ${item.itemName} list`);
                let index = this.formData.purchases[item.itemName].indexOf(name);
                this.formData.purchases[item.itemName].splice(index, 1);
            }
        },
        deleteName(index) {
            this.formData.names.splice(index, 1);
        },
        deleteItem(index) {
            this.formData.items.splice(index, 1);
        }
    }
}
</script>

<style>
button {
    padding: .75rem 1rem;
    border-radius: 8px;
    font-weight: var(--font-medium);
}
/* Acts as a "main" */
.design {
    overflow: hidden;
}

form__box {
    display: flex;
    justify-content: flex-end;
}
.form__box-button {
    background-color: var(--first-color);
    color: var(--white-color);
    font-size: var(--small-font-size);
    transition: background-color 0.4s;
}

.form__box-button:hover {
    cursor: pointer;
    background-color: var(--first-color-alt);
}

.form__container {
    background-color: transparent;
    grid-template-columns: 2fr 1fr;
    height: 100%;
    display: flex;
    align-items: center;
    flex: 0 0 50%;
}

.form__group-button {
    color: var(--white-color);
    padding: .75rem 1rem;
    background-color: var(--first-color);
    transition: opacity 0.3s ease-in-out, background-color .3s;
}

.form__group-button:hover {
    cursor: pointer;
    background-color: var(--first-color-alt);
}

.form__screen {
    grid-column: 1;
    background-color: transparent;
    flex-grow: 2;
}

.form__receipt{
    flex-grow: 1;
    grid-column: 2;
    background-color: var(--white-color);
    border-radius: 8px;
    border: 1px solid var(--gray-color);
    box-shadow: 2px 2px 5px var(--shadow-color); /* Adjust the values here */
}

.form__item {
    width: 70%;
    border-radius: 8px;
    border: 1px solid var(--gray-color);
    padding: .75rem 1rem;
    /* margin: .5rem; */
    font-size: var(--small-font-size);
}

.form__item-name {
    width: 40%;
}

.form__item-cost {
    width: 40%;
}

.form__label {
    display: flex;
    font-size: var(--h1-font-size);
    margin-bottom: 1rem;
}

.form__label-name {
    margin-left: 1rem;
    margin-right: 1rem;
}

.form__list {
    display: flex;
    justify-content: space-evenly;
    flex-wrap: wrap;
    gap: 1rem; /* Vertical Gap */
    /* width: 100%; */
}

/* @keyframes shake {
    0% {
        transform: translateX(0);
    }

    10%,
    90% {
        transform: translateX(-2px);
    }

    20%,
    80% {
        transform: translateX(4px);
    }

    30%,
    50%,
    70% {
        transform: translateX(-8px);
    }

    40%,
    60% {
        transform: translateX(8px);
    }
} */

.form__list-names {
    flex: 0 0 auto;
    background-color: var(--black-color);
    color: var(--white-color);
    border-radius: 10px;
    padding: .75rem 1rem;
    transition: opacity 0.3s ease-in-out, background-color .3s;
    font-size: var(--small-font-size);
    font-weight: var(--font-medium);
}

.form__list-names:hover {
    /* animation: shake 0.5s; */
    opacity: 0.5;
    cursor: pointer;
}

.form__box .form__item {
  margin-right: 1.5rem;
}

label {
    padding: .5rem 1rem;
    border-radius: 8px;
    background-color: var(--black-color);
    color: var(--white-color);
    cursor: pointer;
    appearance: none;
}

/* Hide the default checkbox */
.checkbox__input {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

.checkbox__label:hover {
    background-color: var(--gray-color);
}

.checkbox__input:checked + .label__text{
  background-color: var(--first-color);
}

/* Style the checkbox label when the checkbox is checked */
.checkbox__input:checked + .checkbox__label {
  color: #ff5733;
  font-weight: bold;
}


/* .form__main {
    width: 100%;  
    height: 70dvh;
    display: flex;
}

.form__screen {
    background-color: var(--white-color);
    flex: 65%;
    margin: 7% 12%;
    border-radius: 10px;
    border: 0.5px solid var(--text-color-lightest);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
}
.form__receipt {
    background-color: var(--white-color);
    flex: 35%;
    border-radius: 10px;
    border: 0.5px solid var(--text-color-lightest);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
} */

/* .form__screen-menu {
    width: 68%;
    height: 69%;
    background-color: var(--white-color);
    border: 0.3px solid var(--text-color-lightest);
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
} */


/* .form__receipt {
    width: 27%;
    height: 90%;
    border-radius: 10px;
    background-color: var(--white-color);
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
    margin-right: 2rem;
    display: flex;
    flex-direction: column;
}

.form__receipt-logo {
    font-size: var(--small-font-size);
    padding-top: 2rem;
    padding-bottom: 2rem;
    align-self: center;
    width: 80%;
    text-align: center;
    border-bottom: 1px solid var(--text-color-lightest);
} */
</style>