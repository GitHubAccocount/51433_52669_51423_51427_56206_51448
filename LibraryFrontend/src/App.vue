<script setup>
import { RouterLink, RouterView } from "vue-router";
import navigation from "./components/navigation/navigation.vue";
</script>

<template>
  <header>
    <navigation></navigation>
  </header>

  <RouterView />
</template>
