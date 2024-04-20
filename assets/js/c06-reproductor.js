function crea_listeners_reproduccion() {
  maximo = 670; /* Máximo tamaño posible para la barra de progreso en pixeles */
  medio = document.getElementById("medio");
  reproducir = document.getElementById("reproducir");
  barra = document.getElementById("barra");
  progreso = document.getElementById("progreso");

  reproducir.addEventListener("click", presionar, false);
  barra.addEventListener("click", mover, false);
}
/* Funcion que realiza una tarea*/
function presionar() {
  if (!medio.paused && !medio.ended) {
    medio.pause();
    reproducir.innerHTML = "Reproducir";
    window.clearInterval(bucle);
  } else {
    medio.play();
    reproducir.innerHTML = "Pausar";
    bucle = setInterval(estado, 1000);
  }
}
function estado() {
  if (!medio.ended) {
    var total = parseInt((medio.currentTime * maximo) / medio.duration);
    progreso.style.width = total + "px";
    progreso.innerHTML =
      Math.round((medio.currentTime / medio.duration) * 100) + " %";
  } else {
    progreso.style.width = "0px";
    reproducir.innerHTML = "Reproducir";
    window.clearInterval(bucle);
  }
}
function mover(e) {
  if (!medio.paused && !medio.ended) {
    var ratonX = e.pageX - barra.offsetLeft;
    var nuevoTiempo = (ratonX * medio.duration) / maximo;
    medio.currentTime = nuevoTiempo;
    progreso.style.width = ratonX + "px";
  }
}
window.addEventListener("load", crea_listeners_reproduccion, false);

function crea_listeners_formulario() {
  nombre1 = document.getElementById("nombre");
  nombre1 = document.querySelector("#nombre");
  nombre2 = document.getElementById("apellido");
  nombre2 = document.querySelector("#apellido");
  nombre1.addEventListener("input", validacionForm, false);
  nombre2.addEventListener("input", validacionForm, false);
  validacionForm();
}
function validacionForm() {
  if (nombre1.value == "" && nombre2.value == "") {
    nombre1.setCustomValidity("inserte al menos un nombre");
    nombre1.style.background = "#FFDDDD";
  } else {
    nombre1.setCustomValidity("");
    nombre1.style.background = "#FFFFFF";
  }
}
window.addEventListener("load", crea_listeners_formulario, false);

function crea_listeners_canvas() {
  const elemento = document.getElementById("lienzo");
  const lienzo = elemento.getContext("2d");

  lienzo.beginPath();
  lienzo.fillStyle = "#000099";
  lienzo.fillRect(20, 20, 200, 200);
  lienzo.moveTo(220, 220);
  lienzo.lineTo(325, 102);
  lienzo.strokeStyle = "#990000";
  lienzo.strokeRect(225, 100, 240, 120);
  lienzo.stroke();

  /* var gradiente = lienzo.createLinearGradient(0, 0, 10, 100);
  gradiente.addColorStop(0.5, "#0000FF");
  gradiente.addColorStop(1, "#000000");
  lienzo.fillStyle = gradiente;
 */
  /* lienzo.clearRect(120, 120, 80, 80); */
}
window.addEventListener("load", crea_listeners_canvas, false);
