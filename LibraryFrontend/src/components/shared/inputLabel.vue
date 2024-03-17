<template>
  <label class="block text-sm font-medium text-white mb-2">{{ value }}</label>
</template>

<script setup>
defineProps({
  value: {
    type: String,
  },
});
</script>
