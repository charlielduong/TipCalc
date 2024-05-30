<template>

  <!-- Header / NavBar -->
  <NavBar />

  <!-- App -->
  <div id="app">
    <router-view />
  </div>

  <!-- Footer -->
  <Footer />
  
</template>

<script>
import NavBar from './components/NavBar.vue';
import Footer from './components/Footer.vue';

  export default {
    components: {
      NavBar,
      Footer
    },
    data() {
      return {

      }
    }
}
</script>
<style>
/*=============== GOOGLE FONTS ===============*/
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap');

/*=============== VARIABLES CSS ===============*/
:root {
  --header-height: 3.5rem;

  /*========== Colors ==========*/
  /*Color mode HSL(hue, saturation, lightness)*/
  /* 
      Change favorite color
      Default: hsl(255, 90%, 60%)
      Orange: hsl(14, 90%, 60%) - Blue: hsl(210, 90%, 50%)
      Pink: hsl(356, 100%, 65%) - Green: hsl(162, 90%, 40%)

      For more colors visit: https://colors.dopely.top/color-pedia
      -> Choose any color 
      -> Click on tab (Color Conversion)
      -> Copy the color mode (HSL)
  */
  --hue: 150;
  --first-color: hsl(var(--hue), 42%, 62%);
  --first-color-alt: hsl(var(--hue), 35%, 44%);
  --first-color-light: hsl(var(--hue), 56%, 70%);
  --title-color: hsl(var(--hue), 24%, 16%);
  --text-color: hsl(var(--hue), 43%, 4%);
  --text-color-light: hsl(0, 0%, 50%);
  --text-color-lightest: hsl(0, 0%, 80%);
  --white-color: hsl(0, 0%, 100%);
  --black-color: hsl(0,0%,20%);
  --gray-color: hsl(216,16%,84%);
  --medium-gray-color: hsl(0,0%,65%);
  --dark-gray-color: hsl(215,18%,34%);
  --body-color: hsl(var(--hue), 40%, 98%);
  --container-color: hsl(0, 0%, 97%);
  --shadow-color: hsla(var(--hue), 43%, 11%, .1);

  /*========== Font and typography ==========*/
  /*.5rem = 8px | 1rem = 16px ...*/
  --body-font: "Inter", sans-serif;
  --biggest-font-size: 2rem;
  --h1-font-size: 1.5rem;
  --h2-font-size: 1.25rem;
  --h3-font-size: 1rem;
  --normal-font-size: .938rem;
  --small-font-size: .883rem;
  --smaller-font-size: .75rem;
  --smallest-font-size: .7rem;

  /*========== Font weight ==========*/
  --font-regular: 400;
  --font-medium: 500;
  --font-semi-bold: 600;
  --font-bold: 700;

  /*========== z index ==========*/
  --z-tooltip: 10;
  --z-fixed: 100;
  --z-modal: 1000;
}

/*========== Responsive typography ==========*/
/* @media screen and (min-width: 1150px) {
  :root {
    --biggest-font-size: 4.5rem;
    --h1-font-size: 2.25rem;
    --h2-font-size: 1.5rem;
    --h3-font-size: 1.25rem;
    --normal-font-size: 1.125rem;
    --small-font-size: .875rem;
    --smaller-font-size: .813rem;
  }
} */

/*=============== BASE ===============*/
* {
  box-sizing: border-box;
  padding: 0;
  margin: 0;
}

html {
  scroll-behavior: smooth;
}

body,
input,
textarea,
button {
  font-family: var(--body-font);
  font-size: var(--normal-font-size);
}

body {
  background-color: var(--white-color);
  color: var(--text-color);
  transition: background-color .4s;
}

input,
button,
textarea {
  border: none;
  outline: none;
}

h1,
h2,
h3,
h4 {
  color: var(--title-color);
  font-weight: var(--font-semi-bold);
}

ul {
  list-style: none;
}

a {
  text-decoration: none;
}

img {
  display: block;
  max-width: 100%;
  height: auto;
}

/*=============== REUSABLE CSS CLASSES ===============*/
.container {
  max-width: 1120px;
  margin-inline: 1.5rem;
}

.grid {
  display: grid;
  gap: 1.5rem;
}

.section {
  padding-block: 5rem 1rem;
  height: 100vh;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.section__title {
  font-size: var(--h1-font-size);
  text-align: center;
  margin-bottom: 2rem;
}

.main {
  overflow: hidden;
}



/* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
} */

@media screen and (min-width: 1150px) {
  .container {
    margin-inline: auto;
  }

  .section {
    padding-block: 7rem 2rem;
  }

  .section__title {
    margin-bottom: 3.5rem;
  }

  .nav {
    /* height: calc(var(--header-height) + 2rem); */
    /* column-gap: 3rem; */
    margin-top: 1rem;
  }
}
</style>
