<template>
  <div class="min-h-screen flex items-center justify-center w-full">
    <div
      class="bg-white dark:bg-gray-400 shadow-md rounded-lg px-8 py-6 max-w-md"
    >
      <h1 class="text-2xl font-bold text-center mb-4 text-white">Biblioteka</h1>
      <form @submit.prevent="submit" action="#">
        <div class="mb-4">
          <inputLabel value="Adres Email" for="email"></inputLabel>
          <inputGlobal
            v-model="form.email"
            name="email"
            id="email"
            type="email"
            placeholder="przykład@email.com"
          ></inputGlobal>
        </div>

        <div class="mb-4">
          <inputLabel value="Hasło" for="password"></inputLabel>
          <inputGlobal
            v-model="form.password"
            name="password"
            id="password"
            type="password"
            placeholder="Wprowadź hasło"
          ></inputGlobal>
        </div>

        <div class="mb-4">
          <inputLabel
            value="Powtórz hasło"
            for="password_confirmation"
          ></inputLabel>
          <inputGlobal
            v-model="form.password"
            name="password_confirmation"
            id="password_confirmation"
            type="password_confirmation"
            placeholder="Powtórz hasło"
          ></inputGlobal>

          <router-link
            to="/login"
            class="text-xs text-gray-200 hover:text-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            >Masz już konto? Zaloguj się</router-link
          >
        </div>

        <button
          type="submit"
          class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-slate-600 hover:bg-slate-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
        >
          Zarejestruj się
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import inputGlobal from "../shared/inputGlobal.vue";
import inputLabel from "../shared/inputLabel.vue";
import { ref } from "vue";

const form = ref({
  email: "",
  password: "",
  password_confirmation: "",
});

const submit = () => {
  console.log(form.value);
};
</script>
