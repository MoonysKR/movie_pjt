<template>
  <div>
    <div v-if="isEditing">
      <update-profile :profile="profile" @is-editing-changed="switching"></update-profile>
    </div>
    <div class="wrapper-login fadeInDown-login" v-if="!isEditing">
      <div id="formContent-login">
        <!-- Tabs Titles -->
        <!-- Icon -->
        <div class="fadeIn-login first-login">
          <img src="../images/bee.png" id="icon" alt="User Icon" />
        </div>
        <!-- Login Form -->
        <div v-if="!isEditing">
          <p style="height : 10px"></p>
            <h2 class="mypage-h2">꿀벌 카드</h2>
          <p style="height : 10px"></p>
          <div class="fadeIn-login first-login text-login">
            <div class="row">
              <div class="col-6">
                ID
              </div>
              <div class="col-6">
                <strong>{{ profile.username }}</strong>
              </div>
            </div>
          </div>

          <div class="fadeIn-login second-login text-login">
            <div class="row">
              <div class="col-6">
                나이
              </div>
              <div class="col-6">
                <strong>{{ profile.age }}</strong>
              </div>
            </div>
          </div>
          <div class="fadeIn-login third-login text-login">
            <div class="row">
              <div class="col-6">
                성별
              </div>
              <div class="col-6">
                <strong v-if="profile.gender === 'M'"> 남자 </strong>
                <strong v-if="profile.gender === 'F'"> 여자 </strong>
              </div>
            </div>
          </div>
          <div class="fadeIn-login fourth-login text-login">
            <div class="row">
              <div class="col-6">
                직업
              </div>
              <div class="col-6">
                <strong v-if="profile.occupation === '0'"> 기타 </strong>
                <strong v-if="profile.occupation === '1'"> 교육자 </strong>
                <strong v-if="profile.occupation === '2'"> 예술가 </strong>
                <strong v-if="profile.occupation === '3'"> 사무관리직 </strong>
                <strong v-if="profile.occupation === '4'"> 대학생 및 대학원생 </strong>
                <strong v-if="profile.occupation === '5'"> 서비스업 종사자 </strong>
                <strong v-if="profile.occupation === '6'"> 의사 및 의료계 종사자 </strong>
                <strong v-if="profile.occupation === '7'"> 임원 및 관리자 </strong>
                <strong v-if="profile.occupation === '8'"> 농부 </strong>
                <strong v-if="profile.occupation === '9'"> 전업주부 </strong>
                <strong v-if="profile.occupation === '10'"> 청소년 및 학생 </strong>
                <strong v-if="profile.occupation === '11'"> 법조인 </strong>
                <strong v-if="profile.occupation === '12'"> 프로그래머 </strong>
                <strong v-if="profile.occupation === '13'"> 은퇴 </strong>
                <strong v-if="profile.occupation === '14'"> 영업 및 마케팅 </strong>
                <strong v-if="profile.occupation === '15'"> 과학자 </strong>
                <strong v-if="profile.occupation === '16'"> 프리랜서 </strong>
                <strong v-if="profile.occupation === '17'">기계공 및 엔지니어</strong>
                <strong v-if="profile.occupation === '18'">소상공인</strong>
                <strong v-if="profile.occupation === '19'">백수</strong>
                <strong v-if="profile.occupation === '20'">작가</strong>
              </div>
            </div>
          </div>
          <p style="height : 50px"></p>
          <div id="formfooter-login">
            <button @click="switching" class="btn" style="color: #FFCC5B; font-weight: bolder; font-size: 20px;" > 꿀벌 카드 수정 </button>
          </div>
        </div>
      </div>
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





/* STRUCTURE */
.mypage-h2 {
  font-family: 'Black Han Sans', sans-serif;
  font-size: 3em;
}

.wrapper-login {
  display: flex;
  align-items: center;
  flex-direction: column; 
  justify-content: center;
  width: 100%;
  min-height: 100%;
  padding: 20px;
}

#formContent-login {
  -webkit-border-radius: 10px 10px 10px 10px;
  border-radius: 10px 10px 10px 10px;
  background: #FFCC5B;
  padding: 30px;
  width: 90%;
  max-width: 450px;
  position: relative;
  padding: 0px;
  -webkit-box-shadow: 0 30px 60px 0 rgba(0,0,0,0.3);
  box-shadow: 0 30px 60px 0 rgba(0,0,0,0.3);
  text-align: center;
}

#formfooter-login {
  background-color: #7C683C;
  border-top: 1px solid #7C683C;
  padding: 25px;
  text-align: center;
  -webkit-border-radius: 0 0 10px 10px;
  border-radius: 0 0 10px 10px;
}



/* TABS */

h2.inactive {
  color: #FFCC5B;
}

h2.active {
  color: #0d0d0d;
  border-bottom: 2px solid #C7EBEF;
}



/* FORM TYPOGRAPHY*/

