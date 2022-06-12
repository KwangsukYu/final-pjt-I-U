<template>
  <div class="main">
    <div class="box">
    <div class="back-btn" @click="Back">
      <i class="fa-solid fa-xmark"></i>
    </div>
      <div class="header">
        <div class="info">
          <div class="a-info">
            <div class="a-t">
              {{ articleDetail.title }}
            </div>
            <div class="m-t" >
              <span @click="getDetail(articleDetail.movie.id)">{{ articleDetail.movie.title }}</span>
              <span class="go-profile" @click="fetchProfile(articleDetail.user.username)"> <i class="fa-solid fa-address-card"></i> Author. {{articleDetail.user.username}} </span>
            </div>
          </div>
          <div class="a-content">
            {{ articleDetail.content }}
          </div>
        </div>
        <div class="m-info">
          <img :src="articleDetail.movie.poster_path" alt="">
          <div class="actor">
            <div v-for="(actor, idx) in articleDetail.movie.actors" :key="idx">
              <div v-if="idx<3" class="actor-detail">
                <img  :src="actor.profile_path" alt="" class="actor-profile">
                <span>{{ actor.name }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="a-comment">
        <div class="comment-scroll">
          <div v-if="!commentList.length" class="comment-item">
            add a comment
            <div class="comment-user">
              :)
            </div>
          </div>
          <div v-else class="comment-item" v-for="(comment, idx) in commentList" :key="idx">
            {{ comment.content}}
            <div @click="editComment(comment)" v-show="comment.user.username === currentUser.username" class="edit-btn"> <i class="fa-solid fa-pen-to-square"></i></div>
            <div @click="deleteComment(comment)" v-show="comment.user.username === currentUser.username" class="del-btn"> <i class="fa-solid fa-xmark"></i></div>
            <div @click="fetchProfile(comment.user.username)" class="comment-user">
              {{ comment.user.username }}
            </div>
          </div>
        </div>
        <div class="comment-box">
          <button @click="moveToUpdate" v-show="isAuthor" class="update-btn">Update</button>
          <div>
            <i @click="cToggle" v-if="commentState" class="fa-solid fa-circle-plus add-comment"></i>
            <i @click="cToggle" v-if="!commentState" class="fa-solid fa-circle-minus add-comment"></i>
            <i v-if="!liked" @click="like" class="fa-solid fa-heart like-btn"></i>
          </div>
          <div v-if="!commentState">
            <input id="c-input" v-model="content" class="comment-input">
            <button @click="add">Add</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
import {mapActions} from 'vuex'

export default {
  name: "ArticleDetailView",
  data () {
    return {
      commentState : true,
      id : this.$route.params.articleId,
      content : '',
      liked : '',
    }
  },
  created () {
    this.isLiked()
    this.navToggle(false)
    this.getCommentList(this.$route.params.articleId)
  },
  computed: {
    ...mapGetters(['articleDetail', 'isAuthor', 'currentUser', 'isLoggedIn', 'navState', 'commentList']),
  },
  methods :{
    ...mapActions(['addComment', 'addLike','fetchProfile', 'getDetail', 'navToggle','getCommentList', 'deleteComment','editComment']),
    like() {
      this.addLike(this.id)
      this.isLiked()
      document.querySelector('.like-btn').classList.add('fadeout')
    },
    isLiked () {
      let state = false
      for (let i = 0 ; i < this.articleDetail.article_users.length; i++) {
        if (this.articleDetail.article_users[i].username === this.currentUser.username) {
          state = true
        }
      }
      this.liked = state
    },
    Back () {
      this.$router.back()
    },
    cToggle () {
      this.commentState = !this.commentState
    },
    add () {
      const article = {
        id : this.id,
        content : this.content
      }
      this.addComment(article)
      this.content = ''
    },
    moveToUpdate () {
      this.$router.push({name:'articleupdate', params:{articleId:this.articleDetail.id}})
    },
    moveToprofile (username) {
      this.$router.push({name:'profile', params:{username:username}})
    }
  },
}
</script>

