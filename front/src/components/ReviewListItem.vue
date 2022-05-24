<template>
  <div>
    <span v-if="isEditing">
      <input type="text" v-model="payload.content" value="payload.content">
      <b-form-rating v-model="payload.rate" value="payload.rate"> </b-form-rating>
      
      <button @click="onUpdate">Update</button> |
      <button @click="switchIsEditing">Cancle</button>
    </span>
    <span v-if="currentUser.username === review.user.username && !isEditing">
      {{ review.user.username }}
      {{ review.content }}
      <button @click="switchIsEditing">Edit</button> |
      <button @click="deleteReview(payload)">Delete</button>
    </span>
  </div>
</template>

<script>

import { mapGetters, mapActions } from 'vuex'

export default {
  name : 'ReviewListItem',
  props : { review : Object },
  data () {
    return {
      isEditing: false,
      payload: {
        moviePk: this.review.movie,
        reviewPk: this.review.pk,
        content: this.review.content,
        rate : this.review.rate,
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateReview', 'deleteReview']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      console.log(this.payload)
      this.updateReview(this.payload)
      this.isEditing = false
    }
  },

}
</script>

<style>

</style>