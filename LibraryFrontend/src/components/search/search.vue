<template>
  <div class="grid grid-cols-10 grid-rows-10 gap-4 h-screen">
    <div class="col-span-10">
      <search-input @update-search="updateSearchQuery"></search-input>
    </div>
    <div class="col-span-2 row-span-9 col-start-1 row-start-2">
      <search-category></search-category>
    </div>

    <div class="col-span-8 row-span-9 col-start-3 row-start-2">
      <p class="text-center font-bold">Wynik</p>
      <div
        v-for="book in paginatedBooks"
        :key="book.id"
        class="grid grid-cols-10 gap-4 border-b border-b-slate-400 mb-5 cursor-pointer"
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
      <!-- Pagination Controls -->
      <div class="flex justify-center mt-4">
        <button
          :disabled="currentPage === 1"
          @click="prevPage"
          class="px-4 py-2 mx-2 border rounded disabled:opacity-50"
        >
          Previous
        </button>
        <button
          :disabled="currentPage === totalPages"
          @click="nextPage"
          class="px-4 py-2 mx-2 border rounded disabled:opacity-50"
        >
          Next
        </button>
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

const itemsPerPage = 5; // Number of books per page
const currentPage = ref(1);
const searchQuery = ref("");

const filteredBooks = computed(() => {
  if (searchQuery.value) {
    return bookStore
      .FILTERED_BOOKS()
      .filter(
        (book) =>
          book.title.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
          book.author.toLowerCase().includes(searchQuery.value.toLowerCase())
      );
  }
  return bookStore.FILTERED_BOOKS();
});
console.log("FILTERED BOOKS: ", filteredBooks.value);

// Calculate total pages
const totalPages = computed(() =>
  Math.ceil(filteredBooks.value.length / itemsPerPage)
);

// Compute paginated books based on the current page
const paginatedBooks = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage;
  const end = start + itemsPerPage;
  return filteredBooks.value.slice(start, end);
});

// Pagination control methods
const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
  }
};

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++;
  }
};

const updateSearchQuery = (query) => {
  searchQuery.value = query;
  currentPage.value = 1; // Reset to first page on new search
};

const router = useRouter();
const goToBookDetails = (bookId) => {
  router.push({ name: "book", params: { id: bookId } });
};
</script>
