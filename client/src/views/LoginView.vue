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

    <div class="login">
      <h1>Login</h1>
    </div>
  </template>
  
  <script>

  
  export default {
    name: 'LoginView'
    
  }
  </script>
  