<template>
    <div class="add-book">
      <h1>Dodaj nową książkę</h1>
      <form @submit.prevent="addBook">
        <div class="form-group">
          <label for="title">Tytuł:</label>
          <input type="text" id="title" v-model="newBook.title" placeholder="Wprowadź tytuł książki" required>
        </div>
        <div class="form-group">
          <label for="author">Autor:</label>
          <input type="text" id="author" v-model="newBook.author" placeholder="Wprowadź autora książki" required>
        </div>
        <div class="form-group">
          <label for="isbn">ISBN:</label>
          <input type="text" id="isbn" v-model="newBook.isbn" placeholder="Wprowadź ISBN książki" required>
        </div>
        <div class="form-group">
          <label for="publishedYear">Rok publikacji:</label>
          <input type="number" id="publishedYear" v-model="newBook.publishedYear" placeholder="Wprowadź rok publikacji" required>
        </div>
        <div class="form-group">
          <label for="description">Opis:</label>
          <textarea id="description" v-model="newBook.description" placeholder="Wprowadź opis książki" required></textarea>
        </div>
        <button type="submit">Dodaj książkę</button>
      </form>
    </div>
  </template>
  <script>
  export default {
    data() {
      return {
        newBook: {
          title: "",
          author: "",
          isbn: "",
          publishedYear: null,
          description: ""
        }
      };
    },
    methods: {
      async addBook() {
        try {
          // Wywołanie API do dodania nowej książki
          await axios.post('/api/books', this.newBook);
          
          // Po dodaniu książki przekieruj użytkownika na stronę listy książek
          this.$router.push('/books');
        } catch (error) {
          console.error('Wystąpił błąd podczas dodawania książki:', error);
        }
      }
    }
  };
  </script>
  <style scoped>
  .add-book {
    max-width: 600px;
    margin: 0 auto;
  }
  
  .form-group {
    margin-bottom: 20px;
  }
  
  label {
    display: block;
    font-weight: bold;
  }
  
  input[type="text"],
  input[type="number"],
  textarea {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  button {
    padding: 8px 16px;
    border: none;
    border-radius: 4px;
    background-color: #007bff;
    color: #fff;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  </style>