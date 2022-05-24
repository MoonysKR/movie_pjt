<template>
  <div v-if="selectedVideo" class="video-detail">
    <div class="video-container">
      <iframe :src="videoUrl" frameborder="0"></iframe>
    </div>
  </div>
</template>

<script>
export default {
  name: 'VideoComponent',
  props: {
    selectedVideo: Object
  },
  computed: {
    videoUrl: function () {
      const videoId = this.selectedVideo.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  }

}

</script>

<style>

</style>