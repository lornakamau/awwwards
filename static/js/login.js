$('#signup').click(function() {
    $('.pinkbox').css('transform', 'translateX(80%)');
    $('.signin').addClass('nodisplay');
    $('.signup').removeClass('nodisplay');
  });
  
  $('#signin').click(function() {
    $('.pinkbox').css('transform', 'translateX(0%)');
    $('.signup').addClass('nodisplay');
    $('.signin').removeClass('nodisplay');
  });

  $(document).ready(function(){
    $('.signupbox').css('transform', 'translateX(80%)');
    $('.signinbox').css('transform', 'translateX(0%)');
  });