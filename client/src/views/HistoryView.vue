<template>
    <div class="history">
      <h1>History</h1>
    </div>
    <div class = "receiptHistory" id = "receipts">
        <div class="columns">
          <div class="column" v-for="(item, index) in items" :key="index" :href="item.url">
            <div v-for="(dataItem, dataIndex) in item.data" :key="dataIndex">
              <p>{{ dataIndex }}: ${{ dataItem }}</p>
            </div>
          </div>
        </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  // @ is an alias to /src
  //import HelloWorld from '@/components/HelloWorld.vue'
  export default {
    name: 'HistoryView',
    data() {
      return {
        items: [],
      };
    },
    mounted() {
      this.fetchItems();
    },
    methods: {
      async fetchItems() {
        try {
          const response = await axios.get('http://localhost:5000/get_items');
          console.log(response.data.items);
          this.items = response.data.items;  // Store the fetched items in the data property
        } catch (error) {
          console.error('Error fetching items:', error);
        }
      }
    },
    mounted() {
      this.fetchItems();  // Fetch items when the component is mounted
    }
  };
  </script>
  <style>
  * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      scroll-behavior: smooth;
      overscroll-behavior: none;
  }
  .history{
    margin-top: 6%;
  }
  .columns {
    width: 80%;
    margin: 0 auto; /* Center the .columns container horizontally */
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    /* border: 3px dashed red; */
  }

  /* Indivdual Column's Stylings */
  .column {
    padding: 2em;
    border-radius: 0.3em;
    box-shadow: rgba(0, 0, 0, 0.16) 0px 3px 3px, rgba(255, 255, 255, 0.20) 0px 3px 6px;
    transition: 0.5s;
    border: 3px dashed green;
  }

  .column:hover {
    transform: translateY(-20px);
    /* border: 3px dashed green; */
  }
  </style>