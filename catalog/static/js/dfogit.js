$(function () {
    $('.arrow, [class^=arrow-]').bootstrapArrows();

    $('.table td').bind('dblclick',
               function(){
                   $('.table td a').attr('contentEditable',true);
               });

               $( ".table td a" ).on( "blur", function() {
                 $(this).attr('contentEditable',false);
               });
  });
