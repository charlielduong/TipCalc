<template>
  <div class="history">
    <section class="history section">
      <div class="history__container container grid">
        <h1 class="history__title">Most Recent Receipts</h1>
        <div class="history__columns">
          <a v-for="(item, index) in items" :key="index" :href="item.url" class="history__column">
            <div v-for="(dataItem, dataIndex) in item.data" :key="dataIndex">
              <div>{{ dataIndex }}: {{ dataItem }}</div>
            </div>
          </a>
        </div>
      </div>
    </section>
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
        console.log('Response data:', response.data);
        this.items = response.data.items;  // Store the fetched items in the data property
      } catch (error) {
        console.error('Error fetching items:', error);
      }
    }
  },
};
</script>
<style>

.history {
  height: 100%;
}
.history__title {
  font-size: var(--biggest-font-size);
  margin-bottom: 2rem;
}

.history__container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.history__columns {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
}

.history__column {
  padding: 2rem;
  border-radius: 0.3em;
  transition: 0.5s;
  border-radius: 8px;
  border: 1px solid var(--gray-color);
  box-shadow: 2px 2px 5px var(--shadow-color);
}

.history__column:hover {
  transform: translateY(-20px);
}
</style>