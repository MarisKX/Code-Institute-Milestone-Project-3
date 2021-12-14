$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $("select").formSelect();
    $('.datepicker').datepicker({
        format: "dd-mm-yyyy",
        showClearBtn: true,
        maxDate: new Date(),
        i18n: {
            done: "Select"
        }});
});


$(window).scroll(function () {
    // add 'sticky-header' class to the body tag when the header top is scrolled out of view
    $('#main-navbar').toggleClass('sticky', $(this).scrollTop() > $('.menu-upper').height());
    $('.content').toggleClass('content-sticky', $(this).scrollTop() > $('.menu-upper').height());
});

function apkTrigger() {
    if ($("#apk-init").is(":checked")){
        $("#apk").attr("required", true);
        $("#apk-trigger").removeClass("hidden");
    } else {
        $("#apk").attr("required", false);
        $("#apk-trigger").addClass("hidden");
    }
}

function showAccount() {
    $(".access-rights").removeClass("hidden");
    $(".change-password").addClass("hidden");
    $(".users").addClass("hidden");
}

function showPassword() {
    $(".access-rights").addClass("hidden");
    $(".change-password").removeClass("hidden");
    $(".users").addClass("hidden");
}

function showUsers() {
    $(".access-rights").addClass("hidden");
    $(".change-password").addClass("hidden");
    $(".users").removeClass("hidden");
}

// Switches between sections in cars for sale according to their status

function showAllCars() {
    $(".all-cars").removeClass("hidden");
    $(".cars-in-stock").addClass("hidden");
    $(".sold-cars").addClass("hidden");
    $(".archive").addClass("hidden");
}

function carsInStock() {
    $(".all-cars").addClass("hidden");
    $(".cars-in-stock").removeClass("hidden");
    $(".sold-cars").addClass("hidden");
    $(".archive").addClass("hidden");
}

function soldCars() {
    $(".all-cars").addClass("hidden");
    $(".cars-in-stock").addClass("hidden");
    $(".sold-cars").removeClass("hidden");
    $(".archive").addClass("hidden");
}

function archivedCars() {
    $(".all-cars").addClass("hidden");
    $(".cars-in-stock").addClass("hidden");
    $(".sold-cars").addClass("hidden");
    $(".archive").removeClass("hidden");
}

// Switches between sections in rental cars according to their status

function showUnavailableRentalCars() {
    $(".unavailable-rental-cars").removeClass("hidden");
    $(".rental-cars").addClass("hidden");
    $(".rental-cars-archive").addClass("hidden");
}

function carsAvailableForRent() {
    $(".unavailable-rental-cars").addClass("hidden");
    $(".rental-cars").removeClass("hidden");
    $(".rental-cars-archive").addClass("hidden");
}

function archivedRentalCars() {
    $(".unavailable-rental-cars").addClass("hidden");
    $(".rental-cars").addClass("hidden");
    $(".rental-cars-archive").removeClass("hidden");
}

function archivedRentalCars() {
    $(".unavailable-rental-cars").addClass("hidden");
    $(".rental-cars").addClass("hidden");
    $(".rental-cars-archive").removeClass("hidden");
}

function initMap() {
    var map = new google.maps.Map(document.getElementById("map"), {
      zoom: 14,
      center: {
        lat: 51.574734,
        lng: 5.099945
      }
    });
    var labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    var locations = [
      {lat: 51.574534, lng: 5.080644},
      {lat: 51.578754, lng: 5.118803},
      {lat: 51.578564, lng: 5.084015}
    ];
    var markers = locations.map(function(location, i) {
      return new google.maps.Marker({
        position: location,
        label: labels[i % labels.length]
      });
    });
    var markerCluster = new MarkerClusterer(map, markers,
    {imagePath: "https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m"});
  }


