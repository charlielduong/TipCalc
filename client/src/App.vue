<template>

<nav class="navbar navbar-expand-lg bg-light">
      <a class="navbar-brand" href="#">i paid for my friends</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
        aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <a class="nav-link" href="http://localhost:8080/form">home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="http://localhost:8080/history">history</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="http://localhost:8080/login">login</a>
          </li>
        </ul>
      </div>
    </nav>

  <div id="app">
    <router-view />
  </div>

  <footer class="footer py-3 bg-light">
      <div class="container">
        <span class="text-muted">support@ipaidformyfriends.com</span>
      </div>
    </footer>
</template>


<style>

/* body {
    height: 100vh;
    width: 100vw;
    display: flex;
}

body > * { 
    flex: 1;
}

body > .footer {
    align-self: flex-end;
} */

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.footer {
  position: absolute;
  right: 0;
  bottom: 0;
  left: 0;
  /* padding: 1rem; */
}

</style>
