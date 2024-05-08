/*

*/
if (document.readyState === "complete") {
 
  // Fully loaded!
} else if (document.readyState === "interactive") {
  // DOM ready! Images, frames, and other subresources are still downloading.
} else {
  // Loading still in progress.
  // To wait for it to complete, add "DOMContentLoaded" or "load" listeners.

  window.addEventListener("DOMContentLoaded", () => {
    // DOM ready! Images, frames, and other subresources are still downloading.
  });

  window.addEventListener("load", () => {
    // Fully loaded!
    var tituloHead = document.getElementById("tituloHead");
    tituloHead.innerHTML = "Vouchers";
    var iconHead = document.getElementById("iconHead");
    iconHead.innerHTML = "post_add";
    var btnesCerrar = document.getElementsByClassName("btnCerrar");
    var excursiones = document.getElementsByClassName("excursion_single");
    
    // Verificar si el número de botones y divs coincide
    if (btnesCerrar.length === excursiones.length) {
      // Iterar sobre los botones y agregar controladores de eventos
      for (var i = 0; i < btnesCerrar.length; i++) {
        (function (i) {
          btnesCerrar[i].addEventListener("click", function () {
            // Ocultar la excursión correspondiente al botón
            excursiones[i].style.display = excursiones[i].style.display === "none" ? "block" : "none";
          });
        })(i);
      }
    } else {
      console.error("La cantidad de botones y excursiones no coincide");
    }
  });
}
