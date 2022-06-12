<template>
  <div class="home">
    <SearchBar />
    <SearchResult v-if="showResult"/>
    <div class="circle"></div>
    <div class="title">
      <span>H</span>
      <span>ome</span>
      <span>너와 내가 만들어가는 즐거움!</span>
      <span>U & I</span>
      </div>
      <div class="under-bar"></div>
    <MovieList class="movie-list"/>
    <SiteRanking class="site-ranking"/>
  </div>
</template>
  
<script>
import MovieList from '@/components/MovieList.vue'
import SiteRanking from '@/components/SiteRanking.vue'
import SearchBar from '@/components/SearchBar.vue'
import SearchResult from '@/components/SearchResult.vue'
import {mapGetters, mapActions} from 'vuex'

export default {
  name: 'HomeView',
  components: {
    MovieList,
    SiteRanking,
    SearchBar,
    SearchResult,
  },
  methods: {
    ...mapActions(['navToggle', 'exitResult'])
  },
  computed: {
    ...mapGetters(['navState', 'showResult', 'isLoggedIn' ])
  }, 
  created () {
    this.navToggle(true)
    this.exitResult()
  },
  mounted () {
  }
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


</style>

