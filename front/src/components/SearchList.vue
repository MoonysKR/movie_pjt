<template>
<div>
  <div class="card" v-for="searchmovie in searchmovies" :key="searchmovie.id">
    <div class="card-body">
      <div class="col-10">
        <router-link :to =" { name : 'detail', query : {id : searchmovie.id,} }" class="card-title">
          {{ searchmovie.title }}
        </router-link>
        <p class="card-text">{{ searchmovie.overview }}</p>
      </div> 
    </div>
  </div>
</div>
</template>

<script>
export default {
  name : 'SearchList',
  props : {
    searchmovies : Array
  }
}
</script>

<style>

</style>