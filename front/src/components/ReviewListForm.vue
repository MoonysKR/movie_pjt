<template>
  <form @submit.prevent="onSubmit" class="review-list-form">
    <label for="review">review: </label>
    
    <input type="text" id="comment" v-model="content" required>
    <b-form-rating v-model="rate" > </b-form-rating>
    <p class="mt-2">Rate: {{ rate }}</p>
    
    <button>Review</button>

  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import { BFormRating } from 'bootstrap-vue'

export default {
  name: 'CommentListForm',
  data() {
    return {
      content: '',
      rate : null
    }
  },
  components : {
    BFormRating
  },
  computed : {
    ...mapGetters(['detailMovie', 'currentUser'])
  },
  methods: {
    ...mapActions(['createReview', 'fetchCurrentUser']),
    onSubmit() {
      const movieId = this.detailMovie.id
      console.log(movieId)
      this.createReview({ moviePk : movieId, content: this.content, rate : this.rate })
      this.content = ''
    }
  },
}
</script>

<style>
.review-list-form {
  border: 1px solid black;
  margin: 1rem;
  padding: 1rem;
}
</style>