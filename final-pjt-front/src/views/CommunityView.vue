<template>
  <div class="community">
    <SearchBar />
    <SearchResult v-if="showResult"/>
    <div class="circle"></div>
    <div class="title">
      <span>C</span>
      <span>ommunity</span>
      <span>우리 같이 만들어 볼래?</span>
      <span>U & I</span>
      </div>
      <div class="under-bar"></div>
      <div class="container">
        <div class="side-menu">
          <div v-if="isLoggedIn" @click="goToCreate" >Create</div>
        </div>
        <div class="scroll-area">
          <div class="item" v-for="(article, idx) in articles" :key="idx" @click="getArticleDetail(article.pk)">
            <img :src="article.movie.poster_path" alt="">
            <div class="article-desc">
              <div class="a-title">
                {{ article.title }}
              </div>
              <div class="m-title">
                {{ article.movie.title }}
              </div>
              <div class="a-content">
                {{ article.content }}
              </div>
              <div class="a-about">
                <span>
                  Author. {{ article.user.username }}
                </span>
                <span>
                  <i class="fa-solid fa-heart"> {{ article.like_count }}</i>
                </span>
                <span>
                  <i class="fa-solid fa-comments"> {{ article.comment_count }}</i>
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
  </div>
</template>

<script>

import { mapActions } from 'vuex'
import { mapGetters } from 'vuex'
import SearchBar from '@/components/SearchBar.vue'
import SearchResult from '@/components/SearchResult.vue'

export default {
  name: 'CommunityView',
  data () {
    return {
    }
  },
  
  components: {
    SearchBar,
    SearchResult,
  },
  methods : {
    ...mapActions(['navToggle', 'exitResult','articleList', 'getArticleDetail', 'navToggle']),
    goToCreate () {
      this.$router.push({ name: 'articleform' })
    }
  },
  computed : {
    ...mapGetters(['navState', 'showResult', 'articles', 'isLoggedIn', 'navState'])
  },
  created () {
    this.articleList()
    this.navToggle(true)
  }
}
</script>

<style scoped>
    .community {
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

  .container {
    margin-top: 50px;
    height: 700px;
    width: 1400px;
    position: relative;
    border-radius: 10px;
    border-top-right-radius: 0px;
    background-color: rgba(255, 255, 255, 0.5);
  }

  .scroll-area {
    position: relative;
    height: 85%;
    width: 90%;
    overflow: auto;
    border-radius: 10px;
    display: flex;
    flex-flow: row wrap;
    background-color: transparent;
  }

  .scroll-area::-webkit-scrollbar {
    width: 20px;
  }

  .scroll-area::-webkit-scrollbar-thumb {
    background-color: white; /*스크롤바의 색상*/
    border: 2px solid transparent;
    background-clip: padding-box;
    border-radius: 10px;
  }

  .scroll-area::-webkit-scrollbar-track {
    position: absolute;
    background-color: rgba(0, 0, 0, 0.5);
    border-radius: 10px;
    border: 5px solid transparent;
    background-clip: padding-box;
  }

  .item {
    position: relative;
    margin-top: 20px;
    width: 48%;
    height: 40%;
    display: flex;
    margin-left: 1%;
    margin-bottom: 20px;
    border-radius: 10px;
  }

  .item:hover {
    background-color: rgba(0, 0, 0, 0.2);
    border-radius: 10px;
    box-shadow: 5px rgba(255, 255, 255, 0.7);
    cursor: pointer;
  }

  .item img {
    border-radius: 10px;
  }

  .article-desc {
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100%;
  }

  .side-menu {
    position: absolute;
    top: -81px;
    right: -1px;
  }

  .a-title {
    position: relative;
    height: 20%;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    padding-left: 30px;
    font-family: 'Nanum Pen Script', cursive;
    font-weight: bold;
    font-size: 24px;
  }

  .m-title {
    position: relative;
    height: 15%;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    padding-left: 30px;
    font-family: 'Nanum Pen Script', cursive;
    font-size: 20px;
  }

  .a-content {
    position: relative;
    height: 30%;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    padding-left: 30px;
    font-size: 24px;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 3; /* 라인수 */
    -webkit-box-orient: vertical;
    word-wrap:break-word; 
    line-height: 2em;
    text-align: start;
    font-family: 'Dongle', sans-serif;

  }

  .a-about {
    position: relative;
    height: 25%;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    padding-left: 10px;
    display: flex;
    justify-content: space-evenly;
  }

  .side-menu div {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top : 30px;
    margin-bottom: 30px;
    width: 200px;
    height: 50px;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    background-color : rgba(255, 255, 255, 0.5);
    cursor: pointer;
  }

</style>