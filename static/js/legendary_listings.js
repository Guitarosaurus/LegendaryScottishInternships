$(document).ready( function() {
    $(".listing").each(
        function(index, item) {
            $(item).children("button.favourite").html(localStorage.getItem($(this).children("p.name").html() + "_is_favourite") === "true" ? "unfavourite":"favourite")
            
        }
    );
    $('.listing').click(
        function() {
            $("#name").html($(this).children("p.name").html());
            $("#company").html($(this).children("div.hidden").children("p.company").html());
            $("#description").html($(this).children("div.hidden").children("p.description").html());
            $("#closedate").html($(this).children("div.hidden").children("p.closedate").html());
            $("#startdate").html($(this).children("div.hidden").children("p.startdate").html());
            $("#enddate").html($(this).children("div.hidden").children("p.enddate").html());
            $("#salary").html($(this).children("div.hidden").children("p.salary").html());
            $("#address").html($(this).children("div.hidden").children("p.address").html());
            $("#checklist").html('<label><input class="checklistbox" type="checkbox"> <p style="display: inline-block">' + $(this).children("div.hidden").children("p.checklist").html().replace(/\n/g, '</p></label></br><label><input class="checklistbox" type="checkbox"> <p style="display: inline-block">') + '</p></label>');
            $(".checklistbox").each(
                function(index, item) {
                    $(item).prop('checked', localStorage.getItem($(item).parent().children("p").html()) === "true");
                }
            );
            console.log($(this).children("div.hidden").children("div.comments").children());
            $("#comments").html($(this).children("div.hidden").children("div.comments").html());
        }
    );
    $('.favourite').click(
        function() {
            if ($(this).html() === "favourite") {
                localStorage.setItem($(this).parent().children("p.name").html() + "_is_favourite", true);
                $(this).html("unfavourite");
            } else {
                localStorage.setItem($(this).parent().children("p.name").html() + "_is_favourite", false);
                $(this).html("favourite");
            }
        }
    );
    $("#checklist").on('change', 'input', function(){ 
        localStorage.setItem($(this).parent().children("p").html(), $(this).is(":checked"));
        console.log(localStorage.getItem($(this).parent().children("p").html()));
    });
    $("#report").click(
        function() {
            $(this).attr("href","../about/" + $("#name").html() + "/" + $("#report_reason").val().replace(/\n/g, '%0A') + "/report");
        }
    );
    $("#post_comment").click(
        function() {
            $(this).attr("href", $("#name").html() + "/" + $("#comment").val() + "/comment");
        }
    );
    let nonFavouritesShown = false;
    $("#hide-non-favourites").click(
        function() {
            if (nonFavouritesShown) {
                $(".listing").each(
                    function(index, item) {
                        $(item).css("display", "block");
                        $("#hide-non-favourites").html("Hide Non-Favourites");
                        nonFavouritesShown = false;
                    }
                );
            } else {
                $(".listing").each(
                    function(index, item) {
                        $(item).css("display", localStorage.getItem($(this).children("p.name").html() + "_is_favourite") === "true" ? "block":"none");
                        $("#hide-non-favourites").html("Show Non-Favourites");
                        nonFavouritesShown = true;
                    }
                );
            }
        }
    );
    $("#filter-button-name").click(
        function() {
            $(".listing").each(
                function(index, item) {
                    let name = $(item).children("p.name").html();
                    $(item).css("display", name.includes($("#filter-name").val()) ? "block" : "none");
                }
            );
        }
    );
    $("#filter-button-company").click(
        function() {
            $(".listing").each(
                function(index, item) {
                    let company = $(item).children("div.hidden").children("p.company").html();
                    $(item).css("display", company.includes($("#filter-company").val()) ? "block" : "none");
                }
            );
        }
    );
    $("#filter-button-location").click(
        function() {
            $(".listing").each(
                function(index, item) {
                    let name = $(item).children("div.hidden").children("p.address").html();
                    $(item).css("display", name.includes($("#filter-location").val()) ? "block" : "none");
                }
            );
        }
    );
});

