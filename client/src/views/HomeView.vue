<template>
  <div class="home">
    <section class="home section">
      <div class="home__container container grid">
        <div class="home__landing">
          <h1 class="home__landing-title">Your money back without the hassle</h1>
          <a href="/form" class="home__landing-button">Get Started</a>
        </div>
      </div>
    </section>
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

<style>
.form.section {
  display: flex;
  justify-content: center;
  align-items: center;
}

/* HOME LANDING */
.home__landing {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.home__landing-title {
  font-size: var(--biggest-font-size);
  margin-bottom: 1.5rem;
}

.home__landing-button {
  background-color: var(--first-color);
  color: var(--white-color);
  font-size: var(--small-font-size);
  border-radius: 8px;
  padding: .75rem 1rem;
  font-size: var(--h2-font-size);
  font-weight: var(--font-medium);
  transition: background-color 0.4s;

}

.home__landing-button:hover {
  cursor: pointer;
  background-color: var(--first-color-alt);
}
</style>
