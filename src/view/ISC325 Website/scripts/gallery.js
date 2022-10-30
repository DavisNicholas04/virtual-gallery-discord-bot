var myIndex = 0;
var images = document.getElementsByClassName("myslides");
setInterval(carousel, 2000); // Change image every 2 seconds

function carousel() {
    images[myIndex].style.display = "none";  

    myIndex++;
    if (myIndex >= images.length) {
      myIndex = 0;
    }

    console.log(myIndex, images.length);
    
    images[myIndex].style.display = "block";  
}
