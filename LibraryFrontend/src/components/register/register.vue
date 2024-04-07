<template>
  <div class="min-h-screen flex items-center justify-center w-full">
    <div
      class="bg-white dark:bg-gray-400 shadow-md rounded-lg px-8 py-6 max-w-md"
    >
      <h1 class="text-2xl font-bold text-center mb-4 text-white">Biblioteka</h1>
      <form @submit.prevent="submit">
        <div class="mb-4">
          <inputLabel value="Adres Email" for="email"></inputLabel>
          <inputGlobal
            v-model="form.email"
            name="email"
            id="email"
            type="email"
            placeholder="przykład@email.com"
          ></inputGlobal>
          <span class="text-red-900 font-semibold" v-if="errors.email[0]">
            {{ errors.email[0] }}
          </span>
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
          <span class="text-red-900 font-semibold" v-if="errors.password[0]">
            {{ errors.password[0] }}
          </span>
        </div>

        <div class="mb-4">
          <inputLabel
            value="Powtórz hasło"
            for="password_confirmation"
          ></inputLabel>
          <inputGlobal
            v-model="form.password_confirmation"
            name="password_confirmation"
            id="password_confirmation"
            type="password"
            placeholder="Powtórz hasło"
          ></inputGlobal>
          <span
            class="text-red-900 font-semibold"
            v-if="errors.password_confirmation[0]"
          >
            {{ errors.password_confirmation[0] }}
          </span>

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
import axios from "axios";
import { useRouter } from "vue-router";

const form = ref({
  email: "",
  password: "",
  password_confirmation: "",
});

const errors = ref({ email: [], password: [], password_confirmation: [] });

const router = useRouter();
const submit = async () => {
  if (form.value.password === form.value.password_confirmation) {
    try {
      await axios.post("http://127.0.0.1:8000/api/register", form.value);
    } catch (error) {
      console.log(error);
      if (error.response.data) {
        if (error.response.data.email) {
          errors.value.email = error.response.data.email;
        }
        if (error.response.data.password) {
          errors.value.password = error.response.data.password;
        }
        if (error.response.data.non_field_errors) {
          errors.value.password = error.response.data.non_field_errors;
        }
      }
    } finally {
      router.push({ path: "/login" });
    }
  } else {
    errors.value.password_confirmation.push("Hała nie pasują do siebie");
  }
};
</script>
