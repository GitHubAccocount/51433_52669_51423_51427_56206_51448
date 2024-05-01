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
      <div>
        <router-link to="/book" class="hover:text-teal-300">
        
          <div class="border-b-slate-400 border-b mb-5">
            <p class="font-semibold">Książka o tytule</p>
            <p>Autor Książki</p>
            <p>Rok wydania: 2019</p>
            <p>Lorem ipsum</p>
            <p>Dostępność: 2/2</p>
          </div>

        </router-link>

        <router-link to="/book" class="hover:text-teal-300">

          <div class="border-b-slate-400 border-b mb-5">
            <p class="font-semibold">Książka o tytule</p>
            <p>Autor Książki</p>
            <p>Rok wydania: 2019</p>
            <p>Lorem ipsum</p>
            <p>Dostępność: 2/2</p>
          </div>

        </router-link>

      </div>
    </div>
  </div>
</template>

<script setup>
import searchInput from "./searchInput.vue";
import searchCategory from "./searchCategory.vue";
</script>
