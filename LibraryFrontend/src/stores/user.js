import axios from "axios";
import { defineStore } from "pinia";
import { ref } from "vue";
import { useRouter } from "vue-router";

export const useUserStore = defineStore("user", () => {
  const user = ref({
    isAuthenticated: !!localStorage.getItem("user.access"),
    id: localStorage.getItem("user.id") ?? null,
    email: localStorage.getItem("user.email") ?? null,
    access: localStorage.getItem("user.access") ?? null,
    refresh: localStorage.getItem("user.refresh") ?? null,
  });

  const router = useRouter();
  const isSubmitting = ref(false);
  const errors = ref([]);

  // const REGISTER = async (form) => {
  //   const baseUrl = import.meta.env.VITE_APP_API_URL;
  //   try {
  //     isSubmitting.value = true;
  //     const response = await axios.post(`${baseUrl}/registration`, form);
  //     message.value = response.data.message;
  //     toast.success(message.value);
  //   } catch (error) {
  //     console.log(error);
  //   } finally {
  //     isSubmitting.value = false;
  //     message.value = "";
  //   }
  // };

  const LOGIN = async (form) => {
    try {
      isSubmitting.value = true;
      const response = await axios.post(
        `http://127.0.0.1:8000/api/login`,
        form
      );
      axios.defaults.headers.common["Authorization"] =
        "Bearer " + response.data.access;
      setToken(response.data);
      getUserData();
    } catch (error) {
      if (error.response.data.detail) {
        errors.value.push(error.response.data.detail);
      }
    } finally {
    }
  };

  const getUserData = async () => {
    try {
      isSubmitting.value = true;
      const response = await axios.get(`http://127.0.0.1:8000/api/user_data`);
      setUser(response.data);
    } catch (error) {
      console.log(error);
    } finally {
      isSubmitting.value = false;
      router.push({ path: "/" });
    }
  };

  const setToken = (data) => {
    localStorage.setItem("user.access", data.access);
    localStorage.setItem("user.refresh", data.refresh);

    user.value.access = data.access;
    user.value.refresh = data.refresh;
  };

  const setUser = (data) => {
    localStorage.setItem("user.email", data.email);
    localStorage.setItem("user.id", data.id);

    user.value.isAuthenticated = true;
    user.value.id = data.id;
    user.value.email = data.email;
  };

  const LOGOUT = () => {
    user.value.isAuthenticated = false;
    localStorage.removeItem("user.access");
    localStorage.removeItem("user.refresh");
    localStorage.removeItem("user.email");
    localStorage.removeItem("user.id");
    user.value.id = "";
    user.value.email = "";
    user.value.roles = "";
    router.push("/login");
  };

  return {
    errors,
    isSubmitting,
    user,
    // REGISTER,
    LOGIN,
    LOGOUT,
  };
});
