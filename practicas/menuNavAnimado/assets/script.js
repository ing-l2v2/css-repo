const list = document.querySelectorAll(".list");
function enlaceActivo() {
  list.forEach((item) => item.classList.remove("linkActivo"));
  this.classList.add("linkActivo");
}
list.forEach((item) => item.addEventListener("click", enlaceActivo));
