<template>

  <!-- HEADER -->
  <header class="header" id="header">
    <nav class="nav container">
      <div class="nav__logo">
        <i class="ri-cash-line nav__logo-icon"></i>
        <a href="#" class="nav__logo-label">Payback</a>
      </div>


      <div class="nav__menu" id="nav-menu">
        <ul class="nav__list">
          <li class="nav__item">
            <a href="http://localhost:8080/form" class="nav__link">Home</a>
          </li>

          <li class="nav__item">
            <a href="http://localhost:8080/history" class="nav__link">History</a>
          </li>

          <li class="nav__item">
            <a href="#" class="nav__link">Contact Us</a>
          </li>
        </ul>
      </div>
      <div class="nav__actions">
        <!-- Sign Up -->
        <a href="" class="nav__register">Sign In</a>
        <!-- Log In -->
        <a href="" class="nav__login">Log In</a>
      </div>
    </nav>
  </header>

  <div id="app">
    <router-view />
  </div>

  <!-- FOOTER -->
  <footer class="footer">
    <div class="footer__container container grid">
      <div class="footer__content grid">
        <a href="http://localhost:8080/form" class="footer__logo">Payback</a>
      </div>
    </div>
  </footer>
</template>


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
  --hue: 148;
  --first-color: hsl(var(--hue), 50%, 50%);
  --first-color-alt: hsl(var(--hue), 35%, 44%);
  --first-color-light: hsl(var(--hue), 56%, 70%);
  --title-color: hsl(var(--hue), 24%, 16%);
  --text-color: hsl(var(--hue), 43%, 4%);
  --text-color-light: hsl(0, 0%, 50%);
  --text-color-lightest: hsl(0, 0%, 80%);
  --white-color: hsl(0, 0%, 100%);
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
  --small-font-size: .813rem;
  --smaller-font-size: .75rem;

  /*========== Font weight ==========*/
  --font-regular: 400;
  --font-medium: 500;
  --font-semi-bold: 600;

  /*========== z index ==========*/
  --z-tooltip: 10;
  --z-fixed: 100;
  --z-modal: 1000;
}

/*========== Responsive typography ==========*/
@media screen and (min-width: 1150px) {
  :root {
    --biggest-font-size: 4.5rem;
    --h1-font-size: 2.25rem;
    --h2-font-size: 1.5rem;
    --h3-font-size: 1.25rem;
    --normal-font-size: 1.125rem;
    --small-font-size: .875rem;
    --smaller-font-size: .813rem;
  }
}

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
}

.section__title {
  font-size: var(--h1-font-size);
  text-align: center;
  margin-bottom: 2rem;
}

.main {
  overflow: hidden;
}

/*=============== HEADER & NAV ===============*/
.header {
  position: fixed;
  width: 100%;
  top: 0;
  left: 0;
  background-color: var(--white-color);
  z-index: var(--z-fixed);
  transition: background-color .4s, box-shadow .4s;
  border-bottom: 1px solid var(--text-color-lightest);
}

.nav {
  position: relative;
  height: var(--header-height);
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: var(--small-font-size);
  font-weight: var(--font-semi-bold);
  padding-bottom: 2em;
  padding-top: 2rem;
}

.nav__logo {
  display: flex;
  align-items: center;
  column-gap: 0.75rem;
  transition: color .4s;
  font-size: var(--h3-font-size);
}

.nav__logo-icon {
  color: var(--first-color-alt);
}

.nav__logo-label {
  color: var(--title-color)
}

.nav__menu {
  margin-right: auto;
  margin-left: 2rem;
}

.nav__list {
  display: flex;
  flex-direction: row;
  column-gap: 1.25rem;
  text-align: center;
}

.nav__link {
  color: var(--text-color-light);
  transition: color .4s;
}

.nav__link:hover {
  color: var(--first-color);
}

.nav__register,
.nav__login {
  display: inline-flex;
  align-items: center;
  /* font-size: 1.25rem; */
  cursor: pointer;
}

.nav__actions {
  display: flex;
  column-gap: 1.25rem;
}

.nav__register {
  color: var(--title-color);
  /* color: var(--white-color); */
}

.nav__login {
  color: var(--white-color);
  background-color: var(--first-color-light);
  padding: .75rem 1rem;
  border-radius: 10px;
}

/*=============== FOOTER ===============*/
.footer {
    background-color: var(--first-color);
}

.footer__container {
    padding-block: 4rem 2rem;
    text-align: center;
    row-gap: 5rem;
}

.footer__content {
  row-gap: 2rem;
}

.footer__content a,
.footer__copy {
  color: var(--white-color);
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