input[type=button], .submit-login, input[type=reset]  {
  background-color: #7C683C;
  border: none;
  color: #FFCC5B;
  padding: 15px 80px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  text-transform: uppercase;
  font-size: 13px;
  -webkit-box-shadow: 0 10px 30px 0 rgba(95,186,233,0.4);
  box-shadow: 0 10px 30px 0 rgba(95,186,233,0.4);
  -webkit-border-radius: 5px 5px 5px 5px;
  border-radius: 5px 5px 5px 5px;
  margin: 5px 20px 40px 20px;
  -webkit-transition: all 0.3s ease-in-out;
  -moz-transition: all 0.3s ease-in-out;
  -ms-transition: all 0.3s ease-in-out;
  -o-transition: all 0.3s ease-in-out;
  transition: all 0.3s ease-in-out;
}

input[type=button]:hover, .submit-login:hover, input[type=reset]:hover  {
  background-color: #7C683C;
}

input[type=button]:active, .submit-login:active, input[type=reset]:active  {
  -moz-transform: scale(0.95);
  -webkit-transform: scale(0.95);
  -o-transform: scale(0.95);
  -ms-transform: scale(0.95);
  transform: scale(0.95);
}

.text-login {
  background-color: #C7EBEF;
  border: none;
  color: #0d0d0d;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 5px;
  width: 85%;
  border: 2px solid #C7EBEF;
  -webkit-transition: all 0.5s ease-in-out;
  -moz-transition: all 0.5s ease-in-out;
  -ms-transition: all 0.5s ease-in-out;
  -o-transition: all 0.5s ease-in-out;
  transition: all 0.5s ease-in-out;
  -webkit-border-radius: 5px 5px 5px 5px;
  border-radius: 5px 5px 5px 5px;
}

.text-login:focus {
  background-color: #C7EBEF;
  border-bottom: 2px solid #7C683C;
}

.text-login:placeholder {
  color: #C7EBEF;
}

.pwd-login {
  background-color: #C7EBEF;
  border: none;
  color: #0d0d0d;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 5px;
  width: 85%;
  border: 2px solid #C7EBEF;
  -webkit-transition: all 0.5s ease-in-out;
  -moz-transition: all 0.5s ease-in-out;
  -ms-transition: all 0.5s ease-in-out;
  -o-transition: all 0.5s ease-in-out;
  transition: all 0.5s ease-in-out;
  -webkit-border-radius: 5px 5px 5px 5px;
  border-radius: 5px 5px 5px 5px;
}

.pwd-login:focus {
  background-color: #C7EBEF;
  border-bottom: 2px solid #7C683C;
}

.pwd-login:placeholder {
  color: #C7EBEF;
}

/* ANIMATIONS */

/* Simple CSS3 Fade-in-down Animation */
.fadeInDown-login {
  -webkit-animation-name: fadeInDown;
  animation-name: fadeInDown;
  -webkit-animation-duration: 1s;
  animation-duration: 1s;
  -webkit-animation-fill-mode: both;
  animation-fill-mode: both;
}

@keyframes fadeInDown {
  0% {
    opacity: 0;
    -webkit-transform: translate3d(0, -100%, 0);
    transform: translate3d(0, -100%, 0);
  }
  100% {
    opacity: 1;
    -webkit-transform: none;
    transform: none;
  }
}

@keyframes fadeInDown-login {
  0% {
    opacity: 0;
    -webkit-transform: translate3d(0, -100%, 0);
    transform: translate3d(0, -100%, 0);
  }
  100% {
    opacity: 1;
    -webkit-transform: none;
    transform: none;
  }
}

/* Simple CSS3 Fade-in Animation */
@-webkit-keyframes fadeIn { from { opacity:0; } to { opacity:1; } }
@-moz-keyframes fadeIn { from { opacity:0; } to { opacity:1; } }
@keyframes fadeIn { from { opacity:0; } to { opacity:1; } }

.fadeIn-login {
  opacity:0;
  -webkit-animation:fadeIn ease-in 1;
  -moz-animation:fadeIn ease-in 1;
  animation:fadeIn ease-in 1;

  -webkit-animation-fill-mode:forwards;
  -moz-animation-fill-mode:forwards;
  animation-fill-mode:forwards;

  -webkit-animation-duration:1s;
  -moz-animation-duration:1s;
  animation-duration:1s;
}

.fadeIn-login.first-login {
  -webkit-animation-delay: 0.4s;
  -moz-animation-delay: 0.4s;
  animation-delay: 0.4s;
}

.fadeIn-login.second-login {
  -webkit-animation-delay: 0.6s;
  -moz-animation-delay: 0.6s;
  animation-delay: 0.6s;
}

.fadeIn-login.third-login {
  -webkit-animation-delay: 0.8s;
  -moz-animation-delay: 0.8s;
  animation-delay: 0.8s;
}

.fadeIn-login.fourth-login {
  -webkit-animation-delay: 1s;
  -moz-animation-delay: 1s;
  animation-delay: 1s;
}

/* Simple CSS3 Fade-in Animation */
.underlineHover:after {
  display: block;
  left: 0;
  bottom: -10px;
  width: 0;
  height: 2px;
  background-color: #C7EBEF;
  content: "";
  transition: width 0.2s;
}

.underlineHover:hover {
  color: #0d0d0d;
}

.underlineHover:hover:after{
  width: 100%;
}



/* OTHERS */

*:focus {
    outline: none;
} 

#icon {
  width:60%;
}

</style>