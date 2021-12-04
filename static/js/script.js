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
    $('.container').toggleClass('content-sticky', $(this).scrollTop() > $('.menu-upper').height());
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