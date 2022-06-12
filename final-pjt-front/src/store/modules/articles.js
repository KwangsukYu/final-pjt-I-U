import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'
import Swal from 'sweetalert2'

// import _ from 'lodash'

export default {
  state : {
    article: {},
    articles: [],
    articleDetail: {},
    commentList: [],
  },

  getters : {
    article: state => state.article,
    articles: state => state.articles,
    articleDetail: state => state.articleDetail,
    isAuthor: (state, getters) => {
      return state.articleDetail.user.username === getters.currentUser.username
    },
    commentList: state => state.commentList
  },

  mutations : {
    SET_ARTICLE: (state, article) => state.article = article,
    SET_ARTICLES: (state, articles) => state.articles = articles,
    SET_ARTICLE_DETAIL : (state, data) => state.articleDetail = data, 
    SET_COMMENT_LIST : (state, data) => state.commentList = data,
    ADD_COMMENT_LIST : (state, data) => state.commentList.unshift(data),
    DELETE_COMMENT_LIST : (state, data) => 
    state.commentList.splice(state.commentList.indexOf(data),1),
  },

  actions: {
    articleCreate ({commit, getters}, article) {
      axios ({
        url : drf.articles.getArticle(article.movieId),
        method : 'post',
        data: {
          title : article.title,
          content : article.content
        },
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_ARTICLE', res.data)
          router.replace({name:'community'})
        })
        .catch(err => alert(err.message))
    },
    
    articleList ({commit}) {
      axios ({
        url : drf.articles.getArticles(),
        method: 'get',
      })
      .then(res => {
        commit('SET_ARTICLES', res.data)
      })
      .catch(err => alert(err.message))
    },

    getArticleDetail ({commit, getters}, articleId) {
      if (!getters.isLoggedIn) {
        router.replace({ name: 'login'})
        return
      }
      axios ({
        url : drf.articles.getDetail(articleId),
        method: 'get',
        headers: getters.authHeader,
      })
      .then(res=> {
        commit('SET_ARTICLE_DETAIL', res.data)
        router.push({name:'articledetail', params:{articleId : articleId}})
      })
      .catch(err => alert(err.message))
    },

    getArticleInfo ({commit, getters}, articleId) {
      if (!getters.isLoggedIn) {
        router.replace({ name: 'login'})
        return
      }
      axios ({
        url : drf.articles.getDetail(articleId),
        method: 'get',
        headers: getters.authHeader,
      })
      .then(res=> {
        commit('SET_ARTICLE_DETAIL', res.data)
      })
      .catch(err => alert(err.message))
    },

    updateArticle ({commit, getters}, article) {
      if (!getters.isLoggedIn) {
        router.replace({ name: 'login'})
        return
      }
      axios ({
        url : drf.articles.getDetail(article.articleId),
        method: 'put',
        data : {
          title : article.title,
          content : article.content
        },
        headers: getters.authHeader,
      })
      .then(res=> {
        commit('SET_ARTICLE_DETAIL', res.data)
        router.push({name : 'community'})
      })
      .catch(err => console.log(err.message))
    },

    deleteArticle ({commit, getters}, articleId) {
      if (!getters.isLoggedIn) {
        router.replace({ name: 'login'})
        return
      }
      const Swal = require('sweetalert2')
      Swal.fire({
        title: '진짜 할거야?',
        text: "정말로 할거야?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#4aa8d8',
        cancelButtonColor: '#ffc0cb',
        confirmButtonText: '진행 해!',
        cancelButtonText: '멈...멈춰!'
      }).then((result) => {
        if (result.isConfirmed) {
          axios ({
            url : drf.articles.getDetail(articleId),
            method: 'delete',
            headers: getters.authHeader,
          })
          .then(res=> {
            commit('SET_ARTICLE_DETAIL', res.data)
            Swal.fire(
              '삭제했다...!',
              '오늘도 게시글 하나가 사라졌어...',
              'success'
          )
            router.push({name : 'community'})
          .catch(err => console.log(err.message))
            }
          )
        }
      })
    },

    addComment ({commit, getters}, article) {
      if (!article.content.trim()) {
        Swal.fire('No Content!')
        return
      }
      axios ({
        url : drf.articles.createComment(article.id),
        method : 'post',
        data : {
          content: article.content
        },
        headers: getters.authHeader,
      }).then(res => {
        commit('ADD_COMMENT_LIST', res.data)
      }
      )
      .catch(err => alert(err.message))
    },

    addLike ({getters}, articleId) {
      axios ({
        url : drf.articles.likeaArticle(articleId),
        method : 'get',
        headers: getters.authHeader
      })
      .catch(err => alert(err.message))
    },

    
    getCommentList ({commit, getters}, articleId) {
      axios ({
        url : drf.articles.getComments(articleId),
        method : 'get',
        headers: getters.authHeader
      }).then(res => {
        commit('SET_COMMENT_LIST', res.data)
      }).catch(err => alert(err.message))
    },

    deleteComment ( { commit, getters}, comment) {
      const Swal = require('sweetalert2')
        Swal.fire({
          title: '진짜 할거야?',
          text: "정말로 할거야?",
          icon: 'warning',
          showCancelButton: true,
          confirmButtonColor: '#4aa8d8',
          cancelButtonColor: '#ffc0cb',
          confirmButtonText: '진행 해!',
          cancelButtonText: '멈...멈춰!'
        })
        .then((result) => {
          if (result.isConfirmed) {
            axios ({
              url : drf.articles.delComment(comment.pk),
              method: 'delete',
              headers: getters.authHeader,
            })
            .then(commit('DELETE_COMMENT_LIST', comment))
              Swal.fire(
                '삭제했다...!',
                '오늘도 댓글 하나가 사라졌어...',
                'success'
            )
          }
        })
    },

    async editComment ({dispatch, getters}, comment) {
      const { value: text } = await Swal.fire({
        input: 'textarea',
        inputLabel: 'Edit Comment',
        inputPlaceholder: 'Type your comment here...',
        inputAttributes: {
          'aria-label': 'Type your message here'
        },
        showCancelButton: true,
        confirmButtonColor: '#4aa8d8',
        cancelButtonColor: '#ffc0cb',
      })
      if (text) {
        axios ({
          url : drf.articles.delComment(comment.pk),
          method : 'put',
          data : {
            content: text
          },
          headers: getters.authHeader,
        }).then( res => 
        dispatch('getCommentList', res.data.article))
      }
    }
  }
}