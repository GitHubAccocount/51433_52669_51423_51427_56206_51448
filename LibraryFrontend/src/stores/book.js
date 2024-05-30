import axios from "axios";
import { defineStore } from "pinia";
import { computed, ref } from "vue";
import { useRouter } from "vue-router";

export const useBookStore = defineStore("book", () => {
  const books = ref([]);

  const GET_BOOKS = async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/api/books`);
      books.value = response.data;
      console.log(response.data);
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

  const book = ref();
  const FETCH_BOOK_BY_ID = async (bookId) => {
    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/api/books/${bookId}`
      );
      book.value = response.data;
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

  return {
    book,
    books,
    selectedCategories,
    GET_BOOKS,
    FETCH_BOOK_BY_ID,
    FILTERED_BOOKS,
  };
});
