<template>
  <div class="max-w-md mx-auto">
    <div
      class="relative flex items-center w-full h-12 rounded-lg border border-black focus-within:border-2 bg-white overflow-hidden"
    >
      <input
        class="peer h-full w-full outline-none text-sm text-gray-700 pl-2"
        type="text"
        id="search"
        placeholder="Wpisz tytuł lub autora"
        @input="onInput"
      />

      <button>
        <div class="grid place-items-center h-full w-12 text-gray-400">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-6 w-6"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
            />
          </svg>
        </div>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const searchQuery = ref("");

const onInput = (event) => {
  searchQuery.value = event.target.value;
  emit("update-search", searchQuery.value);
};

const emit = defineEmits(["update-search"]);
</script>
