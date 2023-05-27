function editProfile(element){
    let cardName = document.querySelector(".cardName");
    cardName.innerText = "Pathy Fernandez";
}

function removeUser(element, action) {
    let requestNumber = document.querySelector("#connectionRequestNumber");
    let currentNumber = Number(requestNumber.textContent);
    currentNumber--;
    requestNumber.textContent = currentNumber;
    let user = element.closest(".card-list-item");
    let buttons =element.closest (".buttons");
    buttons.remove();
    let userContent = user.innerHTML;
    user.remove();

    if (action === "add") {
        let myConnection = document.querySelector("#myConnection");
        myConnection.innerHTML += `
            <li class="card-list-item start">
                ${userContent}
            </li>`;
    let totalConnections = document.querySelector("#totalConnections");
    currentNumber = Number(totalConnections.textContent);
    currentNumber ++;
    totalConnections.textContent = currentNumber;
    }
}
