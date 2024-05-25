<template>
    <div class="user-panel">
      <h1>Panel użytkownika</h1>
      <div class="user-info card">
        <h2><i class="fas fa-user"></i> Dane użytkownika</h2>
        <div v-if="isEditing">
          <label>
            Nazwa:
            <input type="text" v-model="editableUser.name" />
          </label>
          <label>
            Email:
            <input type="email" v-model="editableUser.email" />
          </label>
          <label>
            Telefon:
            <input type="text" v-model="editableUser.phone" />
          </label>
          <label>
            Adres:
            <input type="text" v-model="editableUser.address" />
          </label>
          <button @click="saveChanges">Zapisz</button>
          <button @click="cancelEditing">Anuluj</button>
        </div>
        <div v-else>
          <p><strong>Nazwa:</strong> {{ user.name }}</p>
          <p><strong>Email:</strong> {{ user.email }}</p>
          <p><strong>Telefon:</strong> {{ user.phone }}</p>
          <p><strong>Adres:</strong> {{ user.address }}</p>
          <button @click="editUser">Edytuj</button>
        </div>
      </div>
      <div class="current-loans card">
        <h2><i class="fas fa-book"></i> Aktualnie wypożyczone książki</h2>
        <ul>
          <li v-for="book in currentLoans" :key="book.id" :class="getNotificationClass(book)">
            {{ book.title }} - {{ book.author }}
            <span class="notification">{{ getNotificationMessage(book) }}</span>
          </li>
        </ul>
      </div>
      <div class="loan-history card">
        <h2><i class="fas fa-history"></i> Historia wypożyczeń</h2>
        <ul>
          <li v-for="book in loanHistory" :key="book.id">
            {{ book.title }} - {{ book.author }} ({{ book.returnDate }})
          </li>
        </ul>
      </div>
      <div class="reservations card">
        <h2><i class="fas fa-calendar-alt"></i> Rezerwacje</h2>
        <ul>
          <li v-for="reservation in reservations" :key="reservation.id">
            {{ reservation.title }} - {{ reservation.author }}
            <span class="reservation-info">{{ getReservationMessage(reservation) }}</span>
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'User',
    data() {
      return {
        user: {
          name: 'Jan Kowalski',
          email: 'jan.kowalski@example.com',
          phone: '123-456-789',
          address: 'Warszawa, ul. Przykładowa 1',
        },
        editableUser: {
          name: '',
          email: '',
          phone: '',
          address: '',
        },
        isEditing: false,
        currentLoans: [
          { id: 1, title: 'Wiedźmin: Ostatnie życzenie', author: 'Andrzej Sapkowski', dueDate: '2024-06-01' },
          { id: 2, title: 'Duma i uprzedzenie', author: 'Jane Austen', dueDate: '2024-06-10' },
          { id: 3, title: 'Bracia Karamazow', author: 'Fiodor Dostojewski', dueDate: '2024-05-28' },
          { id: 4, title: 'Mistrz i Małgorzata', author: 'Michaił Bułhakow', dueDate: '2024-05-25' },
          { id: 5, title: 'Solaris', author: 'Stanisław Lem', dueDate: '2024-06-20' },
        ],
        loanHistory: [
          { id: 6, title: '1984', author: 'George Orwell', returnDate: '2024-01-15' },
          { id: 7, title: 'Harry Potter i Kamień Filozoficzny', author: 'J.K. Rowling', returnDate: '2023-12-10' },
        ],
        reservations: [
          { id: 8, title: 'Gra o Tron', author: 'George R.R. Martin', positionInQueue: 1, isAvailable: false },
          { id: 9, title: 'Lalka', author: 'Bolesław Prus', positionInQueue: 3, isAvailable: false },
          { id: 10, title: 'Pan Tadeusz', author: 'Adam Mickiewicz', positionInQueue: 0, isAvailable: true },
        ],
      };
    },
    methods: {
      editUser() {
        this.isEditing = true;
        this.editableUser = { ...this.user };
      },
      saveChanges() {
        this.user = { ...this.editableUser };
        this.isEditing = false;
      },
      cancelEditing() {
        this.isEditing = false;
      },
      getNotificationClass(book) {
        const daysLeft = this.getDaysLeft(book.dueDate);
        if (daysLeft <= 7) {
          return daysLeft <= 2 ? 'urgent' : 'warning';
        }
        return '';
      },
      getNotificationMessage(book) {
        const daysLeft = this.getDaysLeft(book.dueDate);
        if (daysLeft <= 7) {
          return daysLeft <= 2 ? 'Termin oddania zbliża się!' : 'Termin oddania w ciągu tygodnia!';
        }
        return '';
      },
      getDaysLeft(dueDate) {
        const due = new Date(dueDate);
        const today = new Date();
        const timeDiff = due.getTime() - today.getTime();
        const daysDiff = Math.ceil(timeDiff / (1000 * 3600 * 24));
        return daysDiff;
      },
      getReservationMessage(reservation) {
        if (reservation.isAvailable) {
          return 'Książka jest dostępna!';
        }
        return `Jesteś ${reservation.positionInQueue}. osobą w kolejce.`;
      },
    },
  };
  </script>
  
  <style scoped>
  @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');
  
  .user-panel {
    max-width: 800px;
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
  
  .user-info p,
  .current-loans ul,
  .loan-history ul,
  .reservations ul {
    margin: 0;
    padding: 0;
  }
  
  h2 {
    margin-bottom: 15px;
    color: #333;
    font-weight: bold;
    display: flex;
    align-items: center;
  }
  
  h2 i {
    margin-right: 10px;
  }
  
  ul {
    list-style: none;
    padding-left: 0;
  }
  
  li {
    background: #fff;
    margin-bottom: 10px;
    padding: 10px;
    border-radius: 4px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  li.warning {
    background-color: #fff3cd;
  }
  
  li.urgent {
    background-color: #f8d7da;
  }
  
  .notification {
    font-weight: bold;
    color: #d9534f;
  }
  
  .reservation-info {
    font-weight: bold;
    color: #5bc0de;
  }
  
  label {
    display: block;
    margin-bottom: 10px;
    font-weight: bold;
  }
  
  input {
    width: 100%;
    padding: 8px;
    margin-top: 5px;
    box-sizing: border-box;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  button {
    margin-right: 10px;
    padding: 10px 20px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #45a049;
  }
  </style>
  