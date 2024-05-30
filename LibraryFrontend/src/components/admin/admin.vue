<template>
  <div class="px-20">
    <h2 class="font-bold text-xl mb-5">Książki wypożyczone</h2>
    <div class="mb-3">
      <input
        class="border border-black px-2 py-1"
        type="email"
        v-model="searchEmail"
        placeholder="Wyszukaj po mailu"
      />
    </div>
    <div v-for="borrowing in filteredBorrowings" class="flex gap-5 mb-3">
      <div class="w-40">
        <img class="w-full" :src="borrowing.book.image_url" />
      </div>
      <div>
        <p>
          <span class="font-bold">Data wypożyczenia:</span>
          {{ formattedBorrowedAt(borrowing.borrowed_at) }}
        </p>
        <p :class="{ 'text-red-500': isOverdue(borrowing.return_date) }">
          <span class="font-bold">Data zwrotu:</span>
          {{ formattedReturnDate(borrowing.return_date) }}
        </p>
        <p>
          <span class="font-bold">Wypożyczający:</span>
          {{ borrowing.user.email }}
        </p>
        <p>
          <span class="font-bold">Książka:</span> {{ borrowing.book.title }},
          {{ borrowing.book.author }},
          {{ borrowing.book.year_published }}
        </p>
        <p>
          <span class="font-bold">Id książki:</span> {{ borrowing.book.id }}
        </p>

        <button
          class="px-3 py-2 bg-lime-500 mt-2"
          @click="return_book(borrowing.id)"
        >
          Zwróć
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useBorrowingsStore } from "@/stores/borrowings";
import { computed, onMounted, ref } from "vue";
import moment from "moment";

const borrowingsStore = useBorrowingsStore();
const borrowings = computed(() => borrowingsStore.borrowings);
console.log("borrowings: ", borrowings.v);

onMounted(() => {
  borrowingsStore.GET_BORROWINGS();
});

const formattedBorrowedAt = (dateString) => {
  return moment(dateString).format("YYYY-MM-DD");
};

const formattedReturnDate = (dateString) => {
  return moment(dateString).format("YYYY-MM-DD");
};

const isOverdue = (returnDateString) => {
  return moment(returnDateString).isBefore(moment(), "day");
};

const searchEmail = ref("");

const filteredBorrowings = computed(() => {
  if (!searchEmail.value) {
    return borrowings.value;
  } else {
    const normalizedEmail = searchEmail.value.toLowerCase();
    return borrowings.value.filter((borrowing) =>
      borrowing.user.email.toLowerCase().includes(normalizedEmail)
    );
  }
});

const return_book = async (id) => {
  borrowingsStore.RETURN_BOOK(id);
};
</script>
