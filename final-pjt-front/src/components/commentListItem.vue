<template>
  <div class="comment-item">
      {{ comment.content}}
        <div class="del-btn"> <i class="fa-solid fa-xmark"></i></div>
        <div class="comment-user">
      {{ comment.user.username }}
      {{ isAuthor }}
      {{ currentUser.username }}
      <div v-if=" comment.user.username  ===  currentUser.username ">dfadsfads</div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name:"commentListItem",
  props: {
    comment : Object,
  },
  methods:{
    // ...mapActions([])
  },
  computed:{
    ...mapGetters(['currentUser']),
    isAuthor () {
      return this.comment.username === this.currentUser.username
    },

  },
}
</script>

<style scoped>
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
    font-size: 14px;
    padding: 10px ;
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

</style>