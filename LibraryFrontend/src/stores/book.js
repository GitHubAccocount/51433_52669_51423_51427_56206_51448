import axios from "axios";
import { defineStore } from "pinia";
import { computed, ref } from "vue";
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

  const selectedCategories = ref([]);

  const FILTERED_BOOKS = () => {
    if (selectedCategories.value.length === 0) {
      return books.value;
    }
    return books.value.filter((book) =>
      selectedCategories.value.includes(book.category)
    );
  };

  return {
    books,
    selectedCategories,
    GET_BOOKS,
    FILTERED_BOOKS,
  };
});
