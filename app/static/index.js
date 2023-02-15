document.addEventListener("visibilitychange", onVisibilityChange);

function reveal()
  {
    if(document.getElementById('box').checked)
      {document.getElementById("id_password").type='text';}
    else{
      document.getElementById("id_password").type='password';
    }

  }

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

$(function() {
  $(window).scroll(function() {
      var totalHeight, currentScroll, visibleHeight;        
        // How far we've scrolled
      currentScroll = $(document).scrollTop();
        // Height of page
      totalHeight = document.body.offsetHeight;
        // Height visible
      visibleHeight = document.documentElement.clientHeight;
        // If visible + scrolled is greater or equal to total
        //   we're at the bottom
      if (visibleHeight + currentScroll >= totalHeight) {
            // Add to top link if it's not there
          if ($("#toTop").length === 0) {
              var toTop = $("<a>");
              toTop.attr("id", "toTop");
              toTop.attr("href", "#");
              toTop.css("display", "none");
              toTop.html("You're Done! Scroll to Top of Page");
                // Bind scroll to top of page functionality
              toTop.click(function() {
                  $('html, body').animate({scrollTop:0}, 'slow', function() {
                      $("#toTop").remove();
                  });
                  return false;
              });
              $("body").append(toTop);
              $("#toTop").fadeIn(3000);
          }
      }
  });
});

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
  var moreText = document.getElementById("dark");
  var btnText = document.getElementById("myBtn");

  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "Show Dark"; 
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.innerHTML = "Hide Dark"; 
    moreText.style.display = "inline";
  }
}

// login
var current = null;
document.querySelector('#email').addEventListener('focus', function(e) {
  if (current) current.pause();
  current = anime({
    targets: 'path',
    strokeDashoffset: {
      value: 0,
      duration: 700,
      easing: 'easeOutQuart'
    },
    strokeDasharray: {
      value: '240 1386',
      duration: 700,
      easing: 'easeOutQuart'
    }
  });
});
document.querySelector('#password').addEventListener('focus', function(e) {
  if (current) current.pause();
  current = anime({
    targets: 'path',
    strokeDashoffset: {
      value: -336,
      duration: 700,
      easing: 'easeOutQuart'
    },
    strokeDasharray: {
      value: '240 1386',
      duration: 700,
      easing: 'easeOutQuart'
    }
  });
});
document.querySelector('#submit').addEventListener('focus', function(e) {
  if (current) current.pause();
  current = anime({
    targets: 'path',
    strokeDashoffset: {
      value: -730,
      duration: 700,
      easing: 'easeOutQuart'
    },
    strokeDasharray: {
      value: '530 1386',
      duration: 700,
      easing: 'easeOutQuart'
    }
  });
});