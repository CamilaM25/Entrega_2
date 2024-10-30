<template>
  <div class="container mt-5">
    <div id="app">
      <h1>BIENVENIDO AL SISTEMA DE ESPECIALISTA</h1>
      <label for="clave">Ingrese la clave  </label>
      <input
        type="password"
        v-model="clave"
        placeholder="Clave"
        id="clave"
      />
    </div>

    <button
      class="btn btn-primary"
      @click="verificarCodigo"
    >
      OK
    </button>

    <div v-if="mensaje" class="mt-3 alert">
      {{ mensaje }}
    </div>
  </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        clave: '',      // Valor ingresado por el usuario
        mensaje: '',    // Mensaje para mostrar después de presionar OK
        claveCorrecta: '1234',  // Clave predeterminada
      };
    },
    methods: {
  verificarCodigo() { 
    if (this.clave === this.claveCorrecta) {
      this.$router.push('/listar');
    } else {
      this.mensaje = 'Clave incorrecta. Inténtalo de nuevo.';
      this.clave = ''; // Limpia el campo de entrada cuando la clave es incorrecta
    }
  },
},
};
  </script>
  