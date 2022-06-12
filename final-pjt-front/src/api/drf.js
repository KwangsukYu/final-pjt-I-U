const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const COMMUNITY = 'community/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
  },

  movies: {
    getSiteRank: () => HOST + MOVIES + 'site_rank_movie/',
    getNowPlayRank: () => HOST + MOVIES + 'nowplay_rank',
    getMovieDetail: movieId => HOST + MOVIES + movieId,
    Search: () => HOST + MOVIES + 'search/',
    getGenres: () => HOST + MOVIES + 'genres/',
    getGenreMovie: (genreId) => HOST + MOVIES + 'genres/' + genreId + '/',
    getRecommend: (movieId) => HOST + MOVIES + movieId + '/recommend/',
    getRandomMovies : () => HOST + MOVIES + 'random_movie/',
    getLikeRecommend: (movieId) => HOST + MOVIES + movieId + '/like_recommend/',
    likeMovie: (movieId) => HOST + MOVIES + 'like_movie/' + movieId + '/',
  },

  articles : {
    getArticle: (movieId) => HOST + COMMUNITY + movieId + '/articles/',
    getArticles: () => HOST + COMMUNITY + 'articles/',
    getDetail: (articleId) => HOST + COMMUNITY + 'articles/' + articleId + '/',
    createComment: (articleId) => HOST + COMMUNITY + 'articles/' + articleId + '/comments/',
    likeaArticle: (articleId) => HOST + COMMUNITY + 'like_article/' + articleId + '/',
    getComments: (articleId) => HOST + COMMUNITY + articleId + '/comments/',
    delComment: (commentId) => HOST + COMMUNITY + 'comments/' + commentId + '/'
  }
}