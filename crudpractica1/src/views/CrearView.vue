<template>

    <div class="container">
      <h2>Datos personales</h2>

      <form class="row g-3"  >
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
        <label for="inputState" class="form-label">Género</label>
        <select v-model= "paciente.Género" id="inputState" class="form-select" >
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
        <button @click="agregarPaciente" type="submit" class="btn btn-primary">Guardar</button>
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

    methods: {
    agregarPaciente(){
      console.log(this.paciente);
      
      let datosPaciente={
        id:null,
        Doc:this.paciente.Doc,
        Nombre:this.paciente.Nombre,
        Apellido:this.paciente.Apellido,
        Edad:this.paciente.Edad,
        Género:this.paciente.Género,
        EPS:this.paciente.EPS,
        CHOLT:this.paciente.CHOLT,
        HDL:this.paciente.HDL,
        LDL:this.paciente.LDL,
        TRIG:this.paciente.TRIG,

      }

      fetch('http://localhost:8081/API/?insertar=1',{
       method: 'POST',
    body: JSON.stringify(datosPaciente),
    headers: {
        'Content-Type': 'application/json'
    }
})
.then(response => response.text())  // Obteniendo la respuesta en texto primero
.then((data) => {
    console.log("Respuesta del servidor:", data);  // Ver la respuesta cruda
     window.location.href='listar'
    try {
        const jsonResponse = JSON.parse(data);  // Intentar convertir a JSON
        console.log("Respuesta parseada como JSON:", jsonResponse);
    } catch (error) {
        console.error("Error al convertir la respuesta a JSON:", error);
    }
})
.catch(error => {
    console.error("Error en la petición:", error);
});

    }



    }
  
}
</script>
