<template>
  <nav class="bg-gray-600">
    <div
      class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4"
    >
      <router-link
        to="/"
        class="self-center text-2xl font-semibold whitespace-nowrap dark:text-white"
        >Biblioteka</router-link
      >

      <div class="hidden w-full md:block md:w-auto" id="navbar-default">
        <ul
          class="font-medium flex flex-col p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 rtl:space-x-reverse md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-600 dark:border-gray-700"
        >
          <li>
            <router-link
              to="/my-borrowings"
              class="block py-2 px-3 hover:text-teal-300 text-white"
              >Moje wypożyczenia</router-link
            >
          </li>
          <li v-if="isSuperUser === 'true'">
            <router-link
              to="/admin"
              class="block py-2 px-3 hover:text-teal-300 text-white"
              >Wypożyczenia</router-link
            >
          </li>
          <li>
            <router-link
              to="/search"
              class="block py-2 px-3 hover:text-teal-300 text-white"
              >Wyszukiwarka</router-link
            >
          </li>

          <li v-if="!isAuthenticated">
            <router-link
              to="/login"
              class="block py-2 px-3 hover:text-teal-300 text-white"
              >Zaloguj się</router-link
            >
          </li>
          <li v-if="!isAuthenticated">
            <router-link
              to="/register"
              class="block py-2 px-3 hover:text-teal-300 text-white"
              >Zarejestruj się</router-link
            >
          </li>
          <li v-if="isAuthenticated">
            <button
              @click="logout"
              class="block py-2 px-3 hover:text-teal-300 text-white"
            >
              Wyloguj się
            </button>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { useUserStore } from "@/stores/user";
import { computed } from "vue";

const userStore = useUserStore();
const isAuthenticated = computed(() => userStore.user.isAuthenticated);
const isSuperUser = computed(() => userStore.user.is_superuser);

const logout = () => {
  userStore.LOGOUT();
};
</script>
