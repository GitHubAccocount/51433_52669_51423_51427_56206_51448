import axios from "axios";
import { defineStore } from "pinia";
import { computed, ref } from "vue";
import { useRouter } from "vue-router";

export const useBorrowingsStore = defineStore("borrowings", () => {
  const borrowings = ref();
  const GET_BORROWINGS = async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/api/borrowings/`);
      borrowings.value = response.data;
      console.log(borrowings.value);
    } catch (error) {
      console.log(error);
    }
  };

  const user_borrowings = ref();
  const GET_USER_BORROWINGS = async () => {
    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/api/borrowings/my_borrowings/`
      );
      user_borrowings.value = response.data;
      console.log(borrowings.value);
    } catch (error) {
      console.log(error);
    }
  };

  const success_message = ref();
  const BORROW_BOOK = async (data) => {
    try {
      await axios.post(`http://127.0.0.1:8000/api/borrowings/`, data);
      success_message.value = "Wypożyczono";
    } catch (error) {
      console.log(error);
    }
  };

  const RETURN_BOOK = async (id) => {
    try {
      await axios.delete(`http://127.0.0.1:8000/api/borrowings/${id}/`);
    } catch (error) {
      console.log(error);
    }
  };

  return {
    borrowings,
    success_message,
    user_borrowings,
    BORROW_BOOK,
    GET_BORROWINGS,
    GET_USER_BORROWINGS,
    RETURN_BOOK,
  };
});
