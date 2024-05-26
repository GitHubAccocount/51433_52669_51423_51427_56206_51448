<template>
    <div class="admin-users">
      <h1>Zarządzaj użytkownikami</h1>
      <div class="user-list card">
        <table>
          <thead>
            <tr>
              <th>Imię i nazwisko</th>
              <th>Email</th>
              <th>Akcje</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="user in users" :key="user.id">
              <td>{{ user.name }}</td>
              <td>{{ user.email }}</td>
              <td>
                <button @click="editUser(user)">Edytuj</button>
                <button @click="deleteUser(user.id)">Usuń</button>
              </td>
            </tr>
          </tbody>
        </table>
        <button @click="addUser">Dodaj użytkownika</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AdminUsers',
    data() {
      return {
        users: [
          { id: 1, name: 'Jan Kowalski', email: 'jan.kowalski@example.com' },
          { id: 2, name: 'Anna Nowak', email: 'anna.nowak@example.com' },
        ],
      };
    },
    methods: {
      addUser() {
        const newUser = { id: Date.now(), name: 'Nowy użytkownik', email: 'nowy.uzytkownik@example.com' };
        this.users.push(newUser);
      },
      editUser(user) {
        // Logika edytowania użytkownika (można dodać modal lub formularz)
        alert(`Edytowanie użytkownika: ${user.name}`);
      },
      deleteUser(userId) {
        this.users = this.users.filter(user => user.id !== userId);
      },
    },
  };
  </script>
  
  <style scoped>
  .admin-users {
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
  </style>
  