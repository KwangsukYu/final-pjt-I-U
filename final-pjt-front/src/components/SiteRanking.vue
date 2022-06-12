<template>
  <div class="card fadein">
    <div class="title">
      <span class="grey">U&I</span>
      <span class="white">Ranking</span>
      </div>
    <div class="slider">
      <div class="slide-track">
        <div class="slide" v-for="(movie, idx) in siteRanking" :key="idx">
          <div class="desc">
            <div class="movie-title">
              {{ movie.title }}
            </div>
            <div class="movie-desc">
              {{ movie.overview }}
            </div>
            <div @click="getDetail(movie.id)" class="detail"> Detail </div>
          </div>
          <img :src="movie.poster_path" alt="">
        </div>
        <div class="slide" v-for="(movie, idx) in siteRanking" :key="idx+20">
          <div class="desc">
            <div class="movie-title">
              {{ movie.title }}
            </div>
            <div class="movie-desc">
              {{ movie.overview }}
            </div>
            <div @click="getDetail(movie.id)" class="detail"> Detail </div>
          </div>
          <img :src="movie.poster_path" alt="">
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import {mapActions} from 'vuex'
import {mapGetters} from 'vuex'

export default {
  name: "SiteRanking",
  methods: {
    ...mapActions(['getRank', 'getDetail'])
  },
  computed: {
    ...mapGetters(['siteRanking'])
  },
  created () {
    this.getRank()
  }
}
</script>

<style scoped>
  .card {
    display: flex;
    place-items: center;
    background: transparent;
    border: none;
  }

  .title {
    position: relative;
    left: 60px;
    width: 80%;
    text-align: start;
    font-size: 2.5rem;
    margin-bottom: 20px;
    color: white;
  }

  .slider {
    height: 300px;
    position: relative;
    width: 75%;
    display: grid;
    place-items: center;
    overflow: hidden;
    border-radius: 10px;
  }

  .slide-track {
    display: flex;
    width: calc(250px * 18);
    animation: scroll 20s linear infinite;
  }

  .slide-track:hover {
    animation-play-state: paused;
  }

  @keyframes scroll {
    0% {
      transform: translateX(0);
    }
    100% {
      transform: translateX(calc(-250px * 9));
    }
  }

  .slide {
    height: 300px;
    width: 250px;
    display: flex;
    align-content: center;
    padding: 20px;
    perspective: 100px;
  }

  .slide:hover img {
    transform: translateZ(10px);
    filter: blur(5px);
  }

  img {
    width: 100%;
    transition: transform 1s;
    border-radius: 10%;
  }


  .slide:hover .desc {
    display: inline;
    z-index: 10;
  }
  
  .slider::before,
  .slider::after {
    background: linear-gradient(to right, rgba(255,255,255,0.5) 0%, rgba(255,255,255,0) 100%);
    content: '';
    height: 100%;
    position: absolute;
    width: 5%;
    z-index: 2;
  }

  .slider::before{
    left: 0;
    top: 0;
  }

  .slider::after {
    right: 0;
    top: 0;
    transform: rotateZ(180deg);
  }

  .title > span {
  margin-right: 20px;
  letter-spacing: 5px;
  font-family: 'Grape Nuts', cursive;
  font-weight: bold;
  }

  .grey {
    color: #666;
  }

  .white {
    color: white;
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

.movie-title {
  position: absolute;
  top: 15%;
  left: 10%;
  right: 5%;
  font-size: 34px;
  color: white;
  font-weight: bold;
  font-family: 'Dongle', sans-serif;

}

.movie-desc {
  width: 50%;
  position: absolute;
  bottom: 35%;
  left: 25%;
  right: 5%;
  color: white;
  font-size: 0.8rem;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 3; /* 라인수 */
  -webkit-box-orient: vertical;
  word-wrap:break-word; 
  line-height: 1.2em;
  height: 3.6em; /* line-height 가 1.2em 이고 5라인을 자르기 때문에 height는 1.2em * 5 = 6.0em */
  font-family: 'Dongle', sans-serif;
  font-size: 20px;
}

.detail {
  display: inline-block;
  position: absolute;
  bottom: 10%;
  right: 5%;
  left: 30%;
  width: 40%;
  background: white;
  text-decoration: none;
  color: #666;
  margin: 5px;
  border-radius: 10px;
  cursor: pointer;
  font-size: 20px;
  font-family: 'Dongle', sans-serif;

}

.desc {
  display:none;
}
</style>>
