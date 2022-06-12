<template>
  <div class="Recommendation">
    <GenreReco @close="close" v-if="IsGenre" />
    <LikeReco @likeclose="likeclose" v-if="IsLike"/>
    <div class="circle"></div>
    <div class="title">
      <span>R</span>
      <span>commendation</span>
      <span>오직 너만을 위한!!!</span>
      <span>U & I</span>
      </div>
      <div class="under-bar"></div>
    <div class="main-container">
      <div class="card">
        <div class="card-title"> Genre Recommendation To. {{ currentUser.username }}</div>
      <div class="imgBox">
        <img src="@/assets/pastel1.jpg" alt="">
      </div>
      <div class="details1">
        <h2>Genre Recommendation</h2>
        <p>어서와! 여긴 처음이야?<br>
        뭐 볼지 고민하고 있었어?<br>
        일단 눌러봐!!<br>
        너만을 위한 맞춤 영화!</p>
        <button @click="Genre">Go!</button>
      </div>
    </div>
    <div class="card2">
      <div class="card2-title"> Like Recommendation To. {{ currentUser.username }}</div>
      <div class="imgBox">
        <img src="@/assets/pastel2.jpg" alt="">
      </div>
      <div class="details2">
        <h2>Like Recommendation</h2>
        <p>좋아하는 영화 있어?<br>
        아, 좋아요도 눌렀구나!<br>
        그런 널 위한 영화가 있지!<br>
        오직, 너만을 위한 영화!</p>
        <button @click="like">Go!</button>
      </div>
    </div>
    </div>
  </div>
</template>

<script>

import { mapActions, mapGetters } from 'vuex'
import GenreReco from '@/components/GenreReco.vue'
import LikeReco from '@/components/LikeReco.vue'
import Swal from 'sweetalert2'

export default {
  name: 'RecommendationView',
  components: {
    GenreReco,
    LikeReco,
  },
  data () {
    return {
      IsGenre : false,
      IsLike : false,
    }
  },
  methods : {
    ...mapActions(['navToggle', 'getProfile']),
    close () {
      this.IsGenre = false
    },
    Genre () {
      this.IsGenre = true
    },
    like () {
      
      if (!this.profile.favorite_article_count) {
        Swal.fire('영화 좋아요를 눌러줘 :(')
        return
      }
      this.IsLike = true
    },
    likeclose () {
      this.IsLike = false
    }
  },
  computed : {
    ...mapGetters(['navState', 'currentUser', 'profile'])
  },
  created () {
    this.navToggle(true)
    this.getProfile(this.currentUser.username)
  }
  
}
</script>

<style scoped>

  .Recommendation {
    position: relative;
    overflow: hidden;
    height: 100vh;
  }

  .site-ranking {
    top:40px;
    position: relative;
  }

  .movie-list {
    position: relative;
    top: 20px;
  }

  .circle {
    position: absolute;
    left: -900px;
    top: -900px;
    height: 1800px;
    width: 1800px;
    border-radius: 50%;
    background: linear-gradient(to bottom, rgba(255,255,255,1) 0%, rgba(255,255,255,0) 100%);
    /* background: linear-gradient(to right, rgba(0,0,0,1) 0%, rgba(0,0,0,0) 100%); */
  }

  .title {
    margin-top: 1vh;
    margin-left: 100px ;
    font-size: 7rem;
    text-align: start;
    color: black;
    font-family: 'Grape Nuts', cursive;
  }

  .title :nth-child(1) {
    font-family: 'Grape Nuts', cursive;
    font-weight: bold;
  }

  .title :nth-child(2) {
    font-family: 'Grape Nuts', cursive;
    font-weight: bold;
    color: white;
  }

  .title :nth-child(3) {
    font-family: 'Nanum Pen Script', cursive;
    font-size: 2.5rem;
    margin-left: 80px;
    color: white;
    vertical-align: sub;
  }

    .title :nth-child(4) {
    font-family: 'Nanum Pen Script', cursive;
    font-weight: bold;
    font-size: 4rem;
    margin-left: 40px;
    color: rgba(0, 0, 0, 0.5);
    vertical-align: sub;
  }

  .under-bar {
    position: relative;
    top: -1%;
    left: 100px;
    height: 3px;
    background: rgb(255,255,255);
    background: linear-gradient(164deg, rgba(255,255,255,0.3) 20%, rgba(255,255,255,0.4) 40%, rgba(255,255,255,0.8) 60%, rgba(255,255,255,0.4) 80%, rgba(255,255,255,0.3) 100%);
    filter: blur(1px);
    width: 80vw;
    transition: 1s;
  }

  .main-container {
    position: relative;
    top:15px;
    height: 750px;
    width: 1200px;
    margin: 100px auto;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
  }

  .card {
  position: relative;
  margin: 20px 0;
  width: 300px;
  height: 400px;
  background-color: rgba(255, 255, 255, 0.5);
  transform-style: preserve-3d ;
  transform: perspective(2000px);
  transform: scale(1.2);
  transition: 1s;
  border: none;
  border-radius: 10px;
}

