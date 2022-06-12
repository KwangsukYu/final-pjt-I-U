<template>
  <div>
    <CommentList />
  </div>
</template>

<script>
// import { mapGetters } from 'vuex'
// import { mapActions } from 'vuex'
import CommentList from '@/components/commentList.vue'

export default {

  name: "TestView",
  components: {
    CommentList
  },
  methods: {
    // ...mapActions([])
  },
  computed: {
    // ...mapGetters(['showResult'])
  }
}
</script>

<style>

</style>