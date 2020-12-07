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
    var nombre = document.frmRegistro.txtNombre; 
    var apellido = document.frmRegistro.txtApellido; 
    var email = document.frmRegistro.txtEma; 
    var email2 = document.frmRegistro.txtEma2; 
    var passw = document.frmRegistro.txtPw1; 
    var passw2 = document.frmRegistro.txtPw2;
    if(!txtUsr.checkValidity()){
        document.frmRegistro.mensaje.value="El usuario debe tener minimo 8 caracteres";
    }else if(!txtEma.checkValidity()){
        document.frmRegistro.mensaje.value="El email es un campo requerido";
    }else if(!txtEma1.checkValidity()){
      document.frmRegistro.mensaje.value="El email de confirmación un campo requerido";
    }else if(txtEma.value!=txtEma2.value){
        document.frmRegistro.mensaje.value="El correo debe igual";
    }else if(!txtPw1.checkValidity()){
        document.frmRegistro.mensaje.value="El password es un campo requerido";            
    }else if(!txtPw2.checkValidity()){
        document.frmRegistro.mensaje.value="La contraseña de confirmación es un campo requerido";
    }else if(txtPw1.value!=txtPw2.value){
        document.frmRegistro.mensaje.value="La clave y la verificacion deben ser iguales";
    }else if (document.getElementById('checkbox1').unchecked){
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