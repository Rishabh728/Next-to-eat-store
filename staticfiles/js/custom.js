// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();


// isotope js
$(window).on('load', function () {
    $('.filters_menu li').click(function () {
        $('.filters_menu li').removeClass('active');
        $(this).addClass('active');

        var data = $(this).attr('data-filter');
        $grid.isotope({
            filter: data
        })
    });

    var $grid = $(".grid").isotope({
        itemSelector: ".all",
        percentPosition: false,
        masonry: {
            columnWidth: ".all"
        }
    })
});

// nice select
$(document).ready(function() {
    $('select').niceSelect();
  });

/** google_map js **/
function myMap() {
    var mapProp = {
        center: new google.maps.LatLng(40.712775, -74.005973),
        zoom: 18,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}

// client section owl carousel
$(".client_owl-carousel").owlCarousel({
    loop: true,
    margin: 0,
    dots: false,
    nav: true,
    navText: [],
    autoplay: true,
    autoplayHoverPause: true,
    navText: [
        '<i class="fa fa-angle-left" aria-hidden="true"></i>',
        '<i class="fa fa-angle-right" aria-hidden="true"></i>'
    ],
    responsive: {
        0: {
            items: 1
        },
        768: {
            items: 2
        },
        1000: {
            items: 2
        }
    }
});

//feedbackFormSubmit
function feedbackFormSubmit() {
    console.log("first")
    const rating = document.querySelector('input[name="rating"]:checked')?.value;
    const name = document.getElementById('feedbackForm-name').value;
    const email = document.getElementById('feedbackForm-email').value;
    const feedback = document.getElementById('feedbackForm-feedback').value;

    if (!rating || !name || !email || !feedback) {
        alert('Please complete all fields before submitting!');
        return;
    }

    alert(`Thank you, ${name}! Your feedback has been submitted.`);
}


// login Register

function showRegistrationForm() {
    document.getElementById("loginReg-registrationForm").style.display = "block";
    document.getElementById("loginReg-loginForm").style.display = "none";
    document.querySelector('button[onclick="showRegistrationForm()"]').classList.add('loginReg-active-btn');
    document.querySelector('button[onclick="showLoginForm()"]').classList.remove('loginReg-active-btn'); 
}

function showLoginForm() {
    document.getElementById("loginReg-registrationForm").style.display = "none";
    document.getElementById("loginReg-loginForm").style.display = "block";
    document.querySelector('button[onclick="showRegistrationForm()"]').classList.remove('loginReg-active-btn');
    document.querySelector('button[onclick="showLoginForm()"]').classList.add('loginReg-active-btn'); 
}


// Initialize by showing the Registration form initially
showRegistrationForm(); 

// **Note:** This is a simplified example. 
// In a real-world scenario, you would handle form submission 
// using JavaScript (e.g., with AJAX) or a server-side language.

// custom nav scss

const navbarToggler = document.querySelector('.navbar-toggler');
const navbarCollapse = document.querySelector('.navbar-collapse');

// Add click event to toggle the menu
navbarToggler.addEventListener('click', function () {
  const isExpanded = navbarToggler.getAttribute('aria-expanded') === 'true';
  navbarToggler.setAttribute('aria-expanded', !isExpanded);
  navbarCollapse.classList.toggle('show', !isExpanded);
});

// sticky nav bar
  window.onscroll = function() {
    var navbar = document.querySelector('.navbar');
    if (window.scrollY > 10) {
      navbar.classList.add('sticky');
    } else {
      navbar.classList.remove('sticky');
    }
  };


  