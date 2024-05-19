<template>
  <div class="book-details-container">
    <div class="book-cover">
      <img :src="bookCover" alt="Okładka książki" class="cover-placeholder" />
    </div>
    <div class="book-details">
      <div class="details-container">
        <h1>{{ book.title }}</h1>
        <p><strong>Autor:</strong> {{ book.author }}</p>
        <p><strong>ISBN:</strong> {{ book.isbn }}</p>
        <p><strong>Rok publikacji:</strong> {{ book.publishedYear }}</p>
        <p><strong>Gatunek:</strong> {{ book.genre }}</p>
        <p><strong>Opis:</strong> {{ book.description }}</p>
        <p><strong>Wydawca:</strong> {{ book.publisher }}</p>
        <p><strong>Liczba stron:</strong> {{ book.pages }}</p>
        <p><strong>Język:</strong> {{ book.language }}</p>
        <div class="rating-reviews">
          <h2>Oceny i recenzje</h2>
          <p><strong>Ocena:</strong> {{ book.rating }} / 5</p>
          <ul>
            <li v-for="review in book.reviews" :key="review.id">
              <p><strong>{{ review.user }}</strong>: {{ review.comment }}</p>
              <p>Ocena: {{ review.rating }} / 5</p>
            </li>
          </ul>
        </div>
        <div class="button-container">
          <router-link to="/bookEdit" class="edit-button">Edytuj</router-link>
          <button class="delete-button" @click="deleteBook">Usuń</button>
          <button class="favorite-button" @click="addToFavorites">Dodaj do ulubionych</button>
          <button class="loan-button" @click="loanBook">Wypożycz</button>
        </div>
        <div class="related-books">
          <h2>Powiązane książki</h2>
          <ul>
            <li v-for="related in relatedBooks" :key="related.id">
              <router-link :to="'/book/' + related.id">{{ related.title }}</router-link>
            </li>
          </ul>
        </div>
      </div>
    </div>
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
        description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit...",
        genre: "Fikcja",
        publisher: "Example Publisher",
        pages: 350,
        language: "Polski",
        rating: 4.5,
        reviews: [
          { id: 1, user: "Alice", comment: "Świetna książka!", rating: 5 },
          { id: 2, user: "Bob", comment: "Bardzo dobra, ale trochę za długa.", rating: 4 },
        ],
      },
      bookCover: 'https://via.placeholder.com/500x800', // Placeholder for book cover
      relatedBooks: [
        { id: 2, title: "Related Book 1" },
        { id: 3, title: "Related Book 2" },
      ],
    };
  },
  methods: {
    deleteBook() {
      if (confirm("Czy na pewno chcesz usunąć tę książkę?")) {
        // Kod usuwający książkę
        // np. this.$http.delete(`/books/${this.book.id}`)
        // this.$router.push('/books')
      }
    },
    addToFavorites() {
      // Kod dodający książkę do ulubionych -- pewnie do usunięcia
      alert("Dodano do ulubionych!");
    },
    loanBook() {
      // Kod wypożyczający książkę
      alert("Wypożyczono książkę!");
    }
  }
};
</script>

<style scoped>
.book-details-container {
  display: flex;
  justify-content: center;
  padding: 20px;
  background-color: #f9f9f9;
  gap: 20px;
}

.book-cover {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.cover-placeholder {
  max-width: 100%;
  max-height: 400px;
  object-fit: cover;
  border-radius: 8px;
  box-shadow: 0 0px 10px rgba(0, 0, 0, 0.1);
}

.book-details {
  flex: 2;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 0px 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
}

.details-container {
  width: 100%;
}

.book-details h1 {
  font-size: 2rem;
  margin-bottom: 10px;
  color: #333;
  text-align: left; /* Zmiana na tekst wyrównany do lewej */
}

.book-details p {
  font-size: 1rem;
  margin-bottom: 8px;
  color: #666;
  text-align: left; /* Zmiana na tekst wyrównany do lewej */
}

.book-details p strong {
  font-weight: bold;
  color: #333;
}

.rating-reviews {
  margin-top: 20px;
}

.rating-reviews h2 {
  font-size: 1.5rem;
  margin-bottom: 10px;
  text-align: center;
}

.rating-reviews ul {
  list-style-type: none;
  padding: 0;
}

.rating-reviews ul li {
  background-color: #f9f9f9;
  padding: 10px;
  border-radius: 4px;
  box-shadow: 0 0px 5px rgba(0, 0, 0, 0.1);
  margin-bottom: 10px;
}

.button-container {
  margin-top: 20px;
  display: flex;
  justify-content: flex-start; /* Zmiana na wyrównanie przycisków do lewej */
  gap: 10px;
}

.edit-button,
.delete-button,
.favorite-button,
.loan-button {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  color: #fff;
  cursor: pointer;
  transition: background-color 0.3s;
}

.edit-button {
  background-color: #007bff;
}

.edit-button:hover {
  background-color: #0056b3;
}

.delete-button {
  background-color: #dc3545;
}

.delete-button:hover {
  background-color: #c82333;
}

.favorite-button {
  background-color: #ffc107;
}

.favorite-button:hover {
  background-color: #e0a800;
}

.loan-button {
  background-color: #28a745;
}

.loan-button:hover {
  background-color: #218838;
}

.related-books {
  margin-top: 20px;
  text-align: left;
}

.related-books h2 {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.related-books ul {
  list-style-type: none;
  padding: 0;
}

.related-books ul li {
  margin-bottom: 5px;
}

.related-books ul li a {
  text-decoration: none;
  color: #007bff;
}

.related-books ul li a:hover {
  text-decoration: underline;
}
</style>
