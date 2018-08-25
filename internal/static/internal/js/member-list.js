$('.activation.confirm').click(function (e) {
    e.preventDefault();
    var url = $(this).attr('href');
    $('#delete-form').attr('action', url);
    $(this).find('#activation-modal .delete.button').click(function (e) {
        $('#delete-form').submit();
    });
    $(this).find('#activation-modal').modal('show');
});

let sort_column = 0;
let order = "asc";
let search = "";
let active = "True";

$("#member-search").on("keyup", function (e) {
    search = e.target.value.toLowerCase();
    filter();
});

const menuNav = $('.ui.compact.menu .item');
menuNav.on('click', function (item) {
    menuNav.removeClass('active');
    $(this).addClass('active');
    active = $(this).data("value");
    filter();
});

function filter() {
    $(".member-row").sort(order_rows).each(function () {
        $(this).toggleClass("make-hidden", !$(this).data("search-text").toLowerCase().includes(search) || $(this).data("active") !== active);
    }).appendTo($("#member-table"));
}

function order_rows(row1, row2) {
    const value_row1 = $($(row1).children()[sort_column]).data("sort");
    const value_row2 = $($(row2).children()[sort_column]).data("sort");

    if (order === "asc") {
        return value_row1 > value_row2;
    }
    return value_row2 > value_row1;
}

$(".icon.sort").parent().click(function (e) {
    const selected_column = $(this).parent().children().index($(this));
    if (selected_column === sort_column) {
        if (order === "asc") {
            $(this).find("i").removeClass("down").addClass("up");
            order = "desc"
        } else {
            $(this).find("i").addClass("down").removeClass("up");
            order = "asc"
        }
    } else {
        $($("#table-header").children()[sort_column]).find("i").removeClass("down").removeClass("up");
        sort_column = selected_column;
        order = "asc";
        $(this).find("i").addClass("down")
    }
    filter();
});

filter();

$(".member-property-status-popup-trigger").popup({
    on: "hover"
})