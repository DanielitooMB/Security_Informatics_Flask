document.getElementById("btn-register").addEventListener("click", register);

function register(){
    password = document.getElementById("user-password").value;
    repeatpassword = document.getElementById("user-repeat-password").value;

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

}