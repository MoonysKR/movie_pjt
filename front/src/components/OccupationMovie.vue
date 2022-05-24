<template>
  <div>
    <h3 style="background-color: #FFCC5B">직업별 영화 추천</h3>
    <div class="">
    
      <div id="carouselExampleControls2" class="carousel slide carousel-fade" data-ride="carousel">
        <div class="carousel-inner">
          <div class="carousel-item active container">
            <div class="row">
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[0].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[0].poster_path}`" class="card-img-top" alt="...">
                </router-link>
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[1].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[1].poster_path}`" class="card-img-top" alt="...">
                </router-link>
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[2].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[2].poster_path}`" class="card-img-top" alt="...">
                </router-link>
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[3].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[3].poster_path}`" class="card-img-top" alt="...">
                </router-link>
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[4].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[4].poster_path}`" class="card-img-top" alt="...">
                </router-link>
              </div>
            </div>
          </div>
          <div class="carousel-item container">
            <div class="row">
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[5].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[5].poster_path}`" class="card-img-top" alt="...">
                </router-link>
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[6].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[6].poster_path}`" class="card-img-top" alt="...">
                </router-link>
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[7].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[7].poster_path}`" class="card-img-top" alt="...">
                </router-link>
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[8].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[8].poster_path}`" class="card-img-top" alt="...">
                </router-link>
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[9].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[9].poster_path}`" class="card-img-top" alt="...">
                </router-link>
              </div>
            </div>
          </div>
          <div class="carousel-item container">
            <div class="row">
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[10].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[10].poster_path}`" class="card-img-top" alt="...">
                </router-link>
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[11].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[11].poster_path}`" class="card-img-top" alt="...">
                </router-link>
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[12].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[12].poster_path}`" class="card-img-top" alt="...">
                </router-link>
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[13].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[13].poster_path}`" class="card-img-top" alt="...">
                </router-link>
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[14].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[14].poster_path}`" class="card-img-top" alt="...">
                </router-link>
              </div>
            </div>
          </div>
          <div class="carousel-item container">
            <div class="row">
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[15].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[15].poster_path}`" class="card-img-top" alt="...">
                </router-link>
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[16].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[16].poster_path}`" class="card-img-top" alt="...">
                </router-link>
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[17].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[17].poster_path}`" class="card-img-top" alt="...">
                </router-link>
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[18].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[18].poster_path}`" class="card-img-top" alt="...">
                </router-link>
              </div>
              <div class="card col-2" style="width: 18rem;">
                <router-link :to =" { name : 'detail', query : { id : `${occupationMovies.results[19].id}` } }">
                  <img :src="`https://image.tmdb.org/t/p/original/${occupationMovies.results[19].poster_path}`" class="card-img-top" alt="...">
                </router-link>
              </div>
            </div>
          </div>
        </div>
        <a class="carousel-control-prev" href="#carouselExampleControls2" role="button" data-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="sr-only">Previous</span>
        </a>
        <a class="carousel-control-next" href="#carouselExampleControls2" role="button" data-slide="next">
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
  name : 'OccupationMovies',
  computed: {
    ...mapGetters(['occupationMovies', 'currentsUser']), 
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