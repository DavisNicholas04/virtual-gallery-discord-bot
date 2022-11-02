/*//////////////////////////////////////////////////////////
                      FIRST CAROUSEL
//////////////////////////////////////////////////////////*/
let slideIndex = 1;

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

// enables clicking dots on the first carousel
function showSlides(n = (slideIndex + 1)) {
  let i;
  let slides = document.getElementsByClassName("slide");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}

/*//////////////////////////////////////////////////////////
                      SECOND CAROUSEL
//////////////////////////////////////////////////////////*/

let slideIndex2 = 1;
// Thumbnail image controls
function currentSlide2(n) {
  showSlides2(slideIndex2 = n);
}

// enables clicking dots on the second carousel
function showSlides2(n = (slideIndex2 + 1)) {
  let i;
  let slides = document.getElementsByClassName("slide1");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex2 = 1}
  if (n < 1) {slideIndex2 = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex2-1].style.display = "block";
  dots[slideIndex2-1].className += " active";
}

/*//////////////////////////////////////////////////////////
              AUTO CAROUSEL (FIRST AND SECOND)
//////////////////////////////////////////////////////////*/

// initialize starting pictures
document.getElementsByClassName("dot")[0].className += " active";
document.getElementsByClassName("slide")[0].style.display = "block";
document.getElementsByClassName("dot1")[0].className += " active";
document.getElementsByClassName("slide1")[0].style.display = "block";

// automatically rotates first and second carousel images and dots
function carouselAuto() {
  let i;
  let slides = document.getElementsByClassName("slide");
  let dots = document.getElementsByClassName("dot");
  let slides2 = document.getElementsByClassName("slide1");
  let dots2 = document.getElementsByClassName("dot1");

  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndex++;

  for (i = 0; i < slides2.length; i++) {
    slides2[i].style.display = "none";  
  }
  slideIndex2++

  if (slideIndex > slides.length) {slideIndex = 1}    
  if (slideIndex2 > slides2.length) {slideIndex2 = 1}    

  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  for (i = 0; i < dots2.length; i++) {
    dots2[i].className = dots2[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  slides2[slideIndex2-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
  dots2[slideIndex-1].className += " active";
}
setInterval(carouselAuto, 4000); // Change image every 2 seconds
