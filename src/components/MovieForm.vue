<template>
  <div>
    <h1>Add a new movie</h1>
    <form @submit.prevent="saveMovie">
      <div>
        <label for="title">Title:</label>
        <input type="text" id="title" v-model="form.title">
      </div>
      <div>
        <label for="poster">Poster:</label>
        <input type="file" id="poster" @change="onPosterChange">
      </div>
      <div>
        <label for="description">Description:</label>
        <textarea id="description" v-model="form.description"></textarea>
      </div>
      <button type="submit">Save</button>
    </form>
    <div v-if="errors.length">
      <h2>Errors:</h2>
      <ul>
        <li v-for="error in errors">{{ error }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { RouterLink } from "vue-router";
let csrf_token = ref("")
let responseMessage = ref("")
let errorMessage = ref("")
function getCsrfToken() {
    fetch('http://localhost:8080/api/v1/csrf-token')
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            csrf_token.value = data.csrf_token;
        })
}
onMounted(() => {
    getCsrfToken();
});
function saveMovie() {
    let movieForm = document.getElementById('MovieForm');
    let form_data = new FormData(movieForm);
    console.log('CSRF Token:', csrf_token.value);
    fetch("http://127.0.0.1:8080/api/v1/movies", {
        method: 'POST',
        body: form_data,
        headers: {
            'X-CSRFToken': csrf_token.value
        }
    })
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            if (data.errors && data.errors.length > 0) {
                console.log(data.errors);
                errors.value = data.errors;
            } else {
                console.log("Success");
                console.log(data);
                responseMessage.value = data.message;
                errorMessage.value = data.response;
            }
            console.log(data);
        })
        .catch(function (error) {
            console.log(error);
        });
}

</script>
