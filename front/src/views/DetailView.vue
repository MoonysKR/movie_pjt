<template>
  <div>
    <div>
      <button @click="spoiler_change">{{ spoiler }}</button>
      <div class="card" style="width: 18rem;">
        <img src="" class="card-img-top" alt="...">
        <div class="card-body">
          <h1>{{detailMovie.title}}</h1>
          <p class="card-text"> {{ detailMovie.overview }}</p>
        </div>
      </div>
      <div class="video-container">
        <video-item :selected-video="selectedVideo"></video-item>
      </div>
      <review-list :reviews="detailMovie.review_set"></review-list>

    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import ReviewList from '@/components/ReviewList.vue'
import VideoItem from '@/components/VideoItem.vue'
import axios from 'axios'

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name : 'DetailView',
  data() {
    return {
      spoiler: false,
      videos: [],
      selectedVideo: null
    }
  },
  components : {
    ReviewList,
    VideoItem
  },
  methods : {
    ...mapActions(['setDetailMovie']),
    spoiler_change() {
      this.spoiler = !this.spoiler
    },
    loadVideo() {
      if (this.spoiler) {
        let params = {
          key: API_KEY,
          part: 'snippet',
          type: 'video',
          q: this.detailMovie.title + ' 예고편'
        }
        axios({
        method: 'GET',
        url: API_URL,
        params,
        })
        .then(res => {
          this.videos = res.data.items
          this.selectedVideo = this.videos[0]
        })
        .catch(res => {
          console.log(res)
        })
      } else {
        let params = {
          key: API_KEY,
          part: 'snippet',
          type: 'video',
          q: this.detailMovie.title + '영화 리뷰'
        }
        axios({
          method: 'GET',
          url: API_URL,
          params
        })
          .then(res => {
            this.videos = res.data.items
            this.selectedVideo = this.videos[0]
          })
          .catch(err => {
            console.log(err)
          })
      }
    }
  },
  computed : {
    ...mapGetters(['detailMovie']),
    videoUrl: function () {
      const videoId = this.selectedVideo.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  },
  watch : {
    detailMovie : function () {
      this.loadVideo()
     }
  },
  created() {
    this.setDetailMovie(this.$route.query.id)
  },

}

</script>

<style>

</style>