// variables
var texto = "texto1"; //str
var numero = 2; // int
var arreglo = ["uno","dos", "tres"]; // array
var objeto = {"atributo1":"uno","atributo1":"dos"}; // object
var primero = document.querySelector("#primero"); //guardar estiqueta en una variable
var segundo = document.querySelectorAll(".segundo");
console.log("segundo", segundo);
// funciones

function cambiarColor(){
    segundo[0].style.background = "green";

    if(segundo[1].innerHTML == "Hola3"){
        segundo[1].style.background = "orange";
    }else{
        segundo[1].style.background = "blue";
    }
    
    
}

// eventos

primero.addEventListener("click", cambiarColor);

// condicionales

