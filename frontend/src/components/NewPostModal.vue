<template>
  <div id="newPostModal" class="modal">
    <div class="modal-content">
      <div class="modal-header">
        <span class="close" @click="hideModal">&times;</span>
        <h5>
          <vue-feather type="edit" size="16" class="new-post-btn"></vue-feather>
          Publicar
        </h5>
      </div>
      <div class="modal-body">
        <h5 class="text-start">Tipo de publicacion</h5>
        <div class="button-group">
          <!-- esto tal vez se pueda parametrizar por si cambian los tipos de publicaciones o algo asi-->
          <button
            class="is-black"
            :class="{ activated: active.publicacion }"
            @click="changeOption('publicacion')"
          >
            <vue-feather
              type="edit"
              size="16"
              class="new-post-btn"
            ></vue-feather
            >Publicacion
          </button>
          <button
            class="is-black"
            :class="{ activated: active.anuncio }"
            @click="changeOption('anuncio')"
          >
            <vue-feather
              type="award"
              size="16"
              class="new-post-btn"
            ></vue-feather
            >Anuncio Oficial
          </button>
          <button
            class="is-black"
            :class="{ activated: active.ofrecer }"
            @click="changeOption('ofercer')"
          >
            <vue-feather
              type="calendar"
              size="16"
              class="new-post-btn"
            ></vue-feather
            >Ofrecer Ayuda
          </button>
          <button
            class="is-black"
            :class="{ activated: active.objeto }"
            @click="changeOption('objeto')"
          >
            <vue-feather
              type="shopping-bag"
              size="16"
              class="new-post-btn"
            ></vue-feather
            >Objeto Perdido
          </button>
          <button
            class="is-black"
            :class="{ activated: active.encuesta }"
            @click="changeOption('encuesta')"
          >
            <vue-feather
              type="headphones"
              size="16"
              class="new-post-btn"
            ></vue-feather
            >Encuesta
          </button>
        </div>
        <h5 class="text-start">Mensaje</h5>
        <div class="message-block input">
          <textarea
            id="message-input"
            name="message-input"
            rows="2"
            v-model="message"
          ></textarea>
        </div>
      </div>
      <div class="modal-footer">
        <button class="send-button is-black" @click="send_intent">
          Enviar
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "NewPostModal",
  data() {
    return {
      message: "",
      type: "publicacion",
      active: {
        publicacion: true,
        anuncio: false,
        ofrecer: false,
        objeto: false,
        encuesta: false,
      },
    };
  },
  methods: {
    hideModal() {
      this.$emit("hide_modal");
    },
    changeOption(option) {
      // un metodo rudimentario de checkbox
      for (let item in this.active) {
        this.active[item] = false;
      }
      this.active[option] = true;
      this.type = option;
    },
    send_intent() {
      if (this.message) {
        if(this.type!="publicacion") this.$emit("hide_modal") //metodo rustico para ocultar si no es publicacion
        this.process_send() //lo apartamos como es async
      } else {
        alert("El post no puede estar vacio"); //se puede mejorar muchisimo pero es mejor tener algun feedback que ninguno para el usuario
      }
    },
    process_send() {
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ post_text: this.message, post_type: this.type  }),
      };
      fetch("http://127.0.0.1:8000/api/v1/post/",requestOptions)
      .then(response => {
        if (response.status != 201){
          alert('Ocurrio un error')
        }
        this.hideModal() // se puede meter una mejor confirmacion al usuario
        this.$emit('reload_posts')
      })
    },
  },
};
</script>

<style>
/* The Modal (background) */
.modal {
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  left: 0;
  top: 0;
  width: 100vw; /* Full width */
  height: 100vh; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgb(0, 0, 0); /* Fallback color */
  background-color: rgba(0, 0, 0, 0.4); /* Black w/ opacity */
  display: flex;
  place-items: center;
}

.modal-header {
  padding: 2px 18px;
  background-color: #6500bc;
  color: white;
  text-align: start;
}
.modal-header h5 {
  margin: 0.6rem 0;
}

.modal-body {
  padding: 2px 16px;
}

.modal-content {
  position: relative;
  background-color: #fefefe;
  margin: auto;
  padding: 0;
  border: 1px solid #888;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}

/* The Close Button */
.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
  margin-top: 0.6rem;
}

.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}
.modal-body h5 {
  margin: 0.5rem 0;
}
.button-group button {
  border-radius: 0;
  border: 1px solid #bebebe;
}
.button-group button:first-child {
  border-top-left-radius: 8px;
  border-bottom-left-radius: 8px;
}
.button-group button:last-child {
  border-top-right-radius: 8px;
  border-bottom-right-radius: 8px;
}
.button-group button:not(:first-child) {
  /* para que no queden bordes de 2px entre botones */
  margin-left: -1px;
}

.message-block {
  margin-top: 0.5rem;
}
.message-block textarea {
  width: 100%;
  border-radius: 0.5rem;
  border: 1px solid #ced4da;
  padding: 0.375rem 0.75rem;
  width: 100%;
  max-width: 100%;
  font-size: 1rem;
  font-family: Inter, Avenir, Helvetica, Arial, sans-serif;
}
.msj-title {
  margin: 0;
}
.modal-footer {
  display: flex;
  justify-content: end;
  margin: 0.5rem 1rem;
}
</style>