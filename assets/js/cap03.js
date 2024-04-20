let contador = 1;
const n_js_slide = 3;
const miliseg_slide = 5000;
setInterval(function () {
  document.getElementById("js-radio-" + contador).checked = true;
  contador++;
  if (contador > n_js_slide) {
    contador = 1;
  }
}, miliseg_slide);
