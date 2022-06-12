<template>
  <div class="main fadein">
    <div class="back-btn" @click="moveToBack">
      <i class="fa-solid fa-xmark"></i>
    </div>
    <div class="articleform">
      <div class="article">
        Article
      </div>
      <div class="under-line"></div>
      <div class="title">
        <div class="movie-title">
          <div class="select-box">
            <div> Movie Title</div>
            <select class="select" name="movie-title" id="movie-title" @change="getTitle">
              <option disabled selected> {{ articleDetail.movie.title }}</option>
            </select>
          </div>
        </div>
        <div class="article-title">
          <div>
            Article Title
          </div>
          <input v-model="articleTitle" type="text" placeholder="Title...">
        </div>
      </div>
      <div class="article-content">
        <div> Article Content </div>
        <textarea v-model="articleContent" name="article-content" id="article-content" cols="30" rows="10">
        </textarea>
      </div>
      <div class="article-footer">
        <button @click="deleteArticle(articleDetail.id)">Delete</button>
        <button @click="submit">Submit</button>
      </div>
    </div>
  </div>
    
</template>

<script>

import { mapActions } from 'vuex'
import { mapGetters } from 'vuex'

export default {
  name: 'ArticleFormView',
  data () {
    return {
      articleTitle : ',',
      articleContent : ''
    }
  },
  computed:{
    ...mapGetters(['genreMovie', 'navState', 'articleDetail'])
  },
  methods: {
    ...mapActions(['articleCreate', 'navToggle', 'getArticleInfo','updateArticle', 'deleteArticle']),
    moveToBack () {
      this.$router.replace({name:'community'})
    },
    getTitle () {
      const select = document.querySelector(".select")
      this.movieId = select.value
    },
    submit () {
      const article = {
        articleId : this.articleDetail.id,
        title : this.articleTitle,
        content : this.articleContent
      }
      this.updateArticle(article)
    },
  },
  created () {
    this.navToggle(false)
    this.getArticleInfo(this.$route.params.articleId)
    this.articleTitle = this.articleDetail.title
    this.articleContent = this.articleDetail.content
  }
}
</script>

<style scoped>

  .main {
    position: relative;
    top: 50px;
    height: 870px;
    width: 800px;
    left: 550px;
    background-color: rgba(255, 255, 255, 0.5);
    border-radius: 10px;
    border: 1px solid rgba(255, 255, 255, 0.5);
    border-right: 1px solid rgba(255, 255, 255, 0.2);
    border-bottom: 1px solid rgba(255, 255, 255, 0.2);
    box-shadow: 0 5px 15px rgba(255, 255, 255, 0.05);
  }

  .back-btn {
    position: absolute;
    color: #666;
    font-size: 42px;
    top: 5%;
    right: 8%;
    z-index: 1;
    cursor: pointer;
  }

  .articleform {
    position: relative;
    width: 90%;
    height: 90%;
    top: 5%;
    left: 5%;

    }

  .article {
    display: flex;
    height: 15%;
    font-family: 'Grape Nuts', cursive;
    text-align: start;
    font-size: 60px;
    align-items: center;
  }
  
  .under-line {
    background-color: white;
    height: 0.5%;
  }

  .title {
    display: flex;
    height: 15%;
    margin-top: 30px ;
  }

  .movie-title {
    width: 34%;
    height: 100%;
    display: flex;
    align-items: center;
  }

  .article-title {
    width: 66%;
    height: 100%;
    display: flex;
    align-items: flex-start;
    flex-direction: column;
    justify-content: center;
  }

  .article-title div {
    font-family: 'Grape Nuts', cursive;
    font-weight: bold;
    font-size: 20px;
    margin-left: 20px ;
  }

  .article-title input {
    height: 40px;
    width: 95%;
    padding: 5px;
    border-radius: 10px;
    border-radius: 10px;
    margin-left: 20px ;
    border: none;
    font-size: 25px;
    font-family: 'Nanum Pen Script', cursive;
    margin-top: 10px;
    padding-left: 10px;
  }

  .article-content{
    height: 60%;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }

  .article-content div {
    margin-top: 30px;
    font-family: 'Grape Nuts', cursive;
    font-weight: bold;
    font-size: 20px;
  }

  .article-content textarea {
    margin-top: 20px;
    width: 100%;
    height: 80%;
    border-radius: 10px;
    outline: none;
    border:none;
    padding: 20px;
  }

  .article-footer {
    height: 9.5%;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  button {
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

  button:hover {
    transform: scale(1.2);
  }


  .select-box {
    position: relative;
    height: 15%;
    width: 100%;
    display: flex;
    align-items: flex-start;
    flex-direction: column;
    justify-content: center;

  }
  
  .select-box form {
    width: 50%;
  }

  select {
    text-align: center;
    height: 40px;
    width: 80%;
    padding: 5px;
    border-radius: 10px;
    border-radius: 10px;
    border: none;
    background-color: rgba(255,255,255,0.8);
    -webkit-appearance: none;
    appearance: none;
    font-size: 25px;
    font-family: 'Nanum Pen Script', cursive;
    margin-top: 10px;
  }

  .select-box div {
    font-family: 'Grape Nuts', cursive;
    font-weight: bold;
    font-size: 20px;
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