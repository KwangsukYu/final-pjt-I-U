<template>
    <form @submit.prevent="getSearchResult(query)" class="fadein">
      <span>Find your pleasure!</span>
      <div class="input">
        <input type="text" v-model="query" placeholder="Search Movie...">
      </div>
      <button>Search</button>
    </form>
</template>

<script>
import { mapActions } from 'vuex'


export default {
  name: "SearchBar",
  data () {
    return {
      query : '',
    }
  },
  methods: {
    ...mapActions(['getSearchResult']),
  }
}
</script>

<style scoped>
  form {
    min-width: 350px;
    position: absolute;
    top: 120px;
    right: 300px;
    height: 5vh;
    z-index: 1;
  }
  
  .input {
    height: 40px;
    position: relative;
    border: none;
    border-radius: 10px;
    background-color: rgba(0,0,0,0.3);
    backdrop-filter: blur(5px);
    border-radius: 35px;
    border: 1px solid rgba(255, 255, 255, 0.5);
    border-right: 1px solid rgba(255, 255, 255, 0.2);
    border-bottom: 1px solid rgba(255, 255, 255, 0.2);
    font-size: 16px;
    color: #666;
    box-shadow: 0 5px 15px rgba(255, 255, 255, 0.05);
    padding: 10px 20px;
    width: 315px;
    bottom: 8px
  }

  button {
    position: absolute;
    top: -2px;
    right: 45px;
    border-radius: 10px;
    background-color: white;
    backdrop-filter: blur(5px);
    border-radius: 35px;
    border: 1px solid rgba(255, 255, 255, 0.5);
    border-right: 1px solid rgba(255, 255, 255, 0.2);
    border-bottom: 1px solid rgba(255, 255, 255, 0.2);
    font-size: 16px;
    color: #666;
    box-shadow: 0 5px 15px rgba(255, 255, 255, 0.05);
    min-width: 80px;
  }

  span {
    position: absolute;
    left: -200px;
  }

  input {
    position: relative;
    left: -40px;
    top: 0;
    height: 100%;
    width: 70%;
    padding: 0;
    margin: 0;
    border: none;
    background: transparent;
    box-shadow: none;
    outline: none;
    color: white;
  }

  input:focus::placeholder {
    color: transparent;
  }

  .form .inputBox input::placeholder {
  color: #666
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