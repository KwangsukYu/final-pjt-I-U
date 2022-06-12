<template>
  <div id="app">
    <NavigationBar/>
    <router-view class="router-view"/>
  </div>
</template>

<script>
import NavigationBar from '@/components/navigationBar.vue'
// import { mapActions } from 'vuex'
import { mapGetters } from 'vuex'

export default {
  name: 'App',
  components: {
    NavigationBar
  },
  methods: {
    // ...mapActions[('fetchCurrentUser')]
  },
  computed: {
    ...mapGetters[('currentUser')]
  },
}
</script>

<style>
* {
  font-family: 'Roboto Mono', monospace;
}

.swal-overlay {
  background-color: rgba(0, 0, 0, 0.4);
}

.swal-modal {
  background-color: white;
}

.swal-button {
  border-radius: 10px;
  background-color: white;
  border: 1px solid white;
  text-shadow: 0px -1px 0px rgba(0, 0, 0, 0.3);
  color: #666;
}

#app{
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100vh;
  width: 100vw;
}

body {
  background-image: url("./assets/back-ground.png");
  /* background-image: url("./assets/back-ground-black.png"); */
  background-size: cover;
  backdrop-filter: blur(10px); 
  /* font-family: 'Jua', sans-serif; */
  font-family: 'Dongle', Arial;
  height: 100vh;
}


</style>

