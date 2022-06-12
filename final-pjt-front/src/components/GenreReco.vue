<template>
  <div class="GenreReco">
    <div v-if="!isSelected" class="container fadein">
        <div  class="GR-title">
        <i @click="closeReco" class="fa-solid fa-xmark back-btn"></i>
        <h2>Gerne Recommendation </h2> 
        <div class="GR-desc">어떤게 재밌어 보여? 한 번 골라봐!</div>
        </div>
        <div v-for="(movie, idx) in getrandomMovies" :key="idx" class="GR-item">
          <div class="itembox">
            <div class="detail">
              <div class="d-t">{{ movie.title }}</div>
              <div class="d-o">{{ movie.overview }}</div>
              <div class="d-btn">
                <button @click="getDetail(movie.id)"> Detail</button>
                <button @click="selectedMovies(movie)"> Select</button>
              </div>
            </div>
            <img  :src="movie.poster_path" alt="">
          </div>
        </div>
    </div>
      <div v-else class="container">
        <div class="content fadein">
          <div class="reco-title"> '{{ nowSelected.title }}' 추천 결과 <br> 
          <span>가장 비슷한 영화들이야, 어때?</span> 
          </div>
          <i @click="reco" class="fa-solid fa-xmark back-btn2"></i>
          <div class="reco-item" v-for="(movie, idx) in getRecoMovies" :key="idx">
            <div @click="getDetail(movie.id)" class="imgbox">
              <img :src="movie.poster_path" alt="">
              <div class="movie-info">
                <div class="m-t">{{ movie.title }}</div>
                <div class="m-i">{{ movie.overview }}</div>
                <div class="m-btn"> click!</div>
              </div>
            </div>
          </div>
        </div>
      </div>
  </div>
</template>

<script>

import {mapActions} from 'vuex'
import {mapGetters} from 'vuex'

export default {
  name: 'GenreRecommendation',
  data () {
    return {
      isSelected : false,
      nowSelected : ''
    }
  },
  methods: {
    ...mapActions(['getRandoms', 'getRecommend', 'getDetail']),
    closeReco () {
      this.$emit('close')
    },
    selectedMovies (movie) {
      this.nowSelected = movie
      this.getRecommend(movie.id)
      this.isSelected = true
    },
    reco () {
      this.isSelected = false
    }
  },
  computed: {
    ...mapGetters(['getrandomMovies', 'getRecoMovies'])
  },
  created () {
    this.getRandoms()
  }
}
</script>