<style scoped>
  .main {
    position: relative;
    background-color: rgba(255,255,255,0.5);
    top: 50px;
    left:400px;
    height: 870px;
    width: 1200px;
    border-radius: 10px;
  }

  .back-btn {
    position: absolute;
    font-size: 40px;
    right: -10px;
    top: -30px;
    cursor: pointer;
  }

  .back-btn:hover {
    transform: scale(1.2);
  }

  .box {
    position: relative;
    width: 90%;
    top: 5%;
    left: 5%;
    height: 90%;
    border-radius: 10px;
  }

  .header {
    position: relative;
    width: 100%;
    height: 60%;
    display: flex;
    
  }

  .m-info {
    position: relative;
    width: 40%;
    height: 100%;
    padding: 30px;
  }

  .m-info img {
    height: 300px;
    border-radius: 10px;
    display: block;
    margin:auto;
  }

  .info {
    position: relative;
    width: 60%;
    height: 100%;
    border-radius: 10px;
    background-color: rgba(255, 255, 255, 0.2);
  }

  .a-info {
    padding-top : 20px;
    position: relative;
    width: 100%;
    height: 30%;
  }

  .a-content {
    padding: 20px;
    position: relative;
    width: 90%;
    height: 62%;
    text-align: start;
    margin-top : 10%;
    margin-left: 5%;
    border-radius: 10px;
    overflow: auto;
    background-color: rgba(255,255,255,0.4);
    font-family: 'Dongle', sans-serif;
    font-size: 30px;
  }

  .a-content::-webkit-scrollbar {
    width: 20px;
  }

  .a-content::-webkit-scrollbar-thumb {
    background-color: white; /*스크롤바의 색상*/
    border: 2px solid transparent;
    background-clip: padding-box;
    border-radius: 10px;
  }

  .a-content::-webkit-scrollbar-track {
    position: absolute;
    background-color: rgba(0, 0, 0, 0.5);
    border-radius: 10px;
    border: 5px solid transparent;
    background-clip: padding-box;
  }

  .a-comment {
    position: relative;
    width: 100%;
    margin-top: 2%;
    height: 35%;
    border-radius: 10px;

  }

  .actor {
    position: absolute;
    width: 100%;
    height: auto;
    display: flex;
    justify-content: space-evenly;
    align-items: center;
  }

  .actor-profile {
    max-height: 120px;
    max-width: 100px;
  }

  .actor-detail {
    width: 150px;
    margin-top : 30px;
  }

  .a-t {
    font-size: 40px;
    font-family: 'Nanum Pen Script', cursive;
    padding-left: 30px;
    color: black;
    height: 130px;
  }

  .m-t {
    display: flex;
    justify-content: space-between;
    padding-left : 10px;
    padding-right: 30px;
  }

  .m-t > span {
    font-size: 30px;
    font-family: 'Nanum Pen Script', cursive;
    padding-left: 30px;
  }

  .m-t span:hover {
    transform: scale(1.2);
    transition: 1s;
    cursor: pointer;
  }

  .comment-box {
    position: absolute;
    right: 0%;
    bottom: -15%;
  }

  .like-btn {
    font-size: 36px;
    position: absolute;
    right: 0%;
    bottom: 50px;
    color: red;
  }
  
  .like-btn:hover {
    transform: scale(1.2);
    cursor: pointer;

  }
  .fadeout {
    transform: translate(0,-100px);
    transition: 2s;
    animation: 2s fadeout linear;
    animation-fill-mode: forwards;
  }

  @keyframes fadeout{
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
    z-index: -10;
  }
}



  .add-comment {
    font-size: 36px;
  }

  .add-comment:hover {
    transform: scale(1.2);
    cursor: pointer;
  }

  .comment-input {
    position: absolute;
    bottom: 0px;
    right: 50px;
    width: 500px;
    height: 100%;
    outline: none;
    border:none;
    border-radius: 10px;
    background-color: rgba(0, 0, 0, 0.2);
    padding-left : 10px;
  }

  button {
    position: absolute;
    bottom: 0px;
    right: 50px;
    width: 70px;
    height: 110%;
    outline: none;
    border: none;
    background-color: white;
    border-radius: 10px;
  }

  button:hover {
    transform: scale(1.2)
  }

  .comment-state {
    display: none;
  }

  .comment-scroll {
  position: relative;
  top: 10%;
  height: 80%;
  left: 5%;
  right: 5%;
  width: 90%;
  border-radius: 10px;
  overflow-y: auto;
  }

  .comment-scroll::-webkit-scrollbar {
    width: 20px;
  }

  .comment-scroll::-webkit-scrollbar-thumb {
    background-color: white; /*스크롤바의 색상*/
    border: 2px solid transparent;
    background-clip: padding-box;
    border-radius: 10px;
  }

  .comment-scroll::-webkit-scrollbar-track {
    position: absolute;
    background-color: rgba(0, 0, 0, 0.5);
    border-radius: 10px;
    border: 5px solid transparent;
    background-clip: padding-box;
  }

  .comment-item {
    display: flex;
    text-align: start;
    justify-content: flex-start;
    align-items: center;
    border-radius: 10px;
    position: relative;
    height: auto;
    width: 80%;
    margin: 10px;
    color: #666;
    background-color: rgba(255, 192, 203, 0.5);
    font-size: 23px;
    padding: 10px ;
    font-weight: bold;
    font-family: 'Dongle', sans-serif;
  }

  .comment-user {
    position: absolute;
    right: -20%;
    width: 18%;
    height: 40px;
    background-color: rgba(255, 236, 196, 0.5);
    font-size: 24px;
    text-align: center;
    font-family: 'Nanum Pen Script', cursive;
    color: #666;
  }

  .comment-user:hover {
    text-decoration: underline;
    cursor: pointer;
  }

  input:focus {
    border: solid 4px wheat
  }

  .actor span {
    font-size: 10px;
  }

  .go-profile {
    color: #666;
    cursor: pointer;
  }
  
  .go-profile:hover {
    transform: scale(1.2);
    transition: 1s;
  }

  .update-btn {
    position: absolute;
    right: 960px;
    bottom: 10px;
    background: #fff;
    color: #666;
    cursor: pointer;
    width: 100px;
    font-weight: 600;
    text-align: center;
    border-radius: 10px;
    border: none;
    height: 40px;
    margin-left: 20px;
    margin-right: 20px;
  }

  .del-btn {
    position: absolute;
    right: 0;
    width: 50px;
    height: 100%;
    border-radius: 10px;
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 20px;
  }

  .del-btn:hover {
    transform: scale(1.2);
    font-weight: bold;
    background-color: #fff;
  } 

    .edit-btn {
    position: absolute;
    right: 50px;
    width: 50px;
    height: 100%;
    border-radius: 10px;
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 20px;
  }

  .edit-btn:hover {
    transform: scale(1.2);
    font-weight: bold;
    background-color: #fff;
  } 

</style>