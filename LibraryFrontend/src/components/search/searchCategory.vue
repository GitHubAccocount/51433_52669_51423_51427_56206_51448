<template>
  <p class="text-center font-bold">Kategorie</p>
  <div>
    <search-collapsible collapsible-title="Nauki ścisłe">
      <div class="">
        <fieldset>
          <ul class="flex flex-wrap">
            <li class="h-8 w-1/2">
              <input id="chemistry" type="checkbox" class="mr-3" />
              <label for="chemistry" class="text-sm">chemia</label>
            </li>
            <li class="h-8 w-1/2">
              <input id="physics" type="checkbox" class="mr-3" />
              <label for="physics" class="text-sm">fizyka</label>
            </li>
            <li class="h-8 w-1/2">
              <input id="mathematics" type="checkbox" class="mr-3" />
              <label for="mathematics" class="text-sm">matematyka</label>
            </li>
            <li class="h-8 w-1/2">
              <input id="geology" type="checkbox" class="mr-3" />
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
              <input id="marketing" type="checkbox" class="mr-3" />
              <label for="marketing" class="text-sm">marketing</label>
            </li>
            <li class="h-8 w-1/2">
              <input id="finance" type="checkbox" class="mr-3" />
              <label for="finance" class="text-sm">finanse</label>
            </li>
            <li class="h-8 w-1/2">
              <input id="social_media" type="checkbox" class="mr-3" />
              <label for="social_media" class="text-sm">social media</label>
            </li>
            <li class="h-8 w-1/2">
              <input id="sales" type="checkbox" class="mr-3" />
              <label for="sales" class="text-sm">sprzedaż</label>
            </li>
          </ul>
        </fieldset>
      </div>
    </search-collapsible>
  </div>
</template>

<script setup>
import searchCollapsible from "../shared/searchCollapsible.vue";
</script>
