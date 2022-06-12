<template>
  <div class="main">
    <div class="contents">
      <div @click="exitResult" class="back-btn">
        <i class="fa-solid fa-xmark"></i>
      </div>
      <div class="keyword">
        <i class="fa-solid fa-magnifying-glass"></i> "{{ searchquery }}"
      </div>
      <div>
        About {{ searchresults.length }} results
      </div>
      <div v-if="!!searchresults.length"  class="content-box">
        <div class="content" v-for="(result, idx) in searchresults" :key="idx" @click="getDetail(result.id)">
          <div class="content-img">
            <img :src="result.poster_path" alt="">
          </div>
          <div class="content-desc">
            <div class="content-title">
              {{ result.title }}
            </div>
            <div class="content-genre">
              <p class="genres" v-for="(genre, idx) in result.genres" :key="idx" > {{ genre.genre_name }}</p>
            </div>
            <div class="content-overview">
              <p>{{ result.overview }}</p>
            </div>
          </div>
        </div>
      </div>
      <div v-else class="no-result">
        <img src="@/assets/noResult.png" alt="">
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'SerachResult',
  methods: {
    ...mapActions(['exitResult', 'getDetail'])
  },
  computed: {
    ...mapGetters(['searchresults', 'searchquery'])
  }
}
</script>

<style scoped>
  
  .main {
    position: absolute;
    height: 100vh;
    width: 100vw;
    background-color: rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(10px);
    z-index: 110;
  }

  .contents {
    position: relative;
    top: 50px;
    left: 600px;
    height: 880px;
    width: 900px;
    background-color: rgba(255, 255, 255, 0.8);
    border-radius: 10px;
    z-index: 2;
  }

  .back-btn {
    position: absolute;
    color:#666;
    font-size: 46px;
    right: 10%;
    top: 5%;
    cursor: pointer;
  }

  .back-btn:hover {
    transform: scale(1.2);
  }

  .keyword {
    padding-top: 80px;
    font-size: 40px;
  }

  .content-box {
    position: relative;
    left: 10%;
    width: 80%;
    right: 10%;
    height: 71%;
    overflow: auto;
    top: 30px;
    border-radius: 10px;
  }

  .content-box::-webkit-scrollbar {
    width: 15px;
  }

  .content-box::-webkit-scrollbar-thumb {
    background-color: #666; /*스크롤바의 색상*/
    border: 2px solid transparent;
    background-clip: padding-box;
    border-radius: 10px;
  }

  .content-box::-webkit-scrollbar-track {
    position: absolute;
    background-color: rgba(255, 255, 255, 0.3);
    border-radius: 10px;
    border: 3px solid transparent;
    background-clip: padding-box;
  }

  .content {
    margin-top: 50px;
    display: flex;
    border: none;
  }

  .content:hover {
  background-color: rgba(0, 0, 0, 0.2);
  border-radius: 10px;
  box-shadow: 5px rgba(255, 255, 255, 0.7);
  cursor: pointer;
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
    text-align: start;
  }

  .no-result {
    position: relative;
    top: 80px;
  }

</style>