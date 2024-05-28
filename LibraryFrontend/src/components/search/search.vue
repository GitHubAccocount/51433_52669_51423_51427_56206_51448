<template>
  <div class="grid grid-cols-10 grid-rows-10 gap-4 h-screen">
    <div class="col-span-10">
      <search-input></search-input>
    </div>
    <div class="col-span-2 row-span-9 col-start-1 row-start-2">
      <search-category></search-category>
    </div>

    <div class="col-span-8 row-span-9 col-start-3 row-start-2">
      <p class="text-center font-bold">Wynik</p>
      <div
        v-for="book in filteredBooks"
        :key="book.id"
        class="grid grid-cols-10 gap-4 border-b border-b-slate-400 mb-5"
        @click="goToBookDetails(book.id)"
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
          <p>Dostępność: {{ book.available }}/{{ book.total_stock }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import searchInput from "./searchInput.vue";
import searchCategory from "./searchCategory.vue";
import { useBookStore } from "@/stores/book";
import { computed, onMounted, ref } from "vue";
import { useRouter } from "vue-router";

const bookStore = useBookStore();

onMounted(() => {
  bookStore.GET_BOOKS();
});

const filteredBooks = computed(() => bookStore.FILTERED_BOOKS());
console.log("FILTERED BOOKS: ", filteredBooks.value);

const router = useRouter();
const goToBookDetails = (bookId) => {
  router.push({ name: "book", params: { id: bookId } });
};
</script>
