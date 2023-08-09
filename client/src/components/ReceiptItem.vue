<template>
    <div>
        <h1>IN TEMPLATE</h1>

        <h2>Upload Image</h2>
        <input type="file" @change="onFileChange">
        
        <!-- Image preview -->

        <div v-if="imageSrc">
            <img :src="imageSrc" alt="Image Preview" />
        </div>
        
        <button @click="submitImage">Submit</button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            imageFile: null,
            imageSrc: null
        }
    },
    methods: {
        onFileChange(e) {
            this.imageFile = e.target.files[0];

            // Preview the uploaded image
            const reader = new FileReader();
            reader.onload = e => {
                this.imageSrc = e.target.result;
            };
            reader.readAsDataURL(this.imageFile);
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
    img {
        max-width: 300px;
        max-height: 300px;
        display: block;
        margin-top: 15px;
    }
</style>
