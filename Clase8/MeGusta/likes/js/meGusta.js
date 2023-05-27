function agregarLike(elemento){
    //console.log(elemento.querySelector(".numLike"));
    let spanNumLike = elemento.querySelector(".numLike");
    numLike = Number (spanNumLike.textContent);
    numLike +=1;
    spanNumLike.innerText = numLike
}


