<template>
    <div class="container">
    <h1>Consulta de resultados</h1>

      <!-- Mostrar los detalles del paciente si se encuentra -->
      <div>
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
              <th scope="col">Colesterol Total</th>
              <th scope="col">HDL</th>
              <th scope="col">LDL</th>
              <th scope="col">Triglicéridos</th>
              <th scope="col"> </th>
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
              <td>
                <router-link :to="{ name: 'editar', params: { id: paciente.id } }" class="btn btn-primary">Editar</router-link>
              </td>

            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return { 
        pacienteEncontrado: [],  // Para almacenar los datos del paciente si se encuentra
      };
    },

    created:function(){
        this.ObtenerPaciente()

    },
    
    methods: {
        ObtenerPaciente(){
            console.log(this.$route.params.id)

        fetch('http://localhost:8081/API/?consultar='+this.$route.params.id)
        .then(response=>response.json())
        .then((data) => {
        if(typeof data[0].sucess==='undefined'){
          this.pacienteEncontrado=data
          console.log(data);
        }
        
        else {
          console.log('Paciente no encontrado');
          this.mensajeError = 'Paciente no encontrado';
          this.pacienteEncontrado = null; // Reinicia los datos si no se encuentra el paciente
        }
        })

        .catch((error) => {
        // Manejo de errores
        console.log('Error al buscar el paciente:', error);
        this.mensajeError = 'Error al buscar el paciente.';
      });
        },
    },
  };
  </script>