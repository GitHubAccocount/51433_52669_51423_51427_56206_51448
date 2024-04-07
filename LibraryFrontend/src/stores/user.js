import { defineStore } from "pinia";
import { ref } from "vue";

export const useUserStore = defineStore("user", () => {
  const user = ref({
    isAuthenticated: false,
    id: null,
    email: null,
    access: null,
    refresh: null,
  });
});
