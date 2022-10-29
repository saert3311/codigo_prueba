<template>
  <div id="main">
    <NewPostCard  @new_post="modalSwitcher"/>
    <PostBlock v-for="post in posts" :key="post.id" :post="post"/>
    <NewPostModal v-if="show_modal" @hide_modal="modalSwitcher" @reload_posts="getPosts"/>
  </div>
</template>

<script>
import NewPostCard from './components/new-post.vue'
import PostBlock from './components/post.vue'
import NewPostModal from './components/NewPostModal.vue'

export default {
  name: 'index',
  components: {NewPostCard, PostBlock, NewPostModal},
  data(){
    return{
      show_modal:false, //para mostrar efectos y cosas un v-if no nos sirve pero para el momento podemos usarlo
      posts:[]
    }
  },
  methods:{
    modalSwitcher(){
      this.show_modal = !this.show_modal
    },
    getPosts(){
      fetch('http://127.0.0.1:8000/api/v1/post')
      .then(response => response.json())
      .then(data => this.posts = data)
    }
  },
  mounted(){
    this.getPosts();
  }
}
</script>

<style>
/* Extra small devices (phones, 600px and down) */
@media only screen and (max-width: 600px) {
  #main, .modal-content{
    width: 100%;
  }
}

/* Small devices (portrait tablets and large phones, 600px and up) */
@media only screen and (min-width: 600px) {
  #main, .modal-content{
    width: 100%;
  }
}

/* Medium devices (landscape tablets, 768px and up) */
@media only screen and (min-width: 768px) {
  #main{
    width: 680px;
  }
  .modal-content{
    width: 840px;
  }
}
</style>
