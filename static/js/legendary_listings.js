$(document).ready( function() {
    $('.listing').click(
        function() {
            $("#name").html($(this).children("p.name").html());
            $("#description").html($(this).children("div.hidden").children("p.description").html());
            $("#closedate").html($(this).children("div.hidden").children("p.closedate").html());
            $("#startdate").html($(this).children("div.hidden").children("p.startdate").html());
            $("#enddate").html($(this).children("div.hidden").children("p.enddate").html());
            $("#salary").html($(this).children("div.hidden").children("p.salary").html());
            $("#address").html($(this).children("div.hidden").children("p.address").html());
            $("#checklist").html($(this).children("div.hidden").children("p.checklist").html());
        }
    );
});

