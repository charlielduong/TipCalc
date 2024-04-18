<template>
  <div class="home">
    <h1>HOMEPAGE: LANDING PAGE OF SORTS</h1>
    <p>This won't be the main page, but the advertisement/landing page for people who want to learn about the product</p>
    <p>AKA, the project's marketing page for recruiters to look at. But queries for ipaidformyfriend.com will ideally route to /form</p>
  </div>
</template>

<script>
// @ is an alias to /src
//import HelloWorld from '@/components/HelloWorld.vue'
import Form from '@/components/FormItem.vue'

export default {
  name: 'HelloView',
  components: {
    Form
  }
}
</script>
