var images = ['Laugher1.jpg', 'laugherpro.jpg', 'laugherultra.jpg'];
$(function () {
    var i = 0;
    $("#dvImage").css("background-image", "url(/static/images/" + images[i] + ")");
    $("#dvImage").css("background-repeat", "no-repeat");
    $("#dvImage").css("bakground-size", "cover");
    setInterval(function () {
        i++;
        if (i == images.length) {
            i = 0;
        }
        $("#dvImage").fadeOut("slow", function () {
            $(this).css("background-image", "url(/static/images/" + images[i] + ")");
            $(this).fadeIn("slow");
        });
    }, 1000);
});
/*
let images = ['app/static/images/laugher1.jpg','app/static/images/laugherpro.jpg','app/static/images/laugherultra.jpg'];

let index = 0;
const imgElement = document.getElementsByClassName('layer2');

function change() {
    index > 1 ? index = 0 : index++;
   imgElement.src = images[index];
   
   console.log(index);
}

window.onload = function () {
    setInterval(change, 5000);
};*/
/* Landing page */
$( document ).ready(function() {
    var $window = $(window);
    function scroll_elements(){
      var scroll = $window.scrollTop();
      var scrollLayer1 = scroll/1.4;
      var scrollLayer2 = scroll/1.2;
      var scrollLayer3 = scroll/1.2;
      
      $(".layer1").css(
        "-webkit-transform","translate3d(0," +  scrollLayer1  + "px,0)",
                "transform","translate3d(0," +  scrollLayer1  + "px,0)"
      );
      $(".layer2").css(
        "-webkit-transform","translate3d(0," +  scrollLayer2  + "px,0)",
                "transform","translate3d(0," +  scrollLayer2  + "px,0)"
      );
      $(".layer3").css(
        "-webkit-transform","translate3d(0," +  scrollLayer3  + "px,0)",
        "transform","translate3d(0," +  scrollLayer3  + "px,0)"
      );
    }
    
    $window.scroll(scroll_elements);
    });
    
/* Home's header */
const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");

hamburger.addEventListener("click", () => {
  hamburger.classList.toggle("active");
  navMenu.classList.toggle("active");
})

document.querySelectorAll(".nav-link").forEach(n => n.addEventListener("click", () => {
  hamburger.classList.remove("active");
  navMenu.classList.remove("active");
}))

function myFunction() {
  var dots = document.getElementById("dots");
  var moreText = document.getElementById("more");
  var btnText = document.getElementById("myBtn");

  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "Read more"; 
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.innerHTML = "Read less"; 
    moreText.style.display = "inline";
  }
}