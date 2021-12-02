$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
});


$(window).scroll(function () {
    // add 'sticky-header' class to the body tag when the header top is scrolled out of view
    $('#main-navbar').toggleClass('sticky', $(this).scrollTop() > $('.menu-upper').height());
    $('.container').toggleClass('content-sticky', $(this).scrollTop() > $('.menu-upper').height());
});