import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'
import swal from 'sweetalert'


export default {
  state: {
    siteRanking: [],
    nowPlaying: [],
    movieDetail: {},
    searchresults: [],
    searchquery: '',
    showResult: false,
    genres: '',
    genreMovie: [],
    defaultgenre : 'Pick One!!!',
    genreName: '',
    recoMovies: [],
    randomMovies : [],
    likerecommend : [],
    userLiked : false,
  },
  getters: {
    siteRanking: state => state.siteRanking,
    nowPlaying: state => state.nowPlaying,
    movieDetail: state => state.movieDetail,
    searchresults: state => state.searchresults,
    searchquery: state => state.searchquery,
    showResult: state => state.showResult,
    genres: state => state.genres,
    genreMovie: state => state.genreMovie,
    genreName: state => state.genreName,
    getRecoMovies: state => state.recoMovies,
    getrandomMovies: state => state.randomMovies,
    getlikerecommend: state => state.likerecommend,
    userLiked: state => state.userLiked,
  },
  mutations: {
    SET_SITE_RANKING: (state, siteRanking) => state.siteRanking = siteRanking,
    SET_NOW_PLAYING: (state, data) => state.nowPlaying = data,
    SET_MOVIE_DETAIL: (state, movieId) => state.movieDetail = movieId,
    SET_SEARCH_RESULTS: (state, results) => state.searchresults = results,
    SET_SEARCH_QUERY: (state, query) => state.searchquery = query,
    SET_NO_RESULT: (state) => state.searchresults = [],
    SET_SHOW_RESULT: (state, bool) => state.showResult = bool,
    SET_GENRES : (state, data) => state.genres = data,
    SET_GENRE_MOVIE : (state, data) => state.genreMovie = data,
    SET_GENRE_NAME : (state, data) => state.genreName = data,
    SET_RECO_MOVIES : (state, data) => state.recoMovies = data,
    SET_RANDOM_MOVIES : (state, data) => state.randomMovies = data,
    SET_LIKE_RECO : (state, data) => state.likerecommend = data,
    SET_LIKED : (state, data) => state.userLiked = data,
  },
  actions: {
    getRank ({commit}) {
      axios({
        url: drf.movies.getSiteRank(),
        method: 'get'
      })
      .then(res => {
        commit('SET_SITE_RANKING', res.data)
      })
      .catch(err => swal(err.message))
    },

    getNowPlay ({commit}) {
      axios({
        url: drf.movies.getNowPlayRank(),
        method: 'get'
      })
      .then(res => {
        commit('SET_NOW_PLAYING', res.data)
      })
      .catch(err => swal(err.message))
    },

    getDetail ({commit,getters}, movieId) {
      if (!getters.isLoggedIn) {
        router.replace({ name: 'login'})
        return
      }
      axios({
        url: drf.movies.getMovieDetail(movieId),
        method: 'get'
      })
      .then(res => {
        commit('SET_MOVIE_DETAIL', res.data)
        for (let i = 0; i < getters.profile.favorite_movies.length; i++ ){
          if (getters.profile.favorite_movies[i] === res.data.id) {
            commit('SET_LIKED', true)
          }
        }
      })
      .catch(err => swal(err.message))
      router.push({ name:'movie', params:{id:movieId}})
    },
    
    getSearchResult ({commit}, query) {
      if (!query.trim()) {
        commit('SET_NO_RESULT')
        swal('Enter Title Here', '', 'info')
        return
      }
      commit('SET_SEARCH_QUERY', query)
      axios({
        url: drf.movies.Search(),
        method: 'post',
        data: {
        keyword: query
        }
      })
      .then(res => {
        commit('SET_SEARCH_RESULTS', res.data)
        console.log(res.data)
        commit('SET_SHOW_RESULT', true)
      })
      .catch(err => alert(err.message))
    },
    
    exitResult ({commit}) {
      commit('SET_SHOW_RESULT', false)
    },
    getGenreList ({commit}) {
      axios({
        url: drf.movies.getGenres(),
        method: 'get'
      })
        .then(res => {
          commit('SET_GENRES', res.data)
        })
        .catch(err => alert(err.message))
    },
    getGenreMovies ({commit}, genreId) {
      axios({
        url: drf.movies.getGenreMovie(genreId),
        method: 'get'
      })
        .then(res => {
          commit('SET_GENRE_MOVIE', res.data)
          commit('SET_GENRE_NAME', genreId)
        })
        .catch(err => alert(err.message))
    },

    getRecommend ({commit, getters}, movieId) {
      axios({
        url: drf.movies.getRecommend(movieId),
        method: 'get',
        headers: getters.authHeader,
      })
        .then (res => {
          commit('SET_RECO_MOVIES', res.data)
        })
        .catch (err => alert(err.response))
    },

    getRandoms ({commit, getters}) {
      axios({
        url: drf.movies.getRandomMovies(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then (res => {
          console.log(getters.profile.favorite_movies)
          commit('SET_RANDOM_MOVIES', res.data)
        })
        .catch (err => alert(err.response))
    },

    getLikeReco ( {commit, getters}, movieId ) {
      axios({
        url: drf.movies.getLikeRecommend(movieId),
        method: 'get',
        headers: getters.authHeader,
      }) 
      .then (res =>{
        commit('SET_LIKE_RECO', res.data)
      })
      .catch (err => console.err(err.message))
    },

    movieLike ({commit, getters}, movieId) {
      axios({
        url : drf.movies.likeMovie(movieId),
        method : 'get',
        headers: getters.authHeader,
      }).then(res => {
        console.log(res.data.data)
        if (res.data.data === "add") {
          commit('SET_LIKED', true)
        } else {
          commit('SET_LIKED', false)
        }
    })
    }
  },
}