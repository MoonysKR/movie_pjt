<template>
  <div>
    <h3 style="background-color: #FFCC5B">가성비 영화 추천 </h3>
    <div class="">
    
      <div id="carouselExampleControls4" class="carousel slide carousel-fade" data-ride="carousel">
        <div class="carousel-inner">
          <div class="carousel-item active container">
            <div class="row">
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[0][1]}` } }">
                  <img :src="`${costeffectiveMovies[0][2]}`" class="card-img-top" alt="...">
                </router-link>                
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[1][1]}` } }">
                <img :src="`${costeffectiveMovies[1][2]}`" class="card-img-top" alt="...">
                </router-link>                
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[2][1]}` } }">
                <img :src="`${costeffectiveMovies[2][2]}`" class="card-img-top" alt="...">
                </router-link>                
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[3][1]}` } }">
                <img :src="`${costeffectiveMovies[3][2]}`" class="card-img-top" alt="...">
                </router-link>                
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[4][1]}` } }">
                <img :src="`${costeffectiveMovies[4][2]}`" class="card-img-top" alt="...">
                </router-link>                
              </div>
            </div>
          </div>
          <div class="carousel-item container">
            <div class="row">
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[5][1]}` } }">
                <img :src="`${costeffectiveMovies[5][2]}`" class="card-img-top" alt="...">
                </router-link>                
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[6][1]}` } }">
                <img :src="`${costeffectiveMovies[6][2]}`" class="card-img-top" alt="...">
                </router-link>                
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[7][1]}` } }">
                <img :src="`${costeffectiveMovies[7][2]}`" class="card-img-top" alt="...">
                </router-link>                
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[8][1]}` } }">
                <img :src="`${costeffectiveMovies[8][2]}`" class="card-img-top" alt="...">
                </router-link>                
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[9][1]}` } }">
                <img :src="`${costeffectiveMovies[9][2]}`" class="card-img-top" alt="...">
                </router-link>                
              </div>
            </div>
          </div>
          <div class="carousel-item container">
            <div class="row">
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[10][1]}` } }">
                <img :src="`${costeffectiveMovies[10][2]}`" class="card-img-top" alt="...">
                </router-link>                
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[11][1]}` } }">
                <img :src="`${costeffectiveMovies[11][2]}`" class="card-img-top" alt="...">
                </router-link>                
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[12][1]}` } }">
                <img :src="`${costeffectiveMovies[12][2]}`" class="card-img-top" alt="...">
                </router-link>                
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[13][1]}` } }">
                <img :src="`${costeffectiveMovies[13][2]}`" class="card-img-top" alt="...">
                </router-link>                
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[14][1]}` } }">
                <img :src="`${costeffectiveMovies[14][2]}`" class="card-img-top" alt="...">
                </router-link>                
              </div>
            </div>
          </div>
          <div class="carousel-item container">
            <div class="row">
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[15][1]}` } }">
                <img :src="`${costeffectiveMovies[15][2]}`" class="card-img-top" alt="...">
                </router-link>                
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[16][1]}` } }">
                <img :src="`${costeffectiveMovies[16][2]}`" class="card-img-top" alt="...">
                </router-link>                
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[17][1]}` } }">
                <img :src="`${costeffectiveMovies[17][2]}`" class="card-img-top" alt="...">
                </router-link>                
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[18][1]}` } }">
                <img :src="`${costeffectiveMovies[18][2]}`" class="card-img-top" alt="...">
                </router-link>                
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${costeffectiveMovies[19][1]}` } }">
                <img :src="`${costeffectiveMovies[19][2]}`" class="card-img-top" alt="...">
                </router-link>                
              </div>
            </div>
          </div>
        </div>
        <a class="carousel-control-prev" href="#carouselExampleControls4" role="button" data-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="sr-only">Previous</span>
        </a>
        <a class="carousel-control-next" href="#carouselExampleControls4" role="button" data-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="sr-only">Next</span>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'


export default {
  name : 'CosteffectiveMovies',
  computed: {
    ...mapGetters(['costeffectiveMovies', 'currentsUser']), 
  },
}
</script>

<style>
.card {
  margin: 0 0.5em;
  box-shadow: 2px 6px 8px 0 rgba(22, 22, 26, 0.18);
  border: none;
  border-radius: 0;
}
.carousel-inner {
  padding: 1em;
}
.row {
  display: flex;
  justify-content: center;
}
.card img {
  max-width: 100%;
  max-height: 100%;
}
.carousel-control-prev,
.carousel-control-next {
  background-color: #e1e1e1;
  width: 5vh;
  height: 5vh;
  border-radius: 50%;
  top: 50%;
  transform: translateY(-50%);
}
</style>