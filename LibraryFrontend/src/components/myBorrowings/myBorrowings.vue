<template>
  <div class="px-20">
    <h2 class="font-bold text-xl mb-5">Moje wypożyczone książki</h2>
    <div v-for="borrowing in user_borrowings" class="flex gap-5 mb-3">
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
      </div>
    </div>
  </div>
</template>

<script setup>
import { useBorrowingsStore } from "@/stores/borrowings";
import { computed, onMounted, ref } from "vue";
import moment from "moment";

const borrowingsStore = useBorrowingsStore();
const user_borrowings = computed(() => borrowingsStore.user_borrowings);

onMounted(() => {
  borrowingsStore.GET_USER_BORROWINGS();
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
</script>
