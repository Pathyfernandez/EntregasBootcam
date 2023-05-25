// Código para cambiar loging a logout//

function loginClicked() {
    var loginButton = document.getElementById("loginButton");

    if (loginButton.innerHTML === "Login") {
        loginButton.innerHTML = "Logout";
    } else {
        loginButton.innerHTML = "Login";
    }
}

// Código que se ejecuta cuando se hace clic en un botón de "likes"
    // button es el botón que se hizo click//
    // Alerta //

function likeButtonClicked(button) {
    console.log('Botón de "likes" clicado');
    console.log('Texto del botón:', button.innerHTML);
    alert("Ninja was liked");
}

// Código que se ejecuta cuando se hace clic en un botón de "addfinition" y desaparece//
function addDefinitionClicked() {
    var addButton = document.getElementById("addDefinitionButton");
    addButton.style.display = "none";
}


