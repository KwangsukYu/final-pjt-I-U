import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import IntroView from '../views/IntroView'
import GenreView from '../views/GenreView.vue'
import RecommendationView from '../views/RecommendationView.vue'
import LogInView from '../views/LogInView.vue'
import SignUpView from '../views/SignUpView'
import MovieDetailView from '../views/MovieDetailView'
import TestView from '../views/TestView'
import ArticleFormView from '../views/ArticleFormView'
import ArticleChangeFormView from '../views/ArticleChangeFormView'
import CommunityView from '../views/CommunityView'
import ArticleDetailView from '../views/ArticleDetailView'
import ProfileView from '../views/ProfileView'
import NotFound404 from '../views/NotFound404'
import store from '../store'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'intro',
    component: IntroView
  },
  {
    path: '/home',
    name: 'home',
    component: HomeView
  },
  {
    path: '/genre',
    name: 'genre',
    component: GenreView
  },
  {
    path: '/recommendation',
    name: 'recommendation',
    component: RecommendationView
  },
  {
    path: '/login',
    name: 'login',
    component: LogInView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/movie/detail/:id',
    name: 'movie',
    component: MovieDetailView
  },
  {
    path: '/test',
    name: 'test',
    component: TestView
  },
  {
    path: '/community',
    name: 'community',
    component : CommunityView
  },
  {
    path: '/articleform',
    name: 'articleform',
    component: ArticleFormView
  },
  {
    path: '/articleform/:articleId',
    name: 'articleupdate',
    component: ArticleChangeFormView
  },
  {
    path: '/articles/:articleId',
    name: 'articledetail',
    component: ArticleDetailView
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404',
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
})

router.beforeEach((to, from, next) => {
  store.commit('SET_AUTH_ERROR', null)
  !to.name ? next({ name: 'NotFound' }) : next()
})

export default router
