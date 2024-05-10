<template>
  <div class="grid grid-cols-10 grid-rows-10 gap-4 h-screen gap-10">
    <div class="col-span-10">
      <search-input></search-input>
    </div>
    <div class="col-span-2 row-span-9 col-start-1 row-start-2">
      <search-category></search-category>
    </div>

    <div class="col-span-8 row-span-9 col-start-3 row-start-2">
      <p class="text-center font-bold">Wynik</p>
      <div
        v-for="book in bookStore.books"
        :key="book.id"
        class="grid grid-cols-10 gap-4 border-b border-b-slate-400 mb-5"
      >
        <div class="col-span-2">
          <img
            :src="book.image"
            :alt="book.title"
            class="w-full h-auto object-cover"
          />
        </div>
        <div class="col-span-8">
          <p class="font-semibold">{{ book.title }}</p>
          <p>{{ book.author }}</p>
          <p>Rok wydania: {{ book.year_published }}</p>
          <p>{{ book.description }}</p>
          <p>Dostępność: 2/2</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import searchInput from "./searchInput.vue";
import searchCategory from "./searchCategory.vue";
import { useBookStore } from "@/stores/book";
import { onMounted } from "vue";

const bookStore = useBookStore();

onMounted(() => {
  bookStore.GET_BOOKS();
});
</script>
