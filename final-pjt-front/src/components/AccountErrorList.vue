<template>
  <div class="account-error-list">
    <div v-for="(errors, field) in authError" :key="field">
      <ul>
        <li v-for="(error, idx) in errors" :key="idx" class="error-li">
          {{ error }}
        </li>
      </ul>
    </div>

  </div>
</template>

<script>
  import { mapGetters } from 'vuex'
  
  export default {
    name: 'AccountErrorList',
    computed: {
      ...mapGetters(['authError'])
    },
  }
</script>

<style>
  .account-error-list {
    color: red;
  }

  .error-li {
    list-style: none;
    text-align: start;
  }
</style>
