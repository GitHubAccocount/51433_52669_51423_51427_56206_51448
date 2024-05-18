<template>
  <div class="book-details">
    <h1>{{ book.title }}</h1>
    <p>Author: {{ book.author }}</p>
    <p>ISBN: {{ book.isbn }}</p>
    <p>Published Year: {{ book.publishedYear }}</p>
    <p>Description: {{ book.description }}</p>
    <p>Genre: {{ book.genre }}</p>
    <div class="button-container">
      <router-link to="/bookEdit" class="edit-button">Edytuj</router-link>
      <button class="delete-button" @click="deleteBook">Usuń</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      book: {
        title: "Example Book",
        author: "John Doe",
        isbn: "1234567890",
        publishedYear: 2020,
        description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
        genre: "book genre"
      }
    };
  },
  methods: {
    deleteBook() {
      // Wyświetlenie potwierdzenia przed usunięciem
      if (confirm("Czy na pewno chcesz usunąć tę książkę?")) {
        // Tutaj dodaj kod usuwający książkę, np. wywołanie odpowiedniego API
        // np. this.$http.delete(`/books/${this.book.id}`)
        // Po usunięciu możesz przekierować użytkownika na inną stronę, np. listę książek
        // np. this.$router.push('/books')
      }
    }
  }
};
</script>

<style scoped>
  .book-details {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 0px 10px rgba(0, 0, 0, 0.1);
  font-size: 1rem;
  transition: background-color 0.3s;
  }

  .book-details h1 {
  font-size: 1.5rem;
  margin-bottom: 10px;
  color: #333;
  }

  .book-details p {
  font-size: 1rem;
  margin-bottom: 8px;
  color: #666;
  }

  .book-details p:first-child {
  margin-top: 0;
  }

  .book-details p:last-child {
  margin-bottom: 0;
  }

  .book-details p strong {
  font-weight: bold;
  color: #333;
  }

  .book-details .button-container {
    margin-top: 20px;
  }

  .book-details .button-container .edit-button {
    padding: 8px 16px;
    border: none;
    border-radius: 4px;
    background-color: #007bff;
    color: #fff;
    cursor: pointer;
    transition: background-color 0.3s;
  }

  .book-details .button-container .edit-button:hover {
    background-color: #0056b3;
  }

  .book-details .button-container button.delete-button {
    margin-left: 10px; /* Dodajemy odstęp między przyciskami */
    padding: 8px 16px;
    border: none;
    border-radius: 4px;
    background-color: #dc3545;
    color: #fff;
    cursor: pointer;
    transition: background-color 0.3s;
  }

  .book-details .button-container button.delete-button:hover {
    background-color: #c82333;
  }
</style>