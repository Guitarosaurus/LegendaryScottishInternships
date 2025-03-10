$(document).ready( function() {
    $('.topnav').css("opacity", 0.4);
    $('.topnav').hover(
        function() {
            $(this).animate({ opacity: 1.0 }, 100);
        },
        function() {
            $(this).animate({ opacity: 0.4 }, 100);
        }
    );
});

