var slideIndex = 0;
document.addEventListener('DOMContentLoaded', showSlides, false);

function showSlides() {

  if (!document.getElementById("hacky-slides-timeout")) {
    return;
  }

  var i;
  var slides = document.getElementsByClassName("hacky-slides");
  var timeout = parseInt(document.getElementById("hacky-slides-timeout").innerHTML);
  if (!timeout) {
    timeout = 5000;
  }
  console.log(timeout);
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}
  slides[slideIndex-1].style.display = "block";
  setTimeout(showSlides, timeout);
}
