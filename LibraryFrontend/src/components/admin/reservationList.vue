<template>
    <div class="reservation-list">
      <h2>{{ title }}</h2>
      <table>
        <thead>
          <tr>
            <th>Tytuł książki</th>
            <th>Użytkownik</th>
            <th v-if="isPending">Pozycja w kolejce</th>
            <th>Status</th>
            <th v-if="!isPending">Akcje</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="reservation in reservations" :key="reservation.id">
            <td>{{ reservation.bookTitle }}</td>
            <td>{{ reservation.userName }}</td>
            <td v-if="isPending">{{ reservation.positionInQueue }}</td>
            <td>{{ reservation.isAvailable ? 'Dostępna' : 'Niedostępna' }}</td>
            <td v-if="!isPending">
              <button v-if="!reservation.isAvailable" @click="confirmLoan(reservation)">Wypożycz</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ReservationList',
    props: {
      title: String,
      reservations: Array,
      isPending: Boolean
    },
    methods: {
      confirmLoan(reservation) {
        if (confirm('Czy na pewno chcesz wypożyczyć tę książkę?')) {
          // Tutaj można dodać logikę wypożyczenia książki
          console.log('Wypożyczono książkę:', reservation.bookTitle);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  /* Tutaj można dodać style dla komponentu ReservationList */
  </style>
  