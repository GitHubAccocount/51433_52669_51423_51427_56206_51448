<template>
    <div class="edit-book">
      <h1>Edytuj książkę</h1>
      <form @submit.prevent="saveChanges">
        <div class="form-group">
          <label for="title">Tytuł:</label>
          <input type="text" id="title" v-model="editedBook.title" required>
        </div>
        <div class="form-group">
          <label for="author">Autor:</label>
          <input type="text" id="author" v-model="editedBook.author" required>
        </div>
        <div class="form-group">
          <label for="isbn">ISBN:</label>
          <input type="text" id="isbn" v-model="editedBook.isbn" required>
        </div>
        <div class="form-group">
          <label for="publishedYear">Rok publikacji:</label>
          <input type="number" id="publishedYear" v-model="editedBook.publishedYear" required>
        </div>
        <div class="form-group">
          <label for="description">Opis:</label>
          <textarea id="description" v-model="editedBook.description" required></textarea>
        </div>
        <button type="submit">Zapisz zmiany</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        editedBook: {
          title: "Example Book",
          author: "John Doe",
          isbn: "1234567890",
          publishedYear: 2020,
          description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit..."
        }
      };
    },
    methods: {
        async saveChanges() {
      try {
        // Wywołanie API do aktualizacji książki
            //await axios.put(`/api/books/${this.editedBook.id}`, this.editedBook);
        
        // Po zapisaniu zmian przekieruj użytkownika na stronę szczegółów książki
            //this.$router.push(`/book/${this.editedBook.id}`);

        this.$router.push(`/book`);

      } catch (error) {
            console.error('Wystąpił błąd podczas zapisywania zmian:', error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .edit-book {
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