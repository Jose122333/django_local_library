$(function () {
    $('.arrow, [class^=arrow-]').bootstrapArrows();

    $('.table td .edit').bind('click',
               function(){
                  $(this).siblings('a').attr('contentEditable',true);
                  $(this).siblings('a').focus();
               });

               $( ".table td a" ).on( "blur", function() {
                 $(this).attr('contentEditable',false);
               });

    $('.table td a,.table td .edit').tooltip();
    //Attach al icon download descargar el doc
    $('.table td img').bind('click',
                        function () {
                          $(this).siblings('a')[0].click();
                        });
  });
