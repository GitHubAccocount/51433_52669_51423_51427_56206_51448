<template>
  <div class="border-brand-grey-2 border-b border-solid py-5">
    <div
      class="flex-warp flex cursor-pointer items-center justify-between"
      role="button"
      @click="open"
    >
      <h3 class="text-base font-semibold">{{ collapsibleTitle }}</h3>
      <svg
        class="w-4"
        :class="{ ' rotate-45': isOpen }"
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 448 512"
      >
        <path
          d="M256 80c0-17.7-14.3-32-32-32s-32 14.3-32 32V224H48c-17.7 0-32 14.3-32 32s14.3 32 32 32H192V432c0 17.7 14.3 32 32 32s32-14.3 32-32V288H400c17.7 0 32-14.3 32-32s-14.3-32-32-32H256V80z"
        />
      </svg>
    </div>
    <div v-if="isOpen" class="mt-5 w-full">
      <slot>Oops! Somebody forgot to populate me.</slot>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";

const isOpen = ref(false);
const props = defineProps(["collapsibleTitle"]);
const collapsibleTitle = props.collapsibleTitle;

const open = () => {
  isOpen.value = !isOpen.value;
};
</script>
