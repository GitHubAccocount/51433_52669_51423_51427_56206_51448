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
              to="/login"
              href="#"
              class="block py-2 px-3 hover:text-teal-300 text-white"
              >Zaloguj się</router-link
            >
          </li>
          <li>
            <router-link
              to="/register"
              href="#"
              class="block py-2 px-3 hover:text-teal-300 text-white"
              >Zarejestruj się</router-link
            >
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup></script>
