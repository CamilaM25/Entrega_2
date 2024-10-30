<template>

  <div class="container">
    <h1>editar </h1>

    <h2>Datos personales</h2>

    <form v-on:submit.prevent="actualizarPaciente"
    
    class="row g-3"  >

    <div class="col-md-5">
      <label for="inputEmail4" class="form-label">Nombres</label>
      <input v-model= "paciente.Nombre" type="text" class="form-control" id="inputEmail4">
    </div>

    <div class="col-md-5">
      <label for="inputPassword4" class="form-label">Apeliidos</label>
      <input v-model= "paciente.Apellido"  type="text" class="form-control" id="inputPassword4">
    </div>

    <div class="col-md-4">
      <label for="inputAddress" class="form-label">Documento</label>
      <input v-model= "paciente.Doc" type="number" class="form-control" id="inputAddress">
    </div>

    <div class="col-md-2">
      <label for="inputAddress2" class="form-label">Edad</label>
      <input v-model= "paciente.Edad" type="number" class="form-control" id="inputAddress2">
    </div>

    <div class="col-md-2">
      <label for="inputState" class="form-label">Genero</label>
      <select v-model= "paciente.Genero" id="inputState" class="form-select" >
        <option selected disabled>Seleccione...</option>

        <option>F</option>
        <option>M</option>
      </select>
    </div>

    <div class="col-md-2">
      <label for="inputState" class="form-label">EPS</label>
      <select v-model= "paciente.EPS" id="inputState" class="form-select">
        <option selected disabled>Seleccione...</option>
        <option>Sanitas</option>
        <option>SURA</option>
        <option>SUMIMEDICAL</option>
        <option>Coomeva</option>
        <option>SaludVida</option>
        <option>NuevaEPS</option>
        <option>Famisanar</option>
        <option>Cafesalud</option>
        <option>Medimas</option>
        <option>SaludColpatria</option>

      </select>
    </div>
    
<h2>Resultados de exámenes</h2>

    <div class="col-md-3">
      <label for="inputEmail4" class="form-label">CHOLT [mg/dL]</label>
      <input v-model= "paciente.CHOLT" type="number" class="form-control" id="inputEmail4">
    </div>

    <div class="col-md-3">
      <label for="inputPassword4" class="form-label">HDL [mg/dL]</label>
      <input v-model= "paciente.HDL"  type="number" class="form-control" id="inputPassword4">
    </div>

    <div class="col-md-3">
      <label for="inputAddress" class="form-label">LDL [mg/dL]</label>
      <input v-model= "paciente.LDL" type="number" class="form-control" id="inputAddress">
    </div>

    <div class="col-md-3">
      <label for="inputAddress2" class="form-label">TRIG [mg/dL]</label>
      <input v-model= "paciente.TRIG" type="number" class="form-control" id="inputAddress2">
    </div>

</form>

<div class="col-12">
      <button @click="actualizarPaciente" type="submit" class="btn btn-primary">Guardar</button>
    </div>

</div>

</template>

<script>

export default {
data() {
    return { 
      paciente:[],  // Para almacenar los datos del paciente si se encuentra
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
          this.paciente=data
          console.log(data);
        }
        
        else {
          console.log('Paciente no encontrado');
          this.mensajeError = 'Paciente no encontrado';
          this.paciente = null; // Reinicia los datos si no se encuentra el paciente
        }
        })

        .catch((error) => {
        // Manejo de errores
        console.log('Error al buscar el paciente:', error);
        this.mensajeError = 'Error al buscar el paciente.';
      });
    },


  actualizarPaciente(){
    console.log(this.paciente);

    let datosPaciente={
      id:this.$route.params.id,
      Doc:this.paciente.Doc,
      Nombre:this.paciente.Nombre,
      Apellido:this.paciente.Apellido,
      Edad:this.paciente.Edad,
      Genero:this.paciente.Genero,
      EPS:this.paciente.EPS,
      CHOLT:this.paciente.CHOLT,
      HDL:this.paciente.HDL,
      LDL:this.paciente.LDL,
      TRIG:this.paciente.TRIG,

    }

    fetch('http://localhost:8081/API/?actualizar=1',{
      method: 'POST',
      body:JSON.stringify(datosPaciente)
    } )

    .then(response=>response.json())
    .then((data) => {
      console.log(data);
      window.location.href='../listar'
  })

  }



  }

}
</script>
