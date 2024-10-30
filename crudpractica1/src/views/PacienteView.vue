<template>
  <div id="app">
    <h1>Bienvenido</h1>
    <h2>Por favor ingrese su número de documento</h2>
    
    <div class="container">
      <div class="input-group mb-3">
        <span class="input-group-text" id="inputGroup-sizing-default">Documento</span>
        <input 
          v-model="docBuscar" 
          type="text" 
          placeholder="xxxxxxxxx" 
          class="form-control" 
          aria-label="Sizing example input" 
          aria-describedby="inputGroup-sizing-default"
        />
        <button 
          class="btn btn-primary" 
          type="button"
          @click="BuscarPaciente(docBuscar)"
        >
          OK
        </button>
      </div>

      <!-- Mostrar mensaje de error si no se encuentra el paciente -->
      <p v-if="mensajeError" class="text-danger">{{ mensajeError }}</p>

      <!-- Mostrar los detalles del paciente si se encuentra -->
      <div v-if="pacienteEncontrado.length > 0">
        <h2>Datos del Paciente</h2>
        <table class="table table-primary">
          <thead>
            <tr>
              <th scope="col">ID</th>
              <th scope="col">Documento</th>
              <th scope="col">Nombres</th>
              <th scope="col">Apellidos</th>
              <th scope="col">Edad</th>
              <th scope="col">Género</th>
              <th scope="col">EPS</th>
              <th scope="col">Colesterol Total (mg/dL)</th>
              <th scope="col">HDL (mg/dL)</th>
              <th scope="col">LDL (mg/dL)</th>
              <th scope="col">Triglicéridos (mg/dL)</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="paciente in pacienteEncontrado" :key="paciente.id">
              <td>{{ paciente.id }}</td>
              <td>{{ paciente.Doc }}</td>
              <td>{{ paciente.Nombre }}</td>
              <td>{{ paciente.Apellido }}</td>
              <td>{{ paciente.Edad }}</td>
              <td>{{ paciente.Género }}</td>
              <td>{{ paciente.EPS }}</td>
              <td>{{ paciente.CHOLT }}</td>
              <td>{{ paciente.HDL }}</td>
              <td>{{ paciente.LDL }}</td>
              <td>{{ paciente.TRIG }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return { 
      pacienteEncontrado: [],  // Para almacenar los datos del paciente si se encuentra
      docBuscar: '',  // Documento que el usuario ingresa para buscar
      mensajeError: '',  // Mensaje de error en caso de fallo o paciente no encontrado
    };
  },
  
  methods: {
    // Buscar un paciente por documento
    BuscarPaciente(doc) {
      console.log(doc);
      fetch('http://localhost:8081/API/?consultarDoc=' + doc) 
        .then(response => response.json())
        .then((data) => {
          if (data.length > 0) {
            this.pacienteEncontrado = data;
            this.mensajeError = '';  // Limpiar cualquier mensaje de error
          } else {
            this.pacienteEncontrado = [];
            this.mensajeError = 'Paciente no encontrado';
          }
        })
        .catch((error) => {
          console.log('Error al buscar el paciente:', error);
          this.mensajeError = 'Error al buscar el paciente.';
        });
    },
  },
};
</script>

<style>
.container {
  margin-top: 20px;
}
.table-bordered {
  margin-top: 20px;
}
</style>
