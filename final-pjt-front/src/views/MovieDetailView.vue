<template>
  <div class="detail">
    <div class="detail-box">
      <i v-if="userLiked" @click="like(movieDetail.id)" class="fa-solid fa-heart like-btn"></i>
      <i v-else @click="like(movieDetail.id)" class="fa-regular fa-heart like-btn" style="color:grey;"></i>
      <i @click="back" class="fa-solid fa-xmark back-btn"></i>
      <div class="video-box">
        <div class="ratio ratio-16x9 video-player">
          <iframe :src="`${movieDetail.video_path}?autoplay=1&mute=1`" title="YouTube video"></iframe>
        </div>
      </div>
      <div class="content-box">
        <div class="movie-desc">
          <div class="movie-title">{{ movieDetail.title }}</div>
          <div class="movie-genre">
            <span v-for="(genre, idx) in movieDetail.genres" :key="idx"> {{ genre.genre_name }}</span>
          </div>
          <div class="under-bar"></div>
          <div class="movie-overview">{{ movieDetail.overview }}</div>
        </div>
        <div class="movie-about">
          <div class="actor-area">
            <div class="actor">
              Actors
            </div>
            <div class="actor-list">
              <div class="actor-info" v-for="(actor, idx) in movieDetail.actors" :key="idx" v-show="idx<4">
                <div class="actor-detail" >
                  <img :src="actor.profile_path" alt="">
                  <span>
                    {{ actor.name }}
                  </span>
                </div>
              </div>
            </div>
          </div>
          <div class="article-area">
            <div class="article-info">Articles</div>
            <div class="article-list" v-if="!!movieDetail.article.length">
              <div @click="getArticleDetail(article.id)" class="article" v-for="(article, idx) in movieDetail.article" :key="idx" v-show="idx<3">
                <div class="a-t">
                  {{article.title}} 
                </div>
                <div class="a-c">
                  {{article.content}}
                </div>
              </div>
            </div>
            <div v-else> No articles...</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'

export default {
  name: 'MovieDetailView',
  methods: {
    moveToBack () {
      this.$router.back()
    },
    ...mapActions(['navToggle','getArticleDetail','movieLike','getProfile']),
    back () {
      this.$router.back()
    },
    like (movieId) {
      this.movieLike(movieId)
    }
  },
  computed:{
    ...mapGetters(['navState', 'movieDetail', 'profile', 'currentUser', 'userLiked']),
  },
  created () {
    this.navToggle(false)
    this.getProfile(this.currentUser.username)
  },
}
</script>

<style scoped>
  .detail {
    height: 100vh;
    width: 100vw;
    background-color: rgba(0,0,0,0.5);
  }

  .detail-box {
    position: relative;
    top: 25px;
    height: 900px;
    width: 1300px;
    left: 300px;
    background-color: rgba(0,0,0,0.5);
    border-radius: 10px;
  }

  .video-box {
    position: relative;
    height: 50%;
    width: 100%;
    background-color: black;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    display: flex;
    justify-content: center;
  }

  .video-player {
    width: 1000px;
  }

  .back-btn {
    position: absolute;
    right: 20px;
    color: white;
    z-index: 1;
    top: 10px;
    font-size: 40px;
  }

  .like-btn {
    position: absolute;
    bottom: 10px;
    color: red;
    font-size: 40px;
    right: -70px;
    cursor: pointer;
  }

  .back-btn:hover {
    transform: scale(1.2);
    cursor: pointer;
  }

  .content-box {
    position: relative;
    width: 100%;
    height: 50%;
    display: flex;
  }

  .movie-desc {
    position: relative;
    width: 50%;
    height: 100%;
  }

  .movie-about {
    position: relative;
    width: 50%;
    height: 100%;
  }

  .movie-title {
    position: relative;
    width: 100%;
    height: 20%;
    font-family: 'Nanum Pen Script', cursive;
    padding: 40px;
    margin-top: 15px;
    font-size: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
  }

  .movie-genre {
    color :white;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: flex-end;
    padding-right: 60px;
  }

  .movie-genre > span {
    margin-left: 15px;
    font-size: 20px;
    font-family: 'Grape Nuts', cursive;
  }

  .under-bar {
    width: 90%;
    background-color: white;
    height: 1%;
    margin-top: 10px;
    margin-left: 35px;
    border-radius: 10px;
  }

  .movie-overview {
    position: relative;
    width: 90%;
    top: 5%;
    height: 52%;
    background-color: rgba(0,0,0,0.5);
    margin-left: 5%;
    padding: 30px;
    text-align: start;
    border-radius: 10px;
    overflow: auto;
    font-family: 'Dongle', sans-serif;
    font-size: 30px;
    color:white;
  }

  .movie-overview::-webkit-scrollbar {
    width: 20px;
  }

  .movie-overview::-webkit-scrollbar-thumb {
    background-color: white; /*스크롤바의 색상*/
    border: 2px solid transparent;
    background-clip: padding-box;
    border-radius: 10px;
  }

  .movie-overview::-webkit-scrollbar-track {
    position: absolute;
    background-color: rgba(0, 0, 0, 0.5);
    border-radius: 10px;
    border: 5px solid transparent;
    background-clip: padding-box;
  }

  .actor-area {
    top:5%;
    position: relative;
    width: 100%;
    height: 60%;
  }

  .actor {
    position: relative;
    font-family: 'Grape Nuts', cursive;
    font-size: 30px;
    color:white;
    text-align: start;
  }

  .actor-list {
    position: relative;
    height: 70%;
    width: 100%;
    display: flex;
    justify-content: space-evenly;
  }

  .actor-info {
    position: relative;
    height: 100%;
    width: 27%;

  }

  .actor-detail {
    position: relative;
    width: 100%;
    height: 100%;
    color:white;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
  }

  .actor-detail > span {
    margin-top: 10px;
    display: inline-block;
    font-size: 24px;
    font-family: 'Dongle', sans-serif;
    display: block;
  }

  .actor-detail > img {
    position: relative;
    height: 50%;
    width: 110px;
    border-radius: 10px;
    display: block;
  }

  .article-area {
    position: absolute;
    top: 53%;
    height: 40%;
    width: 100%;
    color: white;

  }

  .article-info {
    font-family: 'Grape Nuts', cursive;
    font-size: 30px;
    text-align: start;
  }

  .article-list {
    height: 70%;
    display: flex;
    align-items: center;
    justify-content: space-evenly;
  }

  .article {
    height: 100%;
    width: 28%;
    border-radius: 10px;
    text-align: start;
    background-color: rgba(0,0,0,0.5);
    
    padding: 10px;
  }
  .article:hover {
    background-color: rgba(255,255,255,0.5);
  }

  .article:hover {
    cursor: pointer;
  }

  .a-t {
    position: relative;
    height: 30%;
    font-family: 'Dongle', sans-serif;
    font-size: 24px;
  }

  .a-c {
    position: relative;
    height: 80%;
    font-family: 'Dongle', sans-serif;
    font-size: 24px;
    padding:3px;
    padding-bottom: 0;
    overflow: visible;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 3; /* 라인수 */
    -webkit-box-orient: vertical;
    word-wrap:break-word; 
    line-height: 1.2em;
    height: 3.6em; /* line-height 가 1.2em 이고 5라인을 자르기 때문에 height는 1.2em * 5 = 6.0em */
  }

</style>