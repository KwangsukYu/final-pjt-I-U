<template>
  <div>
    <CommentListItem v-for="(comment, idx) in commentList" :key="idx" :comment='comment' />
  </div>
</template>

<script>
import CommentListItem from './commentListItem.vue'
import { mapActions, mapGetters} from 'vuex'

export default {
  name: 'commentList',
  data () {
    return {
      articleId : 3
    }
  },
  components: {
    CommentListItem,
  },
  methods: {
    ...mapActions(['getCommentList'])
  },
  computed : {
    ...mapGetters(['commentList'])
  },
  created () {
    this.getCommentList(this.articleId)
  }
}
</script>

<style>

</style>