.card:hover{
  transform : perspective(2000px) rotate(-10deg);
}

.card:hover .details1 {
  visibility: visible;
  animation: fadein 4s;
  transition: ease-in-out;
}

.card .imgBox {
  position: relative;
  width: 100%;
  height: 100%;
  box-sizing: border-box;
  transform-origin:left;
  z-index: 1;
  transition: 1s;
  border: none;
  border-radius: 10px;
  right:10px;
}

.card:hover .imgBox {
  transform: rotateY(-135deg)
}

.card .imgBox img  {
  box-sizing: border-box;
  position: absolute;
  border-radius: 10px;
  right: 0px;
  opacity: 0.6;
}

.card2 {
  position: relative;
  margin: 20px 0;
  width: 300px;
  height: 400px;
  background-color: rgba(255, 255, 255, 0.5);
  transform-style: preserve-3d ;
  transform: perspective(2000px);
  transform: scale(1.2);
  transition: 1s;
  border-radius: 10px;
}

.card2:hover{
  transform : perspective(2000px) rotate(10deg);
}

.card2 .imgBox {
  position: relative;
  width: 100%;
  height: 100%;
  transform-origin:right;
  z-index: 1;
  transition: 1s;
  border-radius: 10px;
}

.card2:hover .imgBox {
  transform: rotateY(135deg);
  z-index: 100;
}

.card2:hover .details2 {
  visibility: visible;
  animation: fadein 4s;
  transition: ease-in-out;
}

.card2 .imgBox img {
  position: absolute;
  border-radius: 10px;
  opacity: 0.6;
  right: 10px;
  object-fit: cover;
  border-radius: 10px;
}

.details1 {
  position: absolute;
  top: 0;
  left: 0;
  box-sizing: border-box;
  padding: 20px;
  visibility: hidden;
}

.details2 {
  position: absolute;
  top: 0;
  left: 0;
  box-sizing: border-box;
  padding: 20px;
  visibility: hidden;
}

.fadein {
  animation: fadein 2s;
}

@keyframes fadein {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

.details1 > h2 {
  font-family: 'Grape Nuts', cursive;
  font-weight: bold;
  font-size: 40px;
}

.details1 > p {
  margin-top: 30px;
  font-size: 30px;
  font-family: 'Nanum Pen Script', cursive;
}

.details2 > h2 {
  font-family: 'Grape Nuts', cursive;
  font-weight: bold;
  font-size: 40px;
}

.details2 > p {
  padding-left: 10px;
  margin-top: 30px;
  font-size: 30px;
  font-family: 'Nanum Pen Script', cursive;
}

button {
  background-color: transparent;
  opacity: 0.8;
  width: 80px;
  height: 35px;
  border: 2px solid #666;
  border-radius: 10px;
  color: #666;
}

.card:hover .card-title {
  visibility: hidden;
}

.card-title {
  position: absolute;
  top: 20px;
  width: 60px;
  height: 300px;
  background-color: transparent;
  right: 20px;
  writing-mode: vertical-rl;
  font-size: 30px;
  text-align: start;
  padding-top: 30px;
  font-family: 'Grape Nuts', cursive;
  color: black;
}

.card2:hover .card2-title {
  visibility: hidden;
}

.card2-title {
  position: absolute;
  bottom: 10px;
  width: 60px;
  height: 300px;
  background-color: transparent;
  left: 20px;
  writing-mode: vertical-rl;
  font-size: 30px;
  text-align: start;
  padding-top: 30px;
  font-family: 'Grape Nuts', cursive;
  color: black;
  transform: scale(-1);
}

</style>