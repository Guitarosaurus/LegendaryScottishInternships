$(document).ready( function() {
    $('.show').click(
        function() {
            // $(this).children(".name").html($(this).children("p.name").html());
            if ($(this).parent().children("div.hidden").children("p.shown").html() === "false") {
                $(this).parent().children(".company").html($(this).parent().children("div.hidden").children("p.company").html());
                $(this).parent().children(".description").html($(this).parent().children("div.hidden").children("p.description").html());
                $(this).parent().children(".closedate").html($(this).parent().children("div.hidden").children("p.closedate").html());
                $(this).parent().children(".startdate").html($(this).parent().children("div.hidden").children("p.startdate").html());
                $(this).parent().children(".enddate").html($(this).parent().children("div.hidden").children("p.enddate").html());
                $(this).parent().children(".salary").html($(this).parent().children("div.hidden").children("p.salary").html());
                $(this).parent().children(".address").html($(this).parent().children("div.hidden").children("p.address").html());
                $(this).parent().children(".checklist").html('<label><input class="checklistbox" type="checkbox"> <p style="display: inline-block">' + $(this).parent().children("div.hidden").children("p.checklist").html().replace(/\n/g, '</p></label></br><label><input class="checklistbox" type="checkbox"> <p style="display: inline-block">') + '</p></label>');
                $(".checklistbox").each(
                    function(index, item) {
                        $(item).prop('checked', localStorage.getItem("Legendary::" + $(this).parent().parent().children(".name").html() + "::" + $(this).parent().children("p").html(), $(this).is(":checked")) === "true");
                    }
                );
                $(this).parent().children("div.hidden").children("p.shown").html("true");
            } else {
                $(this).parent().children(".company").html("");
                $(this).parent().children(".description").html("");
                $(this).parent().children(".closedate").html("");
                $(this).parent().children(".startdate").html("");
                $(this).parent().children(".enddate").html("");
                $(this).parent().children(".salary").html("");
                $(this).parent().children(".address").html("");
                $(this).parent().children(".checklist").html("");
                $(this).parent().children("div.hidden").children("p.shown").html("false");
            }
        }
    );

    $(".listing").each(
        function(index, item) {
            $(item).css("display", localStorage.getItem("Legendary::" + $(this).children("p.name").html() + "_is_favourite") === "true" ? "block":"none")
            
        }
    );
    
    $(".checklist").on('change', 'input', function(){ 
        localStorage.setItem("Legendary::" + $(this).parent().parent().children(".name").html() + "::" + $(this).parent().children("p").html(), $(this).is(":checked"));
    });
});
