<template>
    <div class="admin-dashboard">
      <h1>Panel administratora</h1>
      <div class="admin-summary card">
        <h2>Podsumowanie</h2>
        <p><strong>Łączna liczba użytkowników:</strong> {{ users.length }}</p>
        <p><strong>Łączna liczba książek:</strong> {{ books.length }}</p>
        <p><strong>Łączna liczba rezerwacji:</strong> {{ reservations.length }}</p>
      </div>
      <div class="available-books card">
        <h2>Książki do wypożyczenia</h2>
        <div class="book-list">
          <div v-if="availableBooks.length === 0" class="empty-books">
            Brak dostępnych książek.
          </div>
          <div v-else>
            <div v-for="book in availableBooks" :key="book.id" class="book-item">
              <div class="book-info">
                <p><strong>Tytuł książki:</strong> {{ book.title }}</p>
                <p><strong>Autor:</strong> {{ book.author }}</p>
              </div>
              <div class="action">
                <button @click="borrowBook(book)">Wypożycz</button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="reservation-section card">
        <h2>Oczekujące rezerwacje</h2>
        <div class="reservation-list">
          <div v-if="pendingReservations.length === 0" class="empty-reservations">
            Brak oczekujących rezerwacji.
          </div>
          <div v-else>
            <div v-for="reservation in pendingReservations" :key="reservation.id" class="reservation-item">
              <div class="book-info">
                <p><strong>Tytuł książki:</strong> {{ reservation.bookTitle }}</p>
                <p><strong>Użytkownik:</strong> {{ reservation.userName }}</p>
                <p><strong>Pozycja w kolejce:</strong> {{ reservation.positionInQueue }}</p>
              </div>
              <div class="status">
                <p v-if="reservation.isAvailable" class="available">Dostępna</p>
                <p v-else class="unavailable">Niedostępna</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="admin-links card">
        <h2>Panel zarządzania</h2>
        <router-link to="/adminUsers" class="admin-link">Zarządzaj użytkownikami</router-link>
        <router-link to="/adminBooks" class="admin-link">Zarządzaj książkami</router-link>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AdminDashboard',
    data() {
      return {
        users: [
          { id: 1, name: 'Jan Kowalski', email: 'jan.kowalski@example.com' },
          { id: 2, name: 'Anna Nowak', email: 'anna.nowak@example.com' },
        ],
        books: [
          { id: 1, title: 'Wiedźmin: Ostatnie życzenie', author: 'Andrzej Sapkowski', isAvailable: true },
          { id: 2, title: 'Duma i uprzedzenie', author: 'Jane Austen', isAvailable: true },
          { id: 3, title: 'Harry Potter i Kamień Filozoficzny', author: 'J.K. Rowling', isAvailable: true },
          { id: 4, title: '1984', author: 'George Orwell', isAvailable: true },
        ],
        reservations: [
          { id: 1, bookTitle: 'Gra o Tron', userName: 'Jan Kowalski', positionInQueue: 1, isAvailable: false },
          { id: 2, bookTitle: 'Lalka', userName: 'Anna Nowak', positionInQueue: 3, isAvailable: false },
          { id: 3, bookTitle: 'Pan Tadeusz', userName: 'Jan Kowalski', positionInQueue: 0, isAvailable: true },
        ],
      };
    },
    computed: {
      pendingReservations() {
        return this.reservations.filter(reservation => !reservation.isAvailable);
      },
      availableBooks() {
        return this.books.filter(book => book.isAvailable);
      },
    },
    methods: {
      borrowBook(book) {
        // Logika wypożyczania książki
        alert(`Wypożyczono książkę: ${book.title}`);
      },
    },
  };
  </script>
  
  <style scoped>
  .admin-dashboard {
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
  
  .admin-links {
    display: flex;
    flex-direction: column;
  }
  
  .admin-link {
    text-decoration: none;
    color: #4CAF50;
    font-weight: bold;
    margin-bottom: 10px;
  }
  
  .admin-link:hover {
    color: #45a049;
  }
  
  .reservation-section {
    margin-top: 20px;
  }
  
  .reservation-list {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
  }
  
  .reservation-item {
    background-color: #fff;
    padding: 15px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    display: flex;
    justify-content: space-between;
  }
  
  .book-info {
    flex: 1;
  }
  
  .status {
    margin-left: 20px;
  }
  
  .available {
    color: green;
  }
  
  .unavailable {
    color: red;
  }
  
  .empty-reservations {
    text-align: center;
    font-style: italic;
    color: #888;
  }

  .empty-books {
    text-align: center;
    font-style: italic;
    color: #888;
  }

  .available-books.card {
    margin-top: 20px;
  }

  .book-list {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
  }
  
  .book-item {
    background-color: #fff;
    padding: 15px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    display: flex;
    justify-content: space-between;
  }

  .book-info {
    flex: 1;
  }

    .action {
    margin-left: auto;
  }
    .empty-books {
    text-align: center;
    font-style: italic;
    color: #888;
  }

  </style>
  