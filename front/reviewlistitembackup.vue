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



<div>
  <span v-if="isEditing">
    <input type="text" v-model="payload.content" value="payload.content">
    <b-form-rating v-model="payload.rate" value="payload.rate"> </b-form-rating>
    
    <button @click="onUpdate">Update</button> |
    <button @click="switchIsEditing">Cancle</button>
  </span>
  <div v-if="!isEditing" class="main-div-reviewlistitem">
    <div class="d-flex flex-column comment-section">
      <div class="bg-white p-2">
        <div class="d-flex flex-row user-info justify-content-between">
          <div class="d-flex flex-column justify-content-start ml-2">
            <!-- 네임 -->
            <span class="d-block font-weight-bold name-revielistitem">
              {{ review.user.username }}
            </span>

          </div>
          <div>
            <!-- 평점 -->
            <div v-if="review.rate===1">
              <i class="fa-solid fa-star fa-xl" style="color : #FFCC5B;"></i>
            </div>
            <div v-if="review.rate===2">
              <i class="fa-solid fa-star fa-xl" style="color : #FFCC5B;"></i>
              <i class="fa-solid fa-star fa-xl" style="color : #FFCC5B;"></i>
            </div>           
            <div v-if="review.rate===3">
              <i class="fa-solid fa-star fa-xl" style="color : #FFCC5B;"></i>
              <i class="fa-solid fa-star fa-xl" style="color : #FFCC5B;"></i>
              <i class="fa-solid fa-star fa-xl" style="color : #FFCC5B;"></i>
            </div>
            <div v-if="review.rate===4">
              <i class="fa-solid fa-star fa-xl" style="color : #FFCC5B;"></i>
              <i class="fa-solid fa-star fa-xl" style="color : #FFCC5B;"></i>
              <i class="fa-solid fa-star fa-xl" style="color : #FFCC5B;"></i>
              <i class="fa-solid fa-star fa-xl" style="color : #FFCC5B;"></i>
            </div>            
            <div v-if="review.rate===5">
              <i class="fa-solid fa-star fa-xl" style="color : #FFCC5B;"></i>
              <i class="fa-solid fa-star fa-xl" style="color : #FFCC5B;"></i>
              <i class="fa-solid fa-star fa-xl" style="color : #FFCC5B;"></i>
              <i class="fa-solid fa-star fa-xl" style="color : #FFCC5B;"></i>
              <i class="fa-solid fa-star fa-xl" style="color : #FFCC5B;"></i>
            </div>
          </div>
          <div>
            <!-- 수정 / 삭제 -->
            <span v-if="currentUser.username === review.user.username && !isEditing">
              <button @click="switchIsEditing" class="btn btn-primary">수정</button> |
              <button @click="deleteReview(payload)" class="btn btn-danger">삭제</button>
            </span>
          </div>
        </div>
        <!-- 내용 --> 
        <div class="mt-2">
          <p class="comment-text"> {{ review.content }}</p>
        </div>
      </div>
    </div>
  </div>

</div>