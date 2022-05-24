<template>
  <div>
    <div v-if="isLoggedIn">
      <div>
        바쁜 벌꿀은 영화볼 시간도 없습니다.
        영화볼 시간도 없는 당신을 위한 영화 추천 서비스 Beesy Bee
      </div>
      <costeffective-movie></costeffective-movie>
      <occupation-movie></occupation-movie>
      <age-movie></age-movie>
      <gender-movie></gender-movie>
    </div>
    <div v-if="!isLoggedIn">
      <div class="beesy d-flex align-items-center">
        <div class="container d-flex flex-column align-items-cneter">
          <h1>BEESY MOVIE</h1>
          <h2>바쁜 벌꿀은 영화볼 시간도 없다</h2>
          <span><router-link :to="{ name: 'login' }" style="text-decoration:none">로그인</router-link></span>
          <span><router-link :to="{ name: 'signup' }" style="text-decoration:none">회원가입</router-link></span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import CosteffectiveMovie from '@/components/CosteffectiveMovie.vue'
import OccupationMovie from '@/components/OccupationMovie.vue'
import AgeMovie from '@/components/AgeMovie.vue'
import GenderMovie from '@/components/GenderMovie.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  name : 'HomeView',
  components : {
    OccupationMovie,
    CosteffectiveMovie,
    AgeMovie,
    GenderMovie,
  },
  methods: {
    ...mapActions(['setAgeMovies', 'setGenderMovies', 'setOccupationMovies', 'fetchCurrentUser',  'setCosteffectiveMovies', 'setCosteffectiveMovies'])
  },
  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser',]), 
  },
  watch : {
    currentUser : function () {
      this.setAgeMovies(this.currentUser.username)
      this.setGenderMovies(this.currentUser.username)
      this.setOccupationMovies(this.currentUser.username)
      this.setCosteffectiveMovies()
     }
  },
  created(){
      this.fetchCurrentUser()
    },

  
}
</script>

<style>
a { text-decoration:none }

.beesy {
  width: 100%;
  height: 100vh;
  background: url("../images/beesyhome.png") top right;
  background-size: cover;
}
.beesy .container {
  padding-top: 70px;
  position: relative;  
}
@media (max-width: 992px) {
  .beesy .container {
    padding-top: 58px;
  }
}
.beesy h1 {
  margin: 0;
  font-size: 48px;
  font-weight: 700;
  line-height: 56px;
  color: #222222;
}
.beesy h2 {
  color: #6f6f6f;
  margin: 10px 0 0 0;
  font-size: 22px;
}
.beesy a {
  font-family: "Raleway", sans-serif;
  text-transform: uppercase;
  font-weight: 600;
  font-size: 12px;
  letter-spacing: 1px;
  display: inline-block;
  padding: 12px 40px;
  border-radius: 50px;
  transition: 0.5s;
  margin-top: 30px;
  color: #fff;
  background: #7C683C;
}
.beesy a:hover {
  background: #7C683C;
}
@media (min-width: 1024px) {
  .beesy {
    background-attachment: fixed;
  }
}
@media (max-width: 992px) {
  .beesy:before {
    content: "";
    background: rgba(255, 255, 255, 0.8);
    position: absolute;
    bottom: 0;
    top: 0;
    left: 0;
    right: 0;
  }
  .beesy h1 {
    font-size: 28px;
    line-height: 36px;
  }
  .beesy h2 {
    font-size: 18px;
    line-height: 24px;
  }
}
</style>
