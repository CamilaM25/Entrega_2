<template>

  <div class="container"> 
    <router-link :to="{ name: 'crear'}" class="btn btn-primary me-2  mb-5">Ingresar nuevo paciente</router-link>

    <div class="input- mb-1">
      <span class="input-group-text"  id="inputGroup-sizing-default">Documento </span>
      <input v-model= "docBuscar" type="text" placeholder="Ingrese el documento" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default">
      <button 
      class="btn btn-primary" 
      type="button"
      id="inputGroup-sizing-default"
      @click="BuscarPaciente(docBuscar)"
      >Buscar</button>
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
            <th scope="col">   </th>

          </tr>
        </thead>
        <tbody>
          <tr v-for="paciente in pacienteEncontrado" :key="paciente.id">
            <td>{{ paciente.id }}</td>
            <td>{{ paciente.Doc }}</td>
            <td>{{ paciente.Nombre }}</td>
            <td>{{ paciente.Apellido }}</td>
          
            <td>
            <div class="btn-group" role="group" aria-label="Button group name">
              <router-link :to="{ name: 'resultados', params: { id: paciente.id } }" class="btn btn-primary">ver resultados</router-link>

              <button
                type="button"
                class="btn btn-danger"
                @click="eliminarPaciente(paciente.id)"

              >
                Eliminar
              </button>
            </div>
            
          </td>



          </tr>
        </tbody>
      </table>
    </div>




    <div class="card"> 
      <div class="card-header">
        <h2>Pacientes registrados</h2>
      </div>
      <div class="card-body">
        <div
          class="table-responsive"
        >
        <table
            class="table table-primary"
          >
            <thead>
              <tr>
                <th scope="col">ID</th>
                <th scope="col">Documento</th>
                <th scope="col">Nombres</th>
                <th scope="col">Apellidos</th>
                <th scope="col">   </th>

              </tr>
            </thead>
            <tbody>
              <tr  v-for="paciente in Pacientes" v-bind:key="paciente.id">
                <td scope="row">{{ paciente.id }}</td>
                <td>{{ paciente.Doc }}</td>
                <td>{{ paciente.Nombre }}</td>        
                <td>{{ paciente.Apellido }}</td>   
                <td>

                  <div class="btn-group" role="group" aria-label="Button group name">
                    <router-link :to="{ name: 'resultados', params: { id: paciente.id } }" class="btn btn-primary">ver resultados</router-link>
                    <button
                      type="button"
                      class="btn btn-danger"
                      @click="eliminarPaciente(paciente.id)"

                    >
                      Eliminar
                    </button>
                  </div>
                    
                  </td>

              </tr>
            </tbody>
          </table>
        </div>
        
      
      </div>
      
    </div>

  </div>
  </template>
  
  <script>

export default {
  data(){
    return{ 
    Pacientes:[],
    pacienteEncontrado:[], // Para almacenar los datos del paciente si se encuentra
    mensajeError: '', // Mensaje de error en caso de fallo o paciente no encontrado
  }
  },
  

    created:function(){
      this.consultarPacientes(); 
    },

    methods:{
      consultarPacientes(){
         fetch('http://localhost:8081/API/')
        .then(response => response.json())
        .then((data)=>{
          console.log(data)
          this.Pacientes=[];
          if(typeof data[0].sucess==='undefined'){
          this.Pacientes=data
        }
        
        })
        .catch(console.log)
      },

      eliminarPaciente(id){
        console.log(id);
        fetch('http://localhost:8081/API/?borrar='+id)
          .then(response=>response.json())
          .then((data)=>{
            console.log(data)
            window.location.href='listar'
        })
        .catch(console.log)
      },

    BuscarPaciente(doc) {
      console.log(doc);
      fetch('http://localhost:8081/API/?consultarDoc='+doc) //se hace uso de la API para consultar un paciente por numero de documento
      .then(response=>response.json())
      .then((data) => {
        if(typeof data[0].sucess==='undefined'){
          this.pacienteEncontrado=data
          this.mensajeError = ''; // Limpiar mensaje de error si el paciente fue encontrado
          console.log(data);
        }
        
        else {
          console.log('Paciente no encontrado');
          this.mensajeError = 'No existe un registro para el documento ingresado. Inténtelo de nuevo';
          this.pacienteEncontrado = null; // Limpiar los datos del paciente si no se encuentra
        
        }
        })

        .catch((error) => {
        // Manejo de errores
        console.log('Error al buscar el paciente:', error);
        this.mensajeError = 'No existe un registro para el documento ingresado. Inténtelo de nuevo';
      });
  }
},

}
</script>
