<template>
  <div class="box">
      <div class="container">
        <div class="form">
          <h2>Login</h2>
          <form @submit.prevent="login(credentials)">
            <div class="inputBox">
              <input type="text" placeholder="Username" v-model="credentials.username">
            </div>
            <div class="inputBox">
              <input type="password" placeholder="Password" v-model="credentials.password">
            </div>
            <div class="inputBox">
              <input type="submit" value="LogIn">
            </div>
            <account-error-list v-if="authError"></account-error-list>
            <p class="forget">Don't have an account ?<router-link to="/signup">Sign-Up</router-link></p>
            <div class="name" @click="backToHome"> U & I</div>
          </form>
        </div>
      </div>
    </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'LoginView',
    components: {
      AccountErrorList
    },
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        }
      }
    },
    methods: {
    ...mapActions(['login', 'navToggle']),
    backToHome() {
      this.$router.replace({ name : "home" })
    },
    moveToSignUp() {
      this.$router.replace({ name : "signup" })
    },
    },
    computed: {
    ...mapGetters(['authError', 'navState'])
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
  width: 400px;
  min-height: 400px;
  background: rgba(255, 255, 255, 0.3);
  border-radius: 10px;
  display: flex;
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

.form{
  position: relative;
  width: 100%;
  height: 100%;
  padding: 40px;
}

.form h2 {
  position: relative;
  color: #666;
  font-size: 24px;
  font-weight: 600;
  letter-spacing: 1px;
  margin-bottom: 40px;
  text-align: start;
}

.form h2::before {
  content: '';
  position: absolute;
  left: 0;
  bottom: -10px;
  width: 80px;
  height: 4px;
  background: #666;
}

.form .inputBox {
  width: 100%;
  margin-top: 20px;
}

.form .inputBox:nth-child(3) {
  display: flex;
  justify-content: flex-start;
}

.form .inputBox input {
  width: 100%;
  background: rgba(255, 255, 255, 0.2);
  border: none;
  outline: none;
  padding: 10px 20px;
  border-radius: 35px;
  border: 1px solid rgba(255, 255, 255, 0.5);
  border-right: 1px solid rgba(255, 255, 255, 0.2);
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
  font-size: 16px;
  letter-spacing: 1px;
  color: #666;
  box-shadow: 0 5px 15px rgba(255, 255, 255, 0.05);
}

.form .inputBox input::placeholder {
  color: #666
}

.form .inputBox input[type="submit"] {
  background: #fff;
  color: #666;
  cursor: pointer;
  width: 100px;
  margin-bottom: 20px;
  font-weight: 600;
}

.name {
  color: rgb(200,200,200);
  font-weight: 600;
  margin-top: 20px;
  font-size: 40px;
}

.forget {
  margin-top: 5px;
  color: #666;
  font-size: 14px;
}

.forget a {
  color: #666;
  font-weight: 600;
  margin-left: 15px;
  font-size: 14px;
}

</style>