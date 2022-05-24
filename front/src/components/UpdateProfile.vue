<template>
  <div>
    <button @click="switching">
      취소
    </button> |
    <button @click="onUpdate">
      수정완료
    </button>
    <p>아이디: {{ payload.username }}</p>
    <p>나이: <input type="text" v-model="payload.age" value="payload.age"></p>
    <p>성별: <input type="text" v-model="payload.gender" value="payload.gender"></p>
    <p>직업: <input type="text" v-model="payload.occupation" value="payload.occupation"></p>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'UpdateProfile',
  props: {
    profile: Object,
  },
  data() {
    return {
      payload: {
        username: this.profile.username,
        age: this.profile.age,
        occupation: this.profile.occupation,
        gender: this.profile.gender,
      }
    }
  },
  methods: {
    ...mapActions(['updateProfile']),
    switching() {
      this.$emit('is-editing-changed')
    },
    onUpdate() {
      this.updateProfile(this.payload)
      this.$emit('is-editing-changed')
    }
  },
}
</script>

<style>

</style>