function showPassword() {
    $('#togglePassword').on('click', function() {
      var passwordField = $('#id_password1');
      var type = passwordField.attr('type') === 'password' ? 'text' : 'password';
      passwordField.attr('type', type);
  
      $(this).toggleClass('bi bi-eye-slash-fill'); 
      $(this).toggleClass('bi bi-eye-fill'); 
    });
  };
  
  function showPassword2() {
    $('#togglePassword2').on('click', function() {
      var passwordField = $('#id_password2');
      var type = passwordField.attr('type') === 'password' ? 'text' : 'password';
      passwordField.attr('type', type);
  
      $(this).toggleClass('bi bi-eye-slash-fill'); 
      $(this).toggleClass('bi bi-eye-fill'); 
      
    });
  };

  function showPasswordLogin() {
    $('#togglePasswordLogin').on('click', function() {
      var passwordField = $('#id_password');
      var type = passwordField.attr('type') === 'password' ? 'text' : 'password';
      passwordField.attr('type', type);
  
      // Toggle Bootstrap icon class based on password visibility
      $(this).toggleClass('bi bi-eye-slash-fill');
      $(this).toggleClass('bi bi-eye-fill');
    });
  };