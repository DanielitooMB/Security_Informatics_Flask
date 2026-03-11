document.getElementById("btn-register").addEventListener("click", register);

function register(){
    const password = document.getElementById("user-password").value;
    const repeatpassword = document.getElementById("user-repeat-password").value;

    if(password != repeatpassword) {
        Swal.fire({
        icon: "error",
        title: "Oops...",
        text: "Something went wrong!",
        footer: '<a href="#">Why do I have this issue?</a>'
        });
        return;

        // sweetalert        

    }

    const data = {
        name: document.getElementById("user-name").value,
        email: document.getElementById("user-email").value,
        password: document.getElementById("user-password").value
    }

    fetch('api/users', {
        method:"POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    }).then(response => response.json())
    .then(result => {
        if(result.success){
            alert("Usuario se guardó correctamente")
        }else {
            alert(result.message)
        }
    })
    .catch(error => {
        console.error(error);
    })
}