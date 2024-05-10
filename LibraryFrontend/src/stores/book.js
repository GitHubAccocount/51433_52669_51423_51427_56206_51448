import axios from "axios";
import { defineStore } from "pinia";
import { ref } from "vue";
import { useRouter } from "vue-router";

export const useBookStore = defineStore("book", () => {
  const books = ref([]);

  const GET_BOOKS = async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/api/books`);
      books.value = response.data.books;
      console.log(books.value);
    } catch (error) {
      console.log(error);
    } finally {
    }
  };

  return {
    books,
    GET_BOOKS,
  };
});
