<template>
    <div class="admin-books">
      <h1>Zarządzaj książkami</h1>
      <div class="book-list card">
        <table>
          <thead>
            <tr>
              <th>Tytuł</th>
              <th>Autor</th>
              <th>Akcje</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="book in books" :key="book.id">
              <td>{{ book.title }}</td>
              <td>{{ book.author }}</td>
              <td>
                <button @click="editBook(book)">Edytuj</button>
                <button @click="deleteBook(book.id)">Usuń</button>
              </td>
            </tr>
          </tbody>
        </table>
        <!-- Zamiast przycisku "Dodaj książkę" używamy router-link -->
        <router-link to="/bookAdd" class="add-book-link">Dodaj książkę</router-link>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AdminBooks',
    data() {
      return {
        books: [
          { id: 1, title: 'Wiedźmin: Ostatnie życzenie', author: 'Andrzej Sapkowski' },
          { id: 2, title: 'Duma i uprzedzenie', author: 'Jane Austen' },
        ],
      };
    },
    methods: {
      addBook() {
        const newBook = { id: Date.now(), title: 'Nowa książka', author: 'Nieznany autor' };
        this.books.push(newBook);
      },
      editBook(book) {
        // Logika edytowania książki (można dodać modal lub formularz)
        alert(`Edytowanie książki: ${book.title}`);
      },
      deleteBook(bookId) {
        this.books = this.books.filter(book => book.id !== bookId);
      },
    },
  };
  </script>
  
  <style scoped>
  .admin-books {
    max-width: 1000px;
    margin: 0 auto;
    padding: 20px;
    font-family: Arial, sans-serif;
    color: #333;
  }
  
  h1 {
    text-align: center;
    color: #4CAF50;
  }
  
  .card {
    background: #f9f9f9;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  h2 {
    margin-bottom: 15px;
    color: #333;
    font-weight: bold;
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
  }
  
  th, td {
    padding: 10px;
    text-align: left;
    border-bottom: 1px solid #ddd;
  }
  
  th {
    background-color: #f2f2f2;
    font-weight: bold;
  }
  
  button {
    padding: 8px 12px;
    margin-right: 5px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #45a049;
  }
  
  button:last-child {
    margin-right: 0;
  }
  
  /* Dodany styl dla router-link */
  .add-book-link {
    display: inline-block;
    padding: 8px 12px;
    background-color: #007bff;
    color: #fff;
    text-decoration: none;
    border-radius: 4px;
    transition: background-color 0.3s;
  }
  
  .add-book-link:hover {
    background-color: #0056b3;
  }
  </style>
  