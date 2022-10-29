<template>
  <div class="card-wrapper st-1">
    <div class="header">
        <div class="avatar">
                <img src="/user.jpg" alt="user image">
            </div>
            <div class="aside">
                <h4>Pablo de Marcos</h4>
                <span>{{ prettyDate(post.created) }}</span> <vue-feather type="edit" size="14" class="new-post-btn"></vue-feather><span>Publicacion</span>
            </div>
    </div>
    <div class="main-post-show">{{ post.post_text }}</div>
    <div class="separator"></div>
    <div class="reactions"><!-- instale un paquete de iconos ligero no tiene tantos asi que tuve que cambiar algunos para conservar la forma-->
        <button><vue-feather type="thumbs-up" size="16" class="new-post-btn"></vue-feather></button>
        <button><vue-feather type="trending-up" size="16" class="new-post-btn"></vue-feather></button>
        <button><vue-feather type="heart" size="16" class="new-post-btn"></vue-feather></button>
        <button><vue-feather type="user-plus" size="16" class="new-post-btn"></vue-feather></button>
        <button><vue-feather type="printer" size="16" class="new-post-btn"></vue-feather></button>
    </div>
  </div>
</template>

<script>
import moment from "moment"; //el unico
export default {
    name: 'PostBlock',
    props: ['post'],
    methods:{
        prettyDate(string) {
      let date = new Date(string);
      return moment(date).format("DD MMM, HH:mm A");
    },
    }
}
</script>

<style>
    .aside{
        text-align: start;
    }
    .aside h4{
        margin: 0;
        color: #6500bc
    }
    .aside span{
        font-size: 14px;
        color: dimgray;
    }
    .main-post-show{
        text-align: start;
        padding: 0 .7rem;
        margin: .8rem 0
    }
    .separator{
        border-bottom: 1px solid #C0C0C0 ;
        margin: 0 .7rem;
    }
    .reactions button {
        color:#383838
    }
    .reactions{
        display: flex;
        justify-content: space-around;
        margin: .5rem;
    }
</style>