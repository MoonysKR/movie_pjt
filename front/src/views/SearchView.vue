<template>
  <div class="d-flex justify-content-center">
    <div class="row">
      <search-list :searchmovies="searchMovies.results">
      </search-list>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import SearchList from '@/components/SearchList.vue'

export default {
  name : 'SearchView',
  components : {
    SearchList
  },
  methods: {
    ...mapActions(['fetchCurrentUser', 'setSearchMovies'])
  },
  computed : {
    ...mapGetters(['searchMovies']),
    searchedmoive : function (){
      return this.$route.query.searchMovie
    }
  },
  beforeCreate() {
  },
  created() {
    this.setSearchMovies(this.$route.query.searchMovie)
  },
  watch : {
    searchedmoive : function () {
      this.setSearchMovies(this.$route.query.searchMovie)
     }
  }
}
</script>

<style>

</style>