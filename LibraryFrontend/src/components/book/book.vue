<template>
    <div class="book-details">
      <h1>{{ book.title }}</h1>
      <p>Author: {{ book.author }}</p>
      <p>ISBN: {{ book.isbn }}</p>
      <p>Published Year: {{ book.publishedYear }}</p>
      <p>Description: {{ book.description }}</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        book: {
          title: "Example Book",
          author: "John Doe",
          isbn: "1234567890",
          publishedYear: 2020,
          description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit..."
        }
      };
    }
  };
  </script>
  
  <style scoped>
    .book-details {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .book-details h1 {
    font-size: 24px;
    margin-bottom: 10px;
    color: #333;
    }

    .book-details p {
    font-size: 16px;
    margin-bottom: 8px;
    color: #666;
    }

    .book-details p:first-child {
    margin-top: 0;
    }

    .book-details p:last-child {
    margin-bottom: 0;
    }

    .book-details p strong {
    font-weight: bold;
    color: #333;
    }
  </style>