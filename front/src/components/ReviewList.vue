<template>
  <div>
    <review-list-item class="col-10"
          v-for="review in reviews"
          :key="review.id"
          :review="review">
    </review-list-item>
    <review-list-form>
      
    </review-list-form>
  </div>
</template>

<script>
import ReviewListItem from '@/components/ReviewListItem.vue'
import ReviewListForm from '@/components/ReviewListForm.vue'

export default {
  name : 'ReviewList',
  components : {
    ReviewListItem,
    ReviewListForm
  },
  props : { reviews : Array },
}
</script>

<style>

</style>