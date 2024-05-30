<template>
  <div v-if="book" class="book-details-container">
    <div class="book-cover">
      <img :src="book.image" :alt="book.title" />
    </div>
    <div class="book-details">
      <div class="details-container">
        <h2>{{ book.title }}</h2>
        <p>By {{ book.author }}</p>
        <p>Year Published: {{ book.year_published }}</p>
        <p>{{ book.description }}</p>
        <p>Availability: {{ book.available }} / {{ book.total_stock }}</p>
        <div v-if="user.is_superuser === true">
          <div class="button-container">
            <button class="edit-button" @click="showUsersList">
              Wybierz wypożyczającego użytkownika:
            </button>
          </div>
          <div v-if="showUsers" class="mt-3 bg-slate-100 p-3">
            <select v-model="selectedUserEmail">
              <option value="" selected disabled>Wybierz użytkownika</option>
              <option
                v-for="user in users"
                :key="user.email"
                :value="user.email"
              >
                {{ user.email }}
              </option>
            </select>
            <button
              class="loan-button ml-5"
              @click="
                borrow_book({
                  user_email: selectedUserEmail,
                  book_id: book.id,
                })
              "
            >
              Wypożycz dla tego użytkownika
            </button>
          </div>
          <div
            class="p-3 bg-green-300 w-fit mt-4"
            v-if="borrowingStore.success_message"
          >
            <p class="text-green-800">{{ borrowingStore.success_message }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from "vue-router";
import { useBookStore } from "@/stores/book";
import { computed, onMounted, onUnmounted, ref } from "vue";
import { useUserStore } from "@/stores/user";
import { useBorrowingsStore } from "@/stores/borrowings";

const route = useRoute();
const bookStore = useBookStore();
const book = computed(() => bookStore.book);

const userStore = useUserStore();
const userEmail = userStore.user.email;
const user = computed(() => userStore.user);
const users = computed(() => userStore.users);

onMounted(async () => {
  await bookStore.FETCH_BOOK_BY_ID(route.params.id);
  await userStore.GET_USERS();
});

const borrowingStore = useBorrowingsStore();

const selectedUserEmail = ref("");
const borrow_book = async (data) => {
  borrowingStore.BORROW_BOOK(data);
};

const showUsers = ref(false);
const showUsersList = () => {
  showUsers.value = !showUsers.value;
};

onUnmounted(() => {
  borrowingStore.success_message = "";
});
</script>

<style scoped>
.book-details-container {
  display: flex;
  justify-content: center;
  padding: 20px;
  background-color: #f9f9f9;
  gap: 20px;
}

.book-cover {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.cover-placeholder {
  max-width: 100%;
  max-height: 400px;
  object-fit: cover;
  border-radius: 8px;
  box-shadow: 0 0px 10px rgba(0, 0, 0, 0.1);
}

.book-details {
  flex: 2;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 0px 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
}

.details-container {
  width: 100%;
}

.book-details h1 {
  font-size: 2rem;
  margin-bottom: 10px;
  color: #333;
  text-align: left; /* Zmiana na tekst wyrównany do lewej */
}

.book-details p {
  font-size: 1rem;
  margin-bottom: 8px;
  color: #666;
  text-align: left; /* Zmiana na tekst wyrównany do lewej */
}

.book-details p strong {
  font-weight: bold;
  color: #333;
}

.rating-reviews {
  margin-top: 20px;
}

.rating-reviews h2 {
  font-size: 1.5rem;
  margin-bottom: 10px;
  text-align: center;
}

.rating-reviews ul {
  list-style-type: none;
  padding: 0;
}

.rating-reviews ul li {
  background-color: #f9f9f9;
  padding: 10px;
  border-radius: 4px;
  box-shadow: 0 0px 5px rgba(0, 0, 0, 0.1);
  margin-bottom: 10px;
}

.button-container {
  margin-top: 20px;
  display: flex;
  justify-content: flex-start; /* Zmiana na wyrównanie przycisków do lewej */
  gap: 10px;
}

.edit-button,
.delete-button,
.favorite-button,
.loan-button {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  color: #fff;
  cursor: pointer;
  transition: background-color 0.3s;
}

.edit-button {
  background-color: #007bff;
}

.edit-button:hover {
  background-color: #0056b3;
}

.delete-button {
  background-color: #dc3545;
}

.delete-button:hover {
  background-color: #c82333;
}

.favorite-button {
  background-color: #ffc107;
}

.favorite-button:hover {
  background-color: #e0a800;
}

.loan-button {
  background-color: #28a745;
}

.loan-button:hover {
  background-color: #218838;
}

.related-books {
  margin-top: 20px;
  text-align: left;
}

.related-books h2 {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.related-books ul {
  list-style-type: none;
  padding: 0;
}

.related-books ul li {
  margin-bottom: 5px;
}

.related-books ul li a {
  text-decoration: none;
  color: #007bff;
}

.related-books ul li a:hover {
  text-decoration: underline;
}
</style>
