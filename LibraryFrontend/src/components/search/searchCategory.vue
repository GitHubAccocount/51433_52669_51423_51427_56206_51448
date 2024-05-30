<template>
  <p class="text-center font-bold">Kategorie</p>
  <div>
    <search-collapsible collapsible-title="Nauki ścisłe">
      <div class="">
        <fieldset>
          <ul class="flex flex-wrap">
            <li class="h-8 w-1/2">
              <input
                id="chemistry"
                type="checkbox"
                value="chemia"
                v-model="bookStore.selectedCategories"
                @change="bookStore.FILTERED_BOOKS()"
                class="mr-3"
              />
              <label for="chemistry" class="text-sm">chemia</label>
            </li>
            <li class="h-8 w-1/2">
              <input
                id="physics"
                type="checkbox"
                value="fizyka"
                v-model="bookStore.selectedCategories"
                @change="bookStore.FILTERED_BOOKS()"
                class="mr-3"
              />
              <label for="physics" class="text-sm">fizyka</label>
            </li>
            <li class="h-8 w-1/2">
              <input
                id="mathematics"
                type="checkbox"
                value="matematyka"
                v-model="bookStore.selectedCategories"
                @change="bookStore.FILTERED_BOOKS()"
                class="mr-3"
              />
              <label for="mathematics" class="text-sm">matematyka</label>
            </li>
            <li class="h-8 w-1/2">
              <input
                id="geology"
                type="checkbox"
                value="geologia"
                v-model="bookStore.selectedCategories"
                @change="bookStore.FILTERED_BOOKS()"
                class="mr-3"
              />
              <label for="geology" class="text-sm">geologia</label>
            </li>
          </ul>
        </fieldset>
      </div>
    </search-collapsible>

    <search-collapsible collapsible-title="Biznes i Ekonomia">
      <div class="">
        <fieldset>
          <ul class="flex flex-wrap">
            <li class="h-8 w-1/2">
              <input
                id="marketing"
                type="checkbox"
                value="marketing"
                v-model="bookStore.selectedCategories"
                @change="bookStore.FILTERED_BOOKS()"
                class="mr-3"
              />
              <label for="marketing" class="text-sm">marketing</label>
            </li>
            <li class="h-8 w-1/2">
              <input
                id="finance"
                type="checkbox"
                value="finanse"
                v-model="bookStore.selectedCategories"
                @change="bookStore.FILTERED_BOOKS()"
                class="mr-3"
              />
              <label for="finance" class="text-sm">finanse</label>
            </li>
            <li class="h-8 w-1/2">
              <input
                id="social_media"
                type="checkbox"
                value="social media"
                v-model="bookStore.selectedCategories"
                @change="bookStore.FILTERED_BOOKS()"
                class="mr-3"
              />
              <label for="social_media" class="text-sm">social media</label>
            </li>
            <li class="h-8 w-1/2">
              <input
                id="sales"
                type="checkbox"
                value="sprzedaż"
                v-model="bookStore.selectedCategories"
                @change="bookStore.FILTERED_BOOKS()"
                class="mr-3"
              />
              <label for="sales" class="text-sm">sprzedaż</label>
            </li>
          </ul>
        </fieldset>
      </div>
    </search-collapsible>

    <search-collapsible collapsible-title="Literatura">
      <div class="">
        <fieldset>
          <ul class="flex flex-wrap">
            <li class="h-8 w-1/2">
              <input
                id="fantasy"
                type="checkbox"
                value="fantasy"
                v-model="bookStore.selectedCategories"
                @change="bookStore.FILTERED_BOOKS()"
                class="mr-3"
              />
              <label for="fantasy" class="text-sm">fantasy</label>
            </li>
            <li class="h-8 w-1/2">
              <input
                id="crime"
                type="checkbox"
                value="kryminał"
                v-model="bookStore.selectedCategories"
                @change="bookStore.FILTERED_BOOKS()"
                class="mr-3"
              />
              <label for="crime" class="text-sm">kryminał</label>
            </li>
            <li class="h-8 w-1/2">
              <input
                id="sci_fi"
                type="checkbox"
                value="sci_fi"
                v-model="bookStore.selectedCategories"
                @change="bookStore.FILTERED_BOOKS()"
                class="mr-3"
              />
              <label for="sci_fi" class="text-sm">sci-Fi</label>
            </li>
            <li class="h-8 w-1/2">
              <input
                id="romance"
                type="checkbox"
                value="romantyczne"
                v-model="bookStore.selectedCategories"
                @change="bookStore.FILTERED_BOOKS()"
                class="mr-3"
              />
              <label for="romance" class="text-sm">romantyczne</label>
            </li>
          </ul>
        </fieldset>
      </div>
    </search-collapsible>
  </div>
</template>

<script setup>
import { ref } from "vue";
import searchCollapsible from "../shared/searchCollapsible.vue";
import { useBookStore } from "@/stores/book";

const bookStore = useBookStore();
</script>
