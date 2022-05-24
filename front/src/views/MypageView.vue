<template>
  <div>
    <div v-if="isEditing">
      <update-profile :profile="profile" @is-editing-changed="switching"></update-profile>
    </div>
    <div v-if="!isEditing">
      <button @click="switching">
        회원 정보 수정
      </button>
      <p>아이디: {{ profile.username }}</p>
      <p>나이: {{ profile.age }}</p>
      <p>성별: {{ profile.gender }}</p>
      <p>직업: {{ profile.occupation }}</p>
    </div>
  </div>
</template>

<script>
import UpdateProfile from '@/components/UpdateProfile.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'MypageView',
  components: { UpdateProfile },
  data() {
    return {
      isEditing: false
    }
  },
  computed: {
    ...mapGetters(['profile'])
  },
  methods: {
    ...mapActions(['fetchProfile']),
    switching() {
      this.isEditing = !this.isEditing
    },
  },
  created() {
    this.fetchProfile()
  }
}
</script>

<style>

</style>