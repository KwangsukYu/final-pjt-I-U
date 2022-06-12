<template>
  <div v-show="navState">
    <div class="menu-trigger" @click="navToggle">
      <span></span>
      <span></span>
      <span></span>
    </div>
    <nav v-if="isToggled">
      <div @click="intro" class="name-space">
        <img class="logo-img" src="@/assets/icon.png" alt="#" style="height: 50px; width: 50px;">
        <div class="pjt-name">U&I</div>
      </div>
      <router-link to="/home" id="neon-btn">
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      Home
      </router-link> 
      <router-link to="/genre" id="neon-btn">
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      Genre
      </router-link>
      <router-link to="/recommendation" id="neon-btn">
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      Recommendation
      </router-link> 
      <router-link to="/community" id="neon-btn">
      <span></span>
      <span></span>
      <span></span>
      <span></span>
      community
      </router-link> 
      <div class="empty"></div>
      <div class="profile">
        <div class="profile-icon">
            <div class="profile-btn icon-btn" :class="{ btnActivate:isProfile }" v-if="isLoggedIn" @click="fetchProfile(currentUser.username)">
              <i class="fa-solid fa-user"></i>
              <p>PROFILE</p>
            </div>
            <div v-else class="icon-btn" @click="moveToSignUp">
              <i class="fa-solid fa-user-plus" ></i>
              <p>SIGN-UP</p>
            </div>
          <div v-if="isLoggedIn" class="icon-btn" @click="loggedOut">
            <i class="fa-solid fa-arrow-right-from-bracket" ></i>
            <p>LOG-OUT</p>
          </div>
          <div v-else class="icon-btn" @click="moveToLogIn">
            <i class="fa-solid fa-arrow-right-to-bracket icon-btn" ></i>
            <p>LOG-IN</p>
          </div>
        </div>
        <div class="profile-detail">
          <div class="user-icon">
            <img src="@/assets/iu4.jpg" alt="iu" style="height: 60px; width: 60px; border-radius: 10px;">
          </div>
          <div v-if="isLoggedIn" class="user-detail">
            <p>Hello!</p>
            <p>{{ currentUser.username }}</p>
          </div>
          <div v-else class="user-detail">
            <p>Hi!</p>
            <p>Anonymous</p>
          </div>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'navigationBar',
  data() {
    return {
      isToggled: false,
    }
  },
  methods: {
    ...mapActions(['logout','fetchProfile']),
    loggedOut () {
      document.querySelector('.menu-trigger').click()
      this.logout()
    },
    navToggle (event) {
      this.isToggled = !this.isToggled
      event.currentTarget.classList.toggle('active-1')
    },
    moveToLogIn () {
      this.$router.push( {name: "login" } )
      document.querySelector('.menu-trigger').click()
    },
    moveToSignUp () {
      this.$router.push( { name: "signup"} )
      document.querySelector('.menu-trigger').click()
    },
    intro () {
      this.$router.push({name:'intro'})
    }

  },
  computed : {
    ...mapGetters(['isLoggedIn', 'currentUser', 'navState']),
    isProfile () {
      if ( this.$route.name === 'profile') {
        return true
      } else {
        return false
      }
    }
  }
}
</script>

<style scoped>

.menu-trigger {
  position: absolute;
  width: 25px;
  height: 22px;
  top : 7vh;
  right: 3.25vw;
  font-size: 30px;
  background: transparent;
  z-index: 101;
}

.menu-trigger span {
  display: inline-block;
  transition: all 0.4s;
  box-sizing: border-box;
  z-index: 101;
}

.menu-trigger span {
  position: absolute;
  left: 0;
  width: 100%;
  height: 4px;
  background-color: rgba(0, 0, 0, 0.3);
  border-radius: 4px;
  z-index: 101;
}

.menu-trigger span:nth-of-type(1) {
  top: 0;
}

.menu-trigger span:nth-of-type(2) {
  top: 9px;
}

.menu-trigger span:nth-of-type(3) {
  bottom: 0;
}

.menu-trigger.active-1 span:nth-of-type(1) {
  transform: translateY(9px) rotate(-45deg);
  background-color: white;
}

.menu-trigger.active-1 span:nth-of-type(2) {
  opacity: 0;
}

.menu-trigger.active-1 span:nth-of-type(3) {
  transform: translateY(-9px) rotate(45deg);
  background-color: white;
}

