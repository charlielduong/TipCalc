<template>
    <div>
        <h1>IN TEMPLATE</h1>

        <h2>Upload Image</h2>
        <input type="file" @change="onFileChange">

        <button @click="submitImage">Submit</button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            imageFile: null
        }
    },
    methods: {
        onFileChange(e) {
            this.imageFile = e.target.files[0];
        },
        submitImage() {
            // Get the base URL of the server

            if (!this.imageFile) {
                console.error("No file selected");
                return;
            }
            let formData = new FormData();
            formData.append("file", this.imageFile);

            // Send the POST request to the server
            fetch(`http://localhost:5000/receipt`, {
                method: "POST",
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                console.log("Server response", data);
            })
            .catch(error => {
                console.error("Error:", error);
            });
        }
    }
}
</script>

<style>
/* Add your styles here */
</style>
