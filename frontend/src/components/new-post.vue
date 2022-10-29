<template>
  <div class="card-wrapper">
    <div class="header">
        <div class="avatar">
            <img src="/user.jpg" alt="user image">
        </div>
        <div class="input">
            <input type="text" class="new-post-input" v-model="new_post" placeholder="Quiero...">
        </div>
    </div>
    <div class="buttons">
        <button  @click="showModal"><vue-feather type="edit" size="16" class="new-post-btn"></vue-feather>publicar</button>
        <button><vue-feather type="award" size="16" class="new-post-btn"></vue-feather>felicitar</button>
        <button><vue-feather type="calendar" size="16" class="new-post-btn"></vue-feather>evento</button>
        <button><vue-feather type="shopping-bag" size="16" class="new-post-btn"></vue-feather>vender</button>
        <button><vue-feather type="headphones" size="16" class="new-post-btn"></vue-feather>asistencia</button>
    </div>
  </div>
</template>

<script>
export default {
    name: 'NewPostCard',
    data(){
        return {
            new_post: ''
        }
    },
    methods:{
        showModal(){
            this.$emit('new_post')
        }
    }
}
</script>

<style>
    .new-post-input {
        border-radius: 3rem;
        border: 1px solid #ced4da;
        padding: .375rem .75rem;
        width: 100%;
        max-width:100%;
        background-color: #DCDCDC;
    }
    .input{
        box-sizing: border-box;
        width:100%;
        display: flex;
    }
    .buttons {
        display: flex;
        justify-content: space-around;
        margin: .4rem 0 .7rem;

    }
    .new-post-btn{
        margin-right: .2rem
    }
    button{box-shadow: rgba(0, 0, 0, 0.15) 1.95px 1.95px 2.6px;}
    button:nth-child(1){color:green}
    button:nth-child(2){color:brown}
    button:nth-child(3){color:red}
    button:nth-child(4){color:blue}
    button:nth-child(5){color:darkgoldenrod}

</style>