<style scoped>
  .GenreReco {
    position: absolute;
    height: 100vh;
    width: 100vw;
    background-color: rgba(0,0,0,0.5);
    z-index: 101;
  }

  .container {
    position: relative;
    top: 70px;
    width: 1400px;
    height: 850px;
    display: flex;
    flex-flow: row wrap;
    justify-content: space-evenly;
  }

  .back-btn {
    position: absolute;
    font-size: 40px;
    color: white;
    top: -400px;
    right: -96px;
    cursor: pointer;
  }

  .back-btn2 {
    position: absolute;
    font-size: 40px;
    color: white;
    top: -65px;
    cursor: pointer;
    right: -30px;
  }


  .back-btn2:hover {
    transform: scale(1.2);
  }

  .back-btn:hover {
    transform: scale(1.2);
  }

  .GR-item {
    width: 22%;
    margin-top: 0;
    height: 300px;
  }

  .itembox {
    height: 300px;
  }

  .itembox:hover .detail {
    transform: scale(1.2);
    visibility: visible;
    transition: 0.5s ease-in-out;
    z-index: 1;
    animation: 1s fadein;
  }

  .detail {
    position: absolute;
    height: 300px;
    background-color: rgba(0,0,0,0.5);
    width: 215px;
    margin-left: 37px;
    border-radius: 10px;
    visibility: hidden;
    color: white;
    padding: 20px;
  }

  .d-t{
    height: 30%;
    font-size: 25px;
    font-family: 'Dongle', sans-serif;

  }

  .d-o {
    position: relative;
    margin-top: 10px;
    font-family: 'Dongle', sans-serif;

    font-size: 24px;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 3; /* 라인수 */
    -webkit-box-orient: vertical;
    word-wrap:break-word; 
    line-height: 1.2em;
    height: 3.6em;
    margin-bottom: 15px;
  }

  .d-btn {
    display: flex;
    justify-content: space-evenly;
    margin-top: 50px;
  }

  .d-btn button {
    border:none;
    background-color: white;
    color: #666;
    border-radius: 10px;
    font-family: 'Dongle', sans-serif;
    font-size: 20px;
  }

  .d-btn button:hover {
    transform: scale(1.2);
  }

  .GR-item img {
    object-fit: cover;
    height: 100%;
    border-radius: 10px;
  }

  .itembox:hover img {
    transform: scale(1.1);
    filter: blur(5px);
    transition: 0.5s ease-in-out;
    cursor: pointer;
  }

  .GR-title {
    position: absolute;
    width: 80%;
    height: 1%;
    top: 49.5%;
    background-color: rgba(255,255,255,0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    border-radius: 50px;
    font-weight: bold;
    font-family: 'Grape Nuts', cursive;
    opacity: 0.8;
    padding: 5px;
  }

  .GR-title > h2 {
    font-family: 'Grape Nuts', cursive;
    color: white;
    font-weight: bold;
    letter-spacing: 10px;
        font-size: 40px;
  }

  .GR-desc {
    display: block;
    font-size: 34px;
    height: 80px;;
    color: white;
    font-family: 'Nanum Pen Script', cursive;
  }

  .content {
    position: absolute;
    top: 50px;
    height: 100px;
    width: 90%;
    top : 10%;
    display: flex;
    flex-flow: row wrap;
    justify-content: space-evenly;
    align-items: center;
  }

  .reco-title {
  position: absolute;
  color: grey;
  width: 100%;
  height: 200px;
}

  .reco-item {
    position: relative;
    top: 150px;
    margin-bottom: 50px;
    margin-left: 50px;
    margin-right: 50px;
    width: 200px;
    height: 250px;
  }

  .imgbox {
    width: 200px;
    height: 250px;
  }

  .reco-item img {
    object-fit: cover;
    height: 100%;
    border-radius: 10px;
  }

.fadein {
  animation: fadein 1s;
}

@keyframes fadein {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

.movie-info {
  padding: 15px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  top : 0px;
  position: absolute;
  width: 180px;
  height: 250px;
  background-color: rgba(0,0,0,0.5);
  border-radius: 10px;
  visibility: hidden;
}


.imgbox:hover .movie-info {
  transform: translate(90px,0);
  transition: 0.5s ease-in-out;
  visibility: visible;
  z-index: -1;
  cursor: pointer;
  animation: 1s fadein;
}

.imgbox:hover img {
  transform: translate(-90px,0);
  transition: 0.5s ease-in-out;
  cursor: pointer;
}

.imgbox:hover {
  cursor: pointer;
}


.m-t {
  position: relative;
  height: 25%;
  border-radius: 10px;
  width: 100%;
  font-family: 'Dongle', sans-serif;
  font-size: 40px;
  color: white;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 1; /* 라인수 */
  -webkit-box-orient: vertical;
  word-wrap:break-word; 
  line-height: 1.2em;
  height: 1.2em;
  margin-bottom: 15px;
}

.m-i {
  position: relative;
  width: 100%;
  border-radius: 10px;
  font-family: 'Dongle', sans-serif;
  font-size: 24px;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 4; /* 라인수 */
  -webkit-box-orient: vertical;
  word-wrap:break-word; 
  line-height: 1.2em;
  height: 4.8em;
  color: white;
}

.m-btn {
  position: relative;
  width: 50%;
  height: 15%;
  border-radius: 10px;
  font-family: 'Dongle', sans-serif;
  font-size: 30px;
  color: black;
  margin-top: 20px;
  background-color: rgba(255,255,255,0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}

.reco-title {
  position: absolute;
  font-size: 70px;
  top: -80px;
  right: -30px;
  font-family: 'Dongle', sans-serif;
  padding: 30px;
  color: white;
  text-align: start;
}

.reco-title > span {
  font-size: 40px;
  font-family: 'Dongle', sans-serif;
  position: absolute;
  top: 130px;
  left: 40px;
}

</style>