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
    $(function() {
        $('.car-sold').click(function(event) {
            event.preventDefault();
            let actionPath = "/manager-dashboard/mark-as-sold/" + $(this).attr('data-car-id');
            let innerId = $(this).attr('data-car-inner-id');
            let make = $(this).attr('data-make');
            let model = $(this).attr('data-model');
            let price = $(this).attr('data-price');
              $('#EditModal form').attr('action', actionPath);
              $('#EditModal .id').text(innerId);
              $('#EditModal .make').text(make);
              $('#EditModal .model').text(model);
              $('#EditModal .price').text(price);
              $('#EditModal').modal('show');
            });
          });
});


$(window).scroll(function () {
    // add 'sticky-header' class to the body tag when the header top is scrolled out of view
    $('#main-navbar').toggleClass('sticky', $(this).scrollTop() > $('.menu-upper').height());
    $('.container').toggleClass('content-sticky', $(this).scrollTop() > $('.menu-upper').height());
    $('h3.flash-message').toUpperCase();
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



