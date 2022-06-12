<template>
<div class="LikeReco">
  <div v-if="!isSelected" class="container">
    <i @click="like" class="fa-solid fa-xmark back-btn"></i>
    <div class="box">
      <div class="box-title"> 너랑 비슷한 취향인 다른 친구들은 어떤 영화를 볼까? <br>
        <span> 좋아요한 영화를 바탕으로 비슷한 취향인 친구들이 본 영화를 추천해줄게! </span>
      </div>
      <div v-if="!!profile.favorite_movies" class="box-content">
        <div @click="recommend(movie.id)" class="box-item" v-for="(movie, idx) in profile.favorite_movies" :key="idx">
          <div class="item-img">
            <img :src="movie.poster_path" alt="">
          </div>
          <div class="item-desc">
            <div class="desc-title">{{ movie.title }}</div>
            <div class="desc-overview"> {{ movie.overview }} </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-else class="container">
    <div class="content fadein">
      <div class="reco-title"> 이 영화 좋아요를 누른 다른 친구들이 본 영화! <br> 
      <span class="reco-desc"> 다른 영화들도 맘껏 눌러봐! </span> 
      </div>
      <i @click="reco" class="fa-solid fa-xmark back-btn2"></i>
      <div class="reco-item" v-for="(movie, idx) in getlikerecommend" :key="idx">
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

import {mapActions, mapGetters} from 'vuex'

export default {
  name: 'LikeReco',
  data () {
    return {
      isSelected : false,
    }
  },
  methods: {
    ...mapActions(['getDetail', 'getProfile','getLikeReco']),
    like() {
      this.$emit('likeclose')
    },
    reco () {
      this.isSelected = false
    },
    recommend (movieId) {
      this.getLikeReco(movieId)
      this.isSelected = true
    },
  },
  computed: {
    ...mapGetters(['currentUser', 'profile', 'getlikerecommend']),
  },
  created () {
    this.getProfile(this.currentUser.username)
  }
}
</script>

<style scoped>

  .box{
    position: absolute;
    top: 50px;
    height: 750px;
    width: 1200px;
  }

  .box-title {
    position: relative;
    height: 20%;
    display: flex;
    justify-content: flex-start;
    align-items: flex-start;
    flex-direction: column;
    color: white;
    font-family: 'Dongle', sans-serif;
    font-size: 70px;
  }

  .box-title > span {
    font-size: 40px;
    font-family: 'Dongle', sans-serif;
    position: absolute;
    top: 100px;
    left: 40px;
  }

  .box-content {
    position: relative;
    margin-top: 40px;
    height: 75%;
    border-radius: 10px;
    display: flex;
    flex-wrap: wrap;
    overflow: auto;
  }

  .box-item {
    position: relative;
    width: 45%;
    height: 40%;
    border-radius: 10px;
    display: flex;
    margin: 20px;
    border: 2px solid white;
    padding: 10px;
    cursor: pointer;
  }

  .box-item:hover {
    background-color: rgba(255,255,255,0.7);
  }

  .box-item:hover .item-desc {
    color: black;
  }

  .item-img {
    position: relative;
    height: 100%;
    left:20px;
    width: 40%;
  }

  img {
    height: 100%;
    width: 90%;
    border-radius: 10px;
  }

  .item-desc {
    height: 100%;
    margin-left: 40px;
    width: 50%;
    color: white;
  }

  .desc-title {
    height: 30%;
    width: 100%;
    font-family: 'Dongle', sans-serif;
    font-size: 35px;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .desc-overview {
    width: 100%;
    padding: 8px;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 4; /* 라인수 */
    -webkit-box-orient: vertical;
    word-wrap:break-word; 
    line-height: 1.2em;
    height: 4.8em;
    font-family: 'Dongle', sans-serif;
    font-size: 24px;
  }

  .box-content::-webkit-scrollbar {
    width: 20px;
  }

  .box-content::-webkit-scrollbar-thumb {
    background-color: white; /*스크롤바의 색상*/
    border: 2px solid transparent;
    background-clip: padding-box;
    border-radius: 10px;
  }

  .box-content::-webkit-scrollbar-track {
    position: absolute;
    background-color: rgba(0, 0, 0, 0.5);
    border-radius: 10px;
    border: 5px solid transparent;
    background-clip: padding-box;
  }

  .back-btn {
    position: absolute;
    font-size: 40px;
    color: white;
    top: 20px;
    cursor: pointer;
    right: 37px;
  }

  .back-btn2 {
    position: absolute;
    font-size: 40px;
    color: white;
    top: -65px;
    cursor: pointer;
    right: -30px;
  }

  .LikeReco {
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
    left: -30px;
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
    left: 40
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
  color: white;
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

</style>