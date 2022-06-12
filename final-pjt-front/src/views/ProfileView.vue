<template>
  <div class="home">
    <div class="circle"></div>
    <div class="title">
      <span> <span style="color:#666;">P</span>rofile</span>
      <br>
      <div>{{ this.$route.params.username }} <span style="color:#666; font-size:5vh">'s page </span></div>
    </div>
    <div class="main fadein">
      <div class="user-info">
        <div class="user-img">
          <img src="@/assets/iu3.jpg" alt="">
          <div class="profile-message">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Itaque incidunt optio illo quisquam.</div>
        </div>
        <div class="user-detail">
          <div class="user-name"> {{ profile.username }}</div>
          <div class="user-desc"> Like Movies : {{ profile.favorite_movies_count }} </div>
          <div class="user-desc"> Total Artciels : {{ profile.articles.length }} </div>
          <div class="user-desc"> Like Articles : {{ profile.favorite_article_count }}  </div>
        </div>
      </div>
      <div class="under-bar"></div>
      <div class="user-about">
        <div class="card like-movies">
          <img src="@/assets/movie.jpg" alt="">
          <div class="content">
            <h2 class="content-title">Like Movies</h2>
            <div>
              <span v-for="(movie, idx) in profile.favorite_movies" :key="idx" @click="getDetail(movie.id)">
                {{ idx+1 }}. <span class="detail-list">{{ movie.title }}</span> <br>
              </span> 
            </div>
          </div>
        </div>
        <div class="card total-articles">
          <img src="@/assets/article.jpg" alt="">
          <div class="content">
            <h2 class="content-title">Total Articles</h2>
            <div>
                <span v-for="(articles, idx) in profile.articles" :key="idx" @click="getArticleDetail(articles.id)">
                {{ idx+1 }}. <span class="detail-list">{{ articles.title }}</span>  <br>
              </span> 
            </div>
          </div>
        </div>
        <div class="card like-articles">
          <img src="@/assets/like.jpg" alt="">
          <div class="content">
            <h2 class="content-title">Like Articles</h2>
            <div>
              <span v-for="(articles, idx) in profile.favorite_article" :key="idx" @click="getArticleDetail(articles.id)">
                {{ idx+1 }}. <span class="detail-list">{{ articles.title }}</span>  <br>
              </span> 
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

// import { mapActions } from 'vuex'
import { mapGetters } from 'vuex'
import { mapActions } from 'vuex'

export default {
  name: 'ProfileView',
  created () {
    this.navToggle(true)
  },
  methods : {
    ...mapActions(['navToggle', 'getDetail','getArticleDetail'])
  },
  computed: {
    ...mapGetters(['navState', 'currentUser', 'profile']),
  },
}
</script>

