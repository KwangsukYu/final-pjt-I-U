<template>
  <div class="box fadein">
    <div class="title">
      <span class="grey">Now</span>
      <span class="white">Playing</span>
    </div>
    <swiper
      class="fadein"
      :slides-per-view="6"
      :space-between="30"
      :loop="false"
      :pagination="false"
      :navigation="true"
    >
      <swiper-slide
        v-for="(movie, idx) in nowPlaying"
        :key="idx"
        class="test"
        :class="{test_2: true}"
      >
      <div class="card-container">
        <div class="desc">
          <div class="movie-title">
            {{ movie.title }}
          </div>
          <div class="movie-desc">
            {{ movie.overview }}
          </div>
          <div @click="getDetail(movie.id)" class="detail"> Detail </div>
        </div>
        <img
          :src="movie.poster_path"
          class="img-fluid w-100 mx-auto card"
          blank="true"
        >
      </div>
      </swiper-slide>
    </swiper>
  </div>
</template>

<script>
import { Navigation, Pagination } from 'swiper'

import { SwiperCore, Swiper, SwiperSlide } from 'swiper-vue2'

import { mapGetters, mapActions } from 'vuex'
// Import Swiper styles
import 'swiper/swiper-bundle.css'

SwiperCore.use([Navigation, Pagination])

export default {
  components: {
    Swiper,
    SwiperSlide
  },
  methods: {
    ...mapActions(['getNowPlay', 'getDetail']),
  },
  mounted() {
    this.getNowPlay()
  },
  computed: {
    ...mapGetters(['nowPlaying']),
  }
}
</script>

<style lang="scss" scoped>

.img-fluid {
  max-width: 100%;
  height: auto;
}
.w-100 {
  width: 100%;
}
.ml-auto, .mx-auto {
  margin-left: auto;
}
.mr-auto, .mx-auto {
  margin-right: auto;
}

.box {
  position: relative;
  left: 10vw;
  top: 1vh;
  width: 70vw;
}

.card-container {
  position: relative;
}

.movie-title {
  position: absolute;
  top: 10%;
  left: 5%;
  right: 5%;
  font-size: 24px;
  color: white;
  font-weight: bold;
  font-family: 'Dongle', sans-serif;
  padding-left: 10px;
  padding-right: 10px;
}

.movie-desc {
  position: absolute;
  top: 40%;
  bottom: 30%;
  left: 5%;
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
  padding-left: 10px;
  padding-right: 10px;
}

.detail {
  display: inline-block;
  position: absolute;
  bottom: 7.5%;
  right: 30%;
  left: 30%;
  width: 40%;
  background: white;
  text-decoration: none;
  color: #666;
  margin: 5px;
  border-radius: 10px;
  font-size: 20px;
  font-family: 'Dongle', sans-serif;
  cursor: pointer;
}

.card-container:hover {
  background: rgba(0, 0, 0, 0.7);
  border-radius: 12px;
}

.desc {
  display: none;
}

.card-container:hover .desc {
  display: block;
}

.card {
  border-radius: 10px;
  border: none;
  height: 25vh;
  z-index: -1;
}

.title {
  text-align: start;
  font-size: 2.5rem;
  margin-bottom: 20px;
  color: white;
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
  margin-left: 7vh;
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

