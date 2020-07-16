/*
------------------------
    Print the Persona
------------------------
 */
$("#print-btn").on("click", function () {
     window.print();
});

/*
------------------------
    Tooltip activation
------------------------
 */

$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})