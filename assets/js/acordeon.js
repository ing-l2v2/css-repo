/*use strict*/
const t01Bloque = document.querySelectorAll(".t01-bloque");
const t01H2 = document.querySelectorAll(".t01-h2");

/* Cuando se hace click en .t01-h2
  1. Quitar la clase .t01-activo de todos los .t01-bloque
  2. Luego se debe añadir la clase .t01-activo al bloque con la posición del .t01-h2 */

/* Recorriendo TODOS los .t01-h2 */
t01H2.forEach((cadaH2, indiceH2) => {
  /* Asignando un CLICK a cada .t01-h2 */
  t01H2[indiceH2].addEventListener("click", () => {
    /* Recorriendo todos los bloques .t01-bloque */
    t01Bloque.forEach((cadaBloque, indiceBloque) => {
      /* Quitando la clase .t01-activo de todos los bloques */
      t01Bloque[indiceBloque].classList.remove("t01-activo");
    });
    /* Añadir la clase .t01-activo al bloque cuya posición sea igual al del .t01-h2 */
    t01Bloque[indiceH2].classList.add("t01-activo");
  });
});
