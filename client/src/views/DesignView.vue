<template>
    <div class="design">
        <div class="form">
            <div>Form</div>
        </div>
    </div>
  </template>
  
<script>
import 'bootstrap/dist/css/bootstrap.css';

    export default {
        name: 'DesignView',
    }
</script>

<style>

.design {
    background-color: gray;
    height: 90vh;
    display: flex;
    align-items: center;
    justify-content: center;
}

.form {
    width: 70%;
    height: 70%;
    background-color: lightgray;
}
</style>
  