<template>
    <div class="receipt">
        <h1>receipt</h1>
        <Receipt />
    </div>
</template>
  

<script>
import Receipt from '@/components/ReceiptItem.vue'

export default {
  name: 'ReceiptView',
  components: {
    Receipt
  }
}
</script>