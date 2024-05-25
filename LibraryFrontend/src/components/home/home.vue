<template>
    <div class="home-container">
      <h1>Witaj w naszej bibliotece!</h1>
      <div class="additional-content">
        <h2>O naszej bibliotece</h2>
        <p>
          Nasza biblioteka oferuje szeroki wybór książek z różnych kategorii, od literatury pięknej po literaturę naukową.
          Zapewniamy wygodny sposób przeglądania oraz wypożyczania książek online. Dołącz do nas już dziś!
        </p>
      </div>
      <div class="sections-container">
        <div class="categories-section">
          <h2>Kategorie</h2>
          <div class="categories-grid">
            <div class="category-card" v-for="category in categories" :key="category.id">
              <router-link :to="'/category/' + category.id">{{ category.name }}</router-link>
            </div>
          </div>
        </div>
        <div class="content-section">
          <div class="new-arrivals-section" >
            <h2>Nowości</h2>
            <div class="books-grid">
              <div class="book-card" v-for="book in newBooks" :key="book.id">
                <img :src="book.cover" alt="Okładka książki" class="book-cover" />
                <div class="book-info">
                  <h3>{{ book.title }}</h3>
                  <p>{{ book.author }}</p>
                </div>
              </div>
            </div>
          </div>
          <div class="featured-books-section">
            <h2>Polecane książki</h2>
            <div class="books-grid">
              <div class="book-card" v-for="book in featuredBooks" :key="book.id">
                <img :src="book.cover" alt="Okładka książki" class="book-cover" />
                <div class="book-info">
                  <h3>{{ book.title }}</h3>
                  <p>{{ book.author }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        newBooks: [
          { id: 1, title: "Książka 1", author: "Autor 1", cover: "https://via.placeholder.com/500%20x%20800" },
          { id: 2, title: "Książka 2", author: "Autor 2", cover: "https://via.placeholder.com/500%20x%20800" },
          { id: 3, title: "Książka 3", author: "Autor 3", cover: "https://via.placeholder.com/500%20x%20800" },
          { id: 4, title: "Książka 4", author: "Autor 4", cover: "https://via.placeholder.com/500%20x%20800" },
          { id: 5, title: "Książka 5", author: "Autor 5", cover: "https://via.placeholder.com/500%20x%20800" },
        ],
        featuredBooks: [
          { id: 6, title: "Książka 1", author: "Autor 1", cover: "https://via.placeholder.com/500%20x%20800" },
          { id: 7, title: "Książka 2", author: "Autor 2", cover: "https://via.placeholder.com/500%20x%20800" },
          { id: 8, title: "Książka 3", author: "Autor 3", cover: "https://via.placeholder.com/500%20x%20800" },
          { id: 9, title: "Książka 4", author: "Autor 4", cover: "https://via.placeholder.com/500%20x%20800" },
          { id: 10, title: "Książka 5", author: "Autor 6", cover: "https://via.placeholder.com/500%20x%20800" },
        ],
        categories: [
          { id: 1, name: "Fikcja" },
          { id: 2, name: "Fantastyka" },          
          { id: 3, name: "Nauka" },
          { id: 4, name: "Biografia" },
          { id: 5, name: "Kryminał" },

        ]
      };
    },
  };
  </script>
  
  <style scoped>
  .home-container {
    margin-top: 20px;
  }
  
  h1 {
    font-size: 2.5rem;
    margin-bottom: 20px;
    text-align: center;
  }
  
  h2 {
    font-size: 1.8rem;
    margin-bottom: 10px;
  }
  
  p {
    font-size: 1.2rem;
    color: #666;
    text-align: center;
  }
  
  .sections-container {
    display: flex;
    gap: 20px;
  }
  
  .categories-section {
    flex: 1;
    margin-right: 20px;

    background-color: #ffefee;
    padding: 20px;
    border-radius: 8px;
  }
  
  .content-section {
    flex: 2;
    display: flex;
    flex-direction: column;
    
    background-color: #ffefee;
    padding: 20px;
    border-radius: 8px;
  }
  
  .categories-section h2 {
    font-size: 2.5rem;
    margin-bottom: 20px;
  }
  
  .categories-grid {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  
  .category-card {
    background-color: #f9f9f9;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0px 10px rgba(0, 0, 0, 0.1);
    text-align: center;
    font-size: 1.2rem;
  }
  
  .category-card a {
    text-decoration: none;
    color: inherit;
  }
  
  .category-card:hover {
    background-color: #ececec;
  }
  
  .content-section h2 {
    font-size: 2.5rem;
  }
  
  .books-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
    gap: 20px;
  }
  
  .book-card {
    background-color: hsla(49, 100%, 81%, 0.815);
    border-radius: 8px;
    box-shadow: 0 0px 10px rgba(0, 0, 0, 0.1);
    overflow: hidden;
    text-align: center;
    padding: 10px;
    margin-bottom: 25px;
  }
  
  .book-cover {
    max-width: 100%;
    height: auto;
    margin-bottom: 10px;
  }
  
  .book-info h3 {
    font-size: 1.2rem;
    margin-bottom: 5px;
  }
  
  .book-info p {
    font-size: 1rem;
    color: #666;
  }
  
  .additional-content {
    margin-top: 40px;
    margin-bottom: 40px;
  }
  </style>
  