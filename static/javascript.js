function animate_Me(target, moveMe){
    $(target).focus(function(){
        $(moveMe).animate({"marginLeft":"266px"});
      });
    $(target).focusout(function(){
      $(moveMe).animate({"marginLeft":"24px"});
    });
  
  }
  //--------------------
  
  animate_Me("input[type='text']", ".fa-user");
  animate_Me("input[placeholder='Your Last Name']", ".fa-user-plus");
  animate_Me("input[type='email']", ".fa-envelope");
  animate_Me("input[type='password']", ".fa-lock");
  animate_Me("input[placeholder='Confirm Password']", ".fa-refresh");
  
  
  function validardatos(){
    var nombres = document.frmRegistro.nombres; 
    var apellidos = document.frmRegistro.apellidos; 
    var correo = document.frmRegistro.correo;
    var password = document.frmRegistro.password; 
    var password2 = document.frmRegistro.password2;
    if(!nombres.checkValidity()){
        document.frmRegistro.mensaje.value="El usuario debe tener minimo 8 caracteres";
    }else if(!apellidos.checkValidity()){
        document.frmRegistro.mensaje.value="Los apellidos debe tener minimo 8 caracteres";
    }else if(!correo.checkValidity()){
      document.frmRegistro.mensaje.value="El email es un campo requerido";
    }else if(!password.checkValidity()){
        document.frmRegistro.mensaje.value="La contraseña es un campo requerido";            
    }else if(!password2.checkValidity()){
        document.frmRegistro.mensaje.value="La contraseña de confirmación es un campo requerido";
    }else if(password.value!=password2.value){
        document.frmRegistro.mensaje.value="La contraseña y la verificacion deben ser iguales";
    }else if (document.getElementById('estado').unchecked){
        document.frmRegistro.mensaje.value="Para continuar, debes aceptar los términos y condiciones";    
    }else{
        document.frmRegistro.mensaje.value="Puede continuar";
    }
}
function validardatosingreso(){
    var nombre = document.frmRegistro.txtNombre; 
    var passw = document.frmRegistro.txtPw1; 
    
    if(!txtNombre.checkValidity()){
        document.frmRegistro.mensaje.value="Debe ingresar usuario";    
    }else if(!txtPw1.checkValidity()){
        document.frmRegistro.mensaje.value="El password es un campo requerido";                
    }else{
        document.frmRegistro.mensaje.value="Puede continuar";
    }
}
$('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
  })

function guardarEst(){
    document.getElementById("frmRegistro").action="/usuario/guardar";
}