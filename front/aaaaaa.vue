<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light" >
    <div class="collapse navbar-collapse " id="navbarNavAltMarkup">
      <div class="navbar-nav d-flex align-items-center">
        <li class="nav-item nav-link">
          <img src="../images/bee.png" alt="" srcset="" class="img-fluid" width="110">
        </li>
        <li class="nav-item nav-link">
          <router-link :to="{ name: 'home' }">Home</router-link>
        </li>
        <form class="form-inline">
            <input @keydown.enter.prevent="movieSearch(searchMovie)" class="form-control mr-sm-2" type="search" placeholder="영화명 검색" aria-label="Search" v-model="searchMovie">
            <router-link :to=" {name : 'search', query: { searchMovie } }">검색</router-link>
        </form>
        <li class="nav-item nav-link " v-if="!isLoggedIn">
          <router-link :to="{ name: 'login' }">로그인</router-link>
        </li>
        <li class="nav-item nav-link " v-if="!isLoggedIn">
          <router-link :to="{ name: 'signup' }">회원가입</router-link>
        </li>
        <li class="nav-item nav-link " v-if="isLoggedIn">
          <router-link :to="{ name: 'logout' }">로그아웃</router-link>
        </li>
        <li class="nav-item nav-link " v-if="isLoggedIn" @click="fetchProfile()">
          <router-link :to="{ name: 'mypage' }">{{ username }}</router-link>
        </li>
      </div>
    </div>
  </nav>
 

</template>

<script>
  import { mapGetters } from 'vuex'
  import { mapActions } from 'vuex'
  
  export default {
    name: 'NavBar',
    data() {
      return {
        searchMovie : ''
      }
    },
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    },
    methods : {
      ...mapActions(['fetchProfile']),
      movieSearch : function (searchMovie) {
        this.$router.push( {name : 'search', query: { searchMovie } }  )
        this.searchMovie = ''
      }
    },
    components: {

    }
  }
</script>

<style></style>
