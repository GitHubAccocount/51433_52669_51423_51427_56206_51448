<script setup>
import { RouterLink, RouterView } from "vue-router";
import navigation from "./components/navigation/navigation.vue";
</script>

<template>
  <header class="pb-5">
    <navigation></navigation>
  </header>

  <main class="px-5">
    <RouterView />
  </main>
</template>