.nav-toggle {
  display: none;
}

nav {
  position: absolute;
  display: flex;
  flex-direction: column;
  top:5vh;
  height: 800px;
  right: 2%;
  backdrop-filter: blur(5px);
  border-radius: 10px;
  background: rgba(0, 0, 0, 0.3);
  box-shadow: 0 25px 45px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.5);
  border-right: 1px solid rgba(255, 255, 255, 0.2);
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
  min-height: 600px;
  animation: nav1 2s;
  z-index: 100;
}

@keyframes nav1 {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

.menu-trigger:hover {
  cursor: pointer;
}

.name-space {
  height: 20%;
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  margin-top: 15px;
  margin-bottom: 20px;
}

.logo {
  position: absolute;
}

.logo-img {
  border-radius: 10px;
}

.pjt-name {
  color: white;
  font-size: 50px;
  letter-spacing: 10px;
  font-family: 'Grape Nuts', cursive;
}

.empty {
  height: 25%;
}

.profile {
  height: 20vh;
  bottom: 0%;
}

.profile-icon {
  display: flex;
  justify-content: center;
  height: 35%;
  align-items: center;
  font-size: 20px;
  color: white;
}

.profile-icon i {
  margin-left: 25px;
  margin-right: 25px;
  margin-bottom: 10px;
  display: block;
}

.profile-icon div {
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  align-items: center;
}

.profile-icon p {
  margin: 0;
  font-size: 12px;
}

.profile-detail {
  height: 65%;
  display: flex;
  justify-content: center;
  align-items: center;
}

nav a {
  font-weight: bold;
  color: white;
}

.user-detail {
  color: white;
  width: 50%;
}

.user-detail p {
  margin: 5px;
  text-align: start;
  font-size: 20px;
  font-family: 'Grape Nuts', cursive;
}

.user-icon {
  width: 50%;
}

#neon-btn {
  position: relative;
  display: inline-block;
  padding: 20px 20px;
  margin: 40px, 0;
  font-size: 16px;
  text-decoration: none;
  text-transform: uppercase;
  overflow: hidden;
  transition: 0.5s;
  letter-spacing: 4px;
  font-family: 'Grape Nuts', cursive;
}

#neon-btn:hover {
  background: white;
  color: #666;
  box-shadow: 0 0 3px white,
              0 0 6px white,
              0 0 12.5px white,
              0 0 25px white;
  transform: scale(1.03);
}

nav a.router-link-exact-active span {
  position: absolute;
  display: block;
}

nav a.router-link-exact-active span:hover {
  animation-play-state: paused;
}

nav a.router-link-exact-active span:nth-child(1) {
  top: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background: linear-gradient(90deg, transparent, white);
  animation: animate1 1s linear infinite;
}

@keyframes animate1{
  0% {
    left: -100%
  }
  50%, 100% {
    left: 100%
  }
}

nav a.router-link-exact-active span:nth-child(2) {
  top: -100%;
  right: 0;
  width: 2px;
  height: 100%;
  background: linear-gradient(180deg, transparent, white);
  animation: animate2 1s linear infinite;
  animation-delay: 0.25s;
}

@keyframes animate2{
  0% {
    top: -100%
  }
  50%, 100% {
    top: 100%
  }
}

nav a.router-link-exact-active span:nth-child(3) {
  bottom: 0%;
  right: -100%;
  width: 100%;
  height: 2px;
  background: linear-gradient(270deg, transparent, white);
  animation: animate3 1s linear infinite;
  animation-delay: 0.5s;
}

@keyframes animate3{
  0% {
    right: -100%
  }
  50%, 100% {
    right: 100%
  }
}

nav a.router-link-exact-active span:nth-child(4) {
  bottom: 100%;
  left: 0;
  width: 2px;
  height: 100%;
  background: linear-gradient(360deg, transparent, white);
  animation: animate4 1s linear infinite;
  animation-delay: 0.75s;
}

@keyframes animate4{
  0% {
    bottom: -100%
  }
  50%, 100% {
    bottom: 100%
  }
}

.icon-btn:hover {
  transform: scale(1.2);
  cursor: pointer;
}

.btnActivate {
  background-color: rgba(255,255,255,0.3);
  border-radius: 10px;
  padding-top: 10px;
  padding-bottom: 10px;
}

</style>