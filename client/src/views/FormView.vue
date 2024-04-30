<template>
  <div class="form">

    <Form class="main-form"/>

  </div>
</template>


<script>
import Form from '@/components/FormItem.vue'

export default {
  name: 'FormView',
  components: {
    Form
  }
}
</script>

<style>

html,
body {
  min-height: 100%;
  background-color: #D9D9D9;
}

#app {
  display: flex;
  flex-direction: column;
  min-height: 100%;
}

.main-form {
  justify-content: center; /* Centers horizontally */
}
.footer {
  margin-top: 1rem;
  /* Push footer to the bottom */
}

.bg-light {
  background-color: #D9D9D9;
}
</style>