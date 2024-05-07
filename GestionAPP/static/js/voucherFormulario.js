/*

*/
if (document.readyState === "complete") {
    var btnesCerrar = document.getElementsByClassName("close");
    var excursiones = document.getElementsByClassName("excursion");
    for (var boton of btnesCerrar){
        boton.onclick = function(){
            alert("hola")
        }
    }
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
    
  });
}
