<template>
  <div class="about">
    <SearchBar />
    <SearchResult v-if="showResult"/>
    <div class="circle"></div>
    <div class="title">
      <span>G</span>
      <span>enre</span>
      <span>너는 어떤 장르를 좋아해?</span>
      <span>U & I</span>
      </div>
    <div class="under-bar"></div>
    <div class="content fadein">
      <div class="select-box">
        <div class="genre">{{ selected }}</div>
        <form>
          <span><i class="fa-solid fa-circle-check"></i> pick</span>
          <select id="select-form" class="select" name="genre" @change="getGenres">
            <option disabled selected> -- Genre --</option>
            <option v-for="(genre, idx) in genres" :key="idx" :value="genre.genre_id">{{ genre.genre_name }}</option>
          </select>
        </form>
      </div>
      <div>
      </div>
      <div class="content-box">
        <div class="scroll-area">
          <div class="content-area" v-if="isChoiced">
              <div class="item" v-for="(result, idx) in genreMovie" :key="idx" @click="getDetail(result.id)">
                <div class="content-img">
                  <img :src="result.poster_path" alt="">
                </div>
              <div class="content-desc">
                <div class="content-title">
                  {{ result.title }}
                </div>
                  <div class="content-overview">
                    <p>{{ result.overview }}</p>
                  </div>
              </div>
            </div>
          </div>
          <div v-else>
            <img src="@/assets/noResult.png" alt="" class="no-result">
            <div class="no-result-text">
              Please select a genre!!!
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar.vue'
import SearchResult from '@/components/SearchResult.vue'
import {mapGetters, mapActions} from 'vuex'

export default {

  name: "AboutView",
  data () {
    return {
      selected : '',
      choice : '1',
      isChoiced : false
    }
  },
  components: {
    SearchBar,
    SearchResult,
  },
  methods: {
    ...mapActions(['navToggle', 'exitResult','getGenreList', 'getGenreMovies', 'getDetail', 'getGenreList',]),
    getGenres () {
    const select = document.querySelector('#select-form')
    this.isChoiced = true
    this.choice = select.value
    this.selected = select[select.selectedIndex].text
    this.getGenreMovies(this.choice)
    },

  },
  computed: {
    ...mapGetters(['navState', 'showResult', 'siteRanking', 'genres', 'genreMovie','genreName'])
  },
  created () {
    this.navToggle(true)
    this.exitResult()
    this.getGenreList()
  },
}
</script>

<style scoped>
  .about {
    position: relative;
    overflow: hidden;
    height: 100vh;
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

  .genre {
    position: relative;
    font-size: 60px;
    font-family: 'Nanum Pen Script', cursive;
    width: 50%;
    margin: 0;
    padding: 0;
  }

  .content {
    position: relative;
    left: 200px;
    top: 30px;
    height: 700px;
    width: 1400px;
  }

  .item {
    position: relative;
    width: 50%;
    height: 100%;
    display: flex;
    margin-bottom: 20px;
    border-radius: 10px;
  }
  
  .item:hover {
    background-color: rgba(0,0,0,0.2);
    cursor: pointer;
  }

  .select-box {
    position: relative;
    height: 15%;
    width: 100%;
    display: flex;
    align-items: center;
  }
  
  .select-box form {
    width: 50%;
  }

  .select-box span {
    font-size: 30px;
    margin-right: 30px;
    color: #666;
  }

  .content-box {
    position: relative;
    background-color: rgba(255,255,255,0.4);
    border-radius: 10px;
    height: 85%;
    width: 100%;
  }

  .content-area {
    position: relative;
    height: 40%;
    width: 100%;
    border-radius: 10px;
    display: flex;
    flex-flow: row wrap;
  }

  .scroll-area {
    position: relative;
    top: 10%;
    height: 80%;
    left: 5%;
    right: 5%;
    width: 90%;
    border-radius: 10px;
    overflow: auto;
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
  
  select {
    text-align: center;
    width: 250px;
    padding: 10px;
    border-radius: 10px;
    border-radius: 10px;
    border: none;
    background-color: rgba(255,255,255,0.8);
    -webkit-appearance: none;
    appearance: none;
    font-size: 25px;
    font-family: 'Nanum Pen Script', cursive;
    
  }
  
  .select {
  background-color: rgba(255,255,255,0.8);
  }

  .select-box .select option {
  background: rgba(255,255,255,0.8);
  color: #666;
  font-size: 25px;
  font-family: 'Nanum Pen Script', cursive;
}

.select:hover {
  border: 2px solid gray
}

.select:focus {
  outline: none;
}

.content-img {
    height: 180px;
    width: 30%;
  }

  .content-img img {
    height: 100%;
    border-radius: 10px;
  }

  .content-desc {
    height: 180px;
    width: 75%;
  }

  .content-title {
    margin-top: 20px;
    height: 35%;
    display: flex;
    font-size: 36px;
    text-align: start;
    align-items: center;
    color: #666;
    font-family: 'Nanum Pen Script', cursive;
  }

  .content-genre {
    height: 10%;
    text-align: start;
    margin-top: 5px;
  }

  .genres {
  position: relative;
  display: inline;
  font-size: 20px;
  font-family: 'Nanum Pen Script', cursive;

}

  p {
  font-family: 'Dongle', sans-serif;
  font-size: 24px;
  overflow: visible;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2; /* 라인수 */
  -webkit-box-orient: vertical;
  word-wrap:break-word; 
  line-height: 1.2em;
  height: 3.6em; /* line-height 가 1.2em 이고 5라인을 자르기 때문에 height는 1.2em * 5 = 6.0em */
  }

  .content-overview {
    height: 45%;
    overflow: hidden;
    padding-top: 20px;
    padding-right: 20px;
    padding-left: 10px;
    text-align: start;
    font-size: 14px;
  }

  .content-about {
    height: 15%;
    text-align: end;
    font-size: 14px;
    padding-right: 50px;
  }

  .no-result {
    height: 380px;
  }

  .no-result-text {
    margin-top: 20px;
    font-size: 50px;
    font-weight: bold;
    color: rgba(0, 0, 0, 0.5);
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
</style>