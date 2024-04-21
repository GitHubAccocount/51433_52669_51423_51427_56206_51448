<template>
  <div class="min-h-screen flex items-center justify-center w-full">
    <div
      class="bg-white dark:bg-gray-400 shadow-md rounded-lg px-8 py-6 max-w-md"
    >
      <h1 class="text-2xl font-bold text-center mb-4 text-white">Biblioteka</h1>
      <form @submit.prevent="submit" action="#">
        <span class="text-red-900 font-semibold" v-if="errors">
          {{ errors }}
        </span>
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

          <a
            href="#"
            class="text-xs text-gray-200 hover:text-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            >Zapomniałeś hasła?</a
          >
        </div>

        <div class="flex items-center justify-end mb-4">
          <a
            href="#"
            class="text-xs text-slate-600 hover:text-slate-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-slate-500"
            >Stwórz konto</a
          >
        </div>
        <button
          type="submit"
          class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-slate-600 hover:bg-slate-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
        >
          Zaloguj się
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";
import inputGlobal from "../shared/inputGlobal.vue";
import inputLabel from "../shared/inputLabel.vue";
import { ref } from "vue";
import axios from "axios";
import { useUserStore } from "@/stores/user";

const form = ref({
  email: "",
  password: "",
});

const userStore = useUserStore();

const errors = ref();

const router = useRouter();
const submit = () => {
  userStore.LOGIN(form.value);
};
</script>
