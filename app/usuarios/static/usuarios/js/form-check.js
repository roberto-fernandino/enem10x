$(document).ready(function(){
    $('input[required]').on('blur', function(){
      if ($(this).val() === ''){
        $(this).css('border', '3px solid red');
      }else{
        $(this).css('border', '')
      }
    })
  })