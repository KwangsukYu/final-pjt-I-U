<template>
  <div>
  <section>
    <div :class="{banner:isActive, a:true}">
      <div :class="{blocks:isActive, b:true}" v-for="(b, idx) in 200" :key="idx+1"
      :style="{animationDelay: idx*0.05+'s'}"></div>
    </div>
    <div class="textbox" v-show="!isActive">
      <div class="p1"> 오늘은 무슨 영화를 볼지?</div>
      <div class="p2"> 고민 해본적 있니?</div>
      <div class="p3"> 그런 널 위해 준비했어!</div>
      <button class="p4" @click="start" v-show="!isActive">일단 눌러봐!</button>
    </div>
    <div v-if="isActive" class="main fadein"> 
      <img src="@/assets/4.jpg" alt="">
    </div>
  <div v-if="isActive" class="text-area fadein">
    <div class="t-t"> 너와 내가 만들어가는 즐거움</div>
    <div class="t-c">I & U</div>
    <button @click="login" class="login"> Start!</button>
  </div>
  </section>
  </div>
</template>

<script>
export default {
  name: 'IntroView',
  data () {
    return {
      isActive : false
    }
  },
  methods : {
    start () {
      this.isActive = true
    },
    login () {
      this.$router.replace({name:'login'})
    }
  },
}
</script>

<style scoped>

section {
  position: relative;
  width: 100%;
  height: 100vh;
  background-color: black;
}
.banner {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  display: flex;
  flex-wrap: wrap;
}

.banner .blocks {
  position: relative;
  display: block;
  width: 20vw;
  height: 130px;
  background: white;
  animation:  animate 0.75s ease-in-out forwards;
}

@keyframes animate
{
  0% {
    opacity: 0;
    transform: scale(0) translateY(1000px);
  }
  50% {
    opacity: 1;
    background-color: white;

  }
  100% {
    opacity: 0;
    transform: scale(1) translateY(0);
    background-color: white;

  }
}

.text-area {
  position: absolute;
  top: 20%;
  left: 30%;
  
}

.t-t {
  font-family: 'Nanum Pen Script', cursive;
  font-size: 100px;
}

.t-c {
  font-family: 'Nanum Pen Script', cursive;
  font-size: 80px;
}

.login {
  border:none;
  border-radius: 10px;
  background-color: rgb(255,255,255,0.3);
  font-size: 50px;
  font-family: 'Dongle', sans-serif;
  margin-top: 150px;
  width: 200px;
  font-family: 'Grape Nuts', cursive;

}

.fadein {
  animation: fadein 5s;
}

@keyframes fadein {
  0% {
    opacity: 0;
  }
  50% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

.textbox {
  position: absolute;
  color:white;
  top: 20%;
  left: 30%;
}

.p1 {
  position: relative;
  left:-200px;
  padding-right: 200px;
  font-family: 'Nanum Pen Script', cursive;
  font-size: 80px;
  width: 100%;
  animation: fadein 1s;  
  opacity: 0;
  animation-fill-mode: forwards;

}

.p2 {
  opacity: 0;
  position: relative;
  right: -200px;
  margin-top: 50px;
  font-family: 'Nanum Pen Script', cursive;
  font-size: 80px;
  animation: fadein 1s;
  animation-delay: 1s;
  animation-fill-mode: forwards;

}

.p3 {
  position: relative;
  left: -150px;
  margin-top: 50px;
  font-family: 'Nanum Pen Script', cursive;
  font-size: 80px;
  animation: fadein 1s;
  animation-delay: 2s;
  opacity: 0;
  animation-fill-mode: forwards;

}

.p4 {
  position: relative;
  right: -400px;
  margin-top: 50px;
  font-family: 'Nanum Pen Script', cursive;
  font-size: 80px;
  color:white;
  background-color: transparent;
  border: solid, 2px, white;
  animation: fadein 1s;
  animation-delay: 3s;
  opacity: 0;
  animation-fill-mode: forwards;
}
</style>