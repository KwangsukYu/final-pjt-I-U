<template>
    <div class="box">
      <div class="container">
        <h2>404 Not Found</h2>
        <button @click="back">Back</button>
      </div>
    </div>
</template>


<script>

import { mapActions, mapGetters} from 'vuex'

export default {
  name: "NotFoundView",
  components: {
  },
  methods: {
    ...mapActions(['navToggle']),
    back() {
      this.$router.go(-1)
    },
  },
  computed : {
    ...mapGetters(['navState']),
  },
  created () {
    this.navToggle(false)
  }
}
</script>

<style scoped>

.box {
  top: 25vh;
  position: relative;
}

.container {
  position: relative;
  width: 440px;
  min-height: 400px;
  background: rgba(255, 255, 255, 0.3);
  border-radius: 10px;
  justify-content: center;
  align-items: center;
  backdrop-filter: blur(5px);
  box-shadow: 0 25px 45px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.5);
  border-right: 1px solid rgba(255, 255, 255, 0.2);
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
  animation: animation1 3s;
}

@keyframes animation1 {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

h2 {
  position: absolute;
  top: 30%;
}

button {
  position: absolute;
  background: #fff;
  color: #666;
  cursor: pointer;
  width: 100px;
  margin-bottom: 20px;
  font-weight: 600;
  text-align: center;
  top: 60%;
  width: 50%;
  border: none;
  outline: none;
  padding: 10px 20px;
  border-radius: 35px;
  border: 1px solid rgba(255, 255, 255, 0.5);
  border-right: 1px solid rgba(255, 255, 255, 0.2);
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
  font-size: 16px;
  color: #666;
  box-shadow: 0 5px 15px rgba(255, 255, 255, 0.05);
}

</style>