document.getElementById("btn-register").addEventListener("click", login);

function login(){
    const email = document.getElementById("user-email").value;
    const password = document.getElementById("user-password").value;

    if(email === "") {
        alert("Debe de ingresar su correo electrónico")
        //TODO: Completra sweetalert2S
    }

    if(password === "") {
        alert("Debe de ingresar su contraseña")
        //TODO: Completra sweetalert2S
    }

    const data = {
        email: email,
        password: password
    }
    
    fetch('api/login', {
        method:"POST",
        headers: { "Content-Type": "application/json"},
        body: JSON.stringify(data)
    }). then(response => response.json())
    .then(result =>  {
            if(result.success){
                window.location.href = "/welcome";
            } else {
                alert("Sus datos de acceso no son correcots")
                //TODO: Completar con sweet alert
            }
    })
    .catch(error => {
        console.error(error);
    })

}