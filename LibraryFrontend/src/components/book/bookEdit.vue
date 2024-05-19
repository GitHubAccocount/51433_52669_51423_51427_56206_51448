<template>
  <div class="edit-book-container">
    <div class="book-cover">
      <img :src="bookCover" alt="Okładka książki" class="cover-placeholder"/>
      <input type="file" @change="uploadCover"/>
    </div>
    <div class="book-details" ref="detailsContainer">
      <div class="details-container">
        <h1>Edytuj książkę</h1>
        <form @submit.prevent="saveChanges">
          <div class="form-group">
            <label for="title">Tytuł:</label>
            <input type="text" id="title" v-model="editedBook.title" placeholder="Wprowadź tytuł książki" required>
          </div>
          <div class="form-group">
            <label for="author">Autor:</label>
            <input type="text" id="author" v-model="editedBook.author" placeholder="Wprowadź autora książki" required>
          </div>
          <div class="form-group">
            <label for="isbn">ISBN:</label>
            <input type="text" id="isbn" v-model="editedBook.isbn" placeholder="Wprowadź ISBN książki" required>
          </div>
          <div class="form-group">
            <label for="publishedYear">Rok publikacji:</label>
            <input type="number" id="publishedYear" v-model="editedBook.publishedYear" placeholder="Wprowadź rok publikacji" required>
          </div>
          <div class="form-group">
            <label for="genres">Gatunek:</label>
            <multiselect v-model="editedBook.genres" :options="genresOptions" :multiple="true" :close-on-select="false" :clear-on-select="false" :preserve-search="true" placeholder="Wybierz gatunki" label="name" track-by="name" style="top: auto !important; bottom: 100% !important;"></multiselect>
          </div>
          <div class="form-group">
            <label for="description">Opis:</label>
            <textarea id="description" v-model="editedBook.description" placeholder="Wprowadź opis książki" required></textarea>
          </div>
          <button type="submit">Zapisz zmiany</button>
        </form>
      </div>
    </div>
  </div>
</template>
  
  <script>
  import Multiselect from 'vue-multiselect';
  import 'vue-multiselect/dist/vue-multiselect.css';

  export default {
    components: {
      Multiselect
    },
    data() {
      return {
        editedBook: {
          title: "Example Book",
          author: "John Doe",
          isbn: "1234567890",
          publishedYear: 2020,
          genres: [],
          description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit..."
        },
        genresOptions: [
          { name: 'Fikcja' },
          { name: 'Fantastyka' },
          { name: 'Nauka' },
          { name: 'Biografia' },
          { name: 'Kryminał' }
        ],
        bookCover: 'https://via.placeholder.com/500%20x%20800' // Placeholder for book cover
      };
    },
    mounted() {
      window.addEventListener('resize', this.setDetailsHeight);
      this.setDetailsHeight();
    },
    beforeDestroy() {
      window.removeEventListener('resize', this.setDetailsHeight);
    },

    methods: {
        async saveChanges() {
      try {
        // Wywołanie API do aktualizacji książki
            //await axios.put(`/api/books/${this.editedBook.id}`, this.editedBook);
        
        // Po zapisaniu zmian przekieruj użytkownika na stronę szczegółów książki
            //this.$router.push(`/book/${this.editedBook.id}`);

        this.$router.push(`/book`);

      } catch (error) {
            console.error('Wystąpił błąd podczas zapisywania zmian:', error);
        }
      },
      uploadCover(event) {
        const file = event.target.files[0];
        if (file) {
          const reader = new FileReader();
          reader.onload = e => {
            this.bookCover = e.target.result;
          };
          reader.readAsDataURL(file);
        }
      },
      setDetailsHeight() {
        const detailsContainer = this.$refs.detailsContainer;
        if (detailsContainer) {
          detailsContainer.style.maxHeight = `${window.innerHeight}px`;
        }
      }
    }
  };
  </script>
  
  <style scoped>
  @import 'vue-multiselect/dist/vue-multiselect.css';

  .edit-book-container {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    gap: 20px;
  }

  .book-cover {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
  }

  .book-details {
    flex: 2;
    padding: 20px;
  }

  .details-container {
    overflow: hidden;
  }

  .cover-placeholder {
    width: 100%;
    max-width: 200px;
    margin-bottom: 20px;
  }

  .form-group {
    margin-bottom: 20px;
  }
  
  label {
    display: block;
    font-weight: bold;
  }
  
  input[type="text"],
  input[type="number"],
  textarea {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  button {
    padding: 8px 16px;
    border: none;
    border-radius: 4px;
    background-color: #007bff;
    color: #fff;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  </style>