<style scoped>
  .home {
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
    left: -600px;
    top: -600px;
    height: 1200px;
    width: 1200px;
    border-radius: 50%;
    background: linear-gradient(to bottom, rgba(255,255,255,1) 0%, rgba(255,255,255,0) 100%);
    /* background: linear-gradient(to right, rgba(0,0,0,1) 0%, rgba(0,0,0,0) 100%); */
  }

  .title {
    position: absolute;
    margin-left: 30px;
    text-align: start;
    color: white;
    font-family: 'Grape Nuts', cursive;
    transform: rotate(310deg);
    
  }

  .title :nth-child(1) {
    font-family: 'Grape Nuts', cursive;
    font-weight: bold;
    text-align: center;
    font-size: 12vh;
  }

  .title :nth-child(3) {
    font-family: 'Grape Nuts', cursive;
    font-weight: bold;
    font-size: 6vh;
    color: blanchedalmond;
    position: relative;
    text-align: end;
    left: -100px;
    top: -40px;
    width: 500px;
  }

  .main {
    position: relative;
    left: 350px;
    top: 100px;
    height: 800px;
    width: 1200px;
  }

  .user-info {
    position: relative;
    left: 5%;
    width: 90%;
    height: 39%;
    display: flex;
    border-radius: 10px;
  }
  
  .user-img {
    position: relative;
    width: 50%;
    height: 100%;
    display: flex;
    place-content: center;
  }

  .user-img img {
    height: 80%;
    width: 50%;
    border-radius: 10px;
    margin: 30px;
    margin-left: 50px;
  }

  .user-detail {
    padding: 20px;
    width: 50%;
    height: 80%;
    display: flex;
    flex-direction: column;
    margin: 50px;
    margin-top: 30px;
    border: 4px solid white;
    border-radius: 10px;
  }

  .user-name{
    text-align: start;
    font-size: 40px;
    padding-left: 50px;
  }

  .user-desc {
    text-align: start;
    margin-top: 20px ;
    padding-left: 50px;
  }


  .under-bar {
    top:44%;
    position: absolute;
    width: 100%;
    height: 1%;
    background-color: white;
    border-radius: 10px;
  }

  .user-about {
    position: relative;
    margin-top: 150px;
    left: -5%;
    width: 110%;
    height: 50%;
    display: flex;
    justify-content: space-evenly;
    align-items: center;
  }

  .card img {
    position: relative;
    top: -50px;
    left: 35px;
    height: 300px;
    width: 250px;
    border-radius: 10px;
    opacity: 0.8;

  }

  .card:hover img {
    transform: translate(0, -200px);    
    transition: 1s ease-in-out;
    animation: fadeout 1s;
    animation-fill-mode: forwards;
  }

  @keyframes fadeout {
    0% {
      opacity: 1;
    }
    100% {
      opacity: 0;
    }
  }

  .card:hover .content {
    transform: translate(0, -240px);    
    transition: 1.5s;
  }

  .card:hover .content > div {
    visibility: visible;
    transition: ease-in-out;
    animation: fadeout2 2s;
  }
  @keyframes fadeout2 {
    0% {
      opacity: 0;
    }
    100% {
      opacity: 1;
    }
  }

  .content {
    position: relative;
    top: -25px;
  }

  .card {
    width: 320px;
    height: 340px;
    border-radius: 10px;
    border: none;
    background-color: rgba(255,255,255,0.7);
  }

  .content > div {
    visibility: hidden;
    height: 230px;
    width: 270px;
    margin: auto;
    padding: 10px;
    overflow-y: scroll;
    padding-left: 30px;
    text-align: start;
  }

  .content > div > span {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    display: block;
    width: 200px;
    font-family: 'Dongle', sans-serif;
    font-size: 16px;
  }

  .detail-list {
    font-family: 'Dongle', sans-serif;
    font-size: 36px;
  }

  
  .content > div > span:hover {
    text-decoration: underline;
    cursor: pointer;
  }

  .content > div::-webkit-scrollbar {
    width: 20px;
  }

  .content > div::-webkit-scrollbar-thumb {
    background-color: white; /*스크롤바의 색상*/
    border: 2px solid transparent;
    background-clip: padding-box;
    border-radius: 10px;
  }

  .content > div::-webkit-scrollbar-track {
    position: absolute;
    background-color: rgba(0, 0, 0, 0.5);
    border-radius: 10px;
    border: 5px solid transparent;
    background-clip: padding-box;
  }

  .content-title {
    font-family: 'Dongle', sans-serif;
    font-size: 50px;
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

.profile-message {
  position: absolute;
  z-index: -1;
  top: 100px;
  left: 104px;
  height: 210px;
  width: 300px;
  background-color: rgba(255,255,255,0.5);
  border-radius: 10px;
  font-family: 'Dongle', sans-serif;
  padding: 20px;
  font-size: 24px;
}

  .user-img:hover img {
    transform: translate(0, -200px);    
    transition: 1s ease-in-out;
    animation: fadeout 1s;
    animation-fill-mode: forwards;
  }

  @keyframes fadeout {
    0% {
      opacity: 1;
    }
    100% {
      opacity: 0;
    }
  }

  .user-img:hover  div {
    transition: ease-in-out;
    animation: fadeout2 2s;
  }
  @keyframes fadeout2 {
    0% {
      opacity: 0;
    }
    100% {
      opacity: 1;
    }
  }

</style>>
