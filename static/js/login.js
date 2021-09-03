(function() {
    var ref;
  
    window.login = (ref = window.login) != null ? ref : {};
  
    login.init = function() {  
      $("#btn_submit").click(function(event) {
        var login_data;
        event.preventDefault();
        login_data = {
          username: $("#username").val(),
          password: $("#password").val()
        };
        if (!login_data.username || !login_data.password) {
          alert("Username & Password Shouldn't Empty");
          return false;
        }
        console.log(login_data)
        $.ajax({
          type: "POST",
          url: "/api/login/",
          data: JSON.stringify(login_data),
          contentType: "application/json"
        }).then(function(response) {
          console.log('ress', response);
          Cookies.set('token', response['token']);
          localStorage.setItem('token', response['token']);
          localStorage.setItem('username', response['username']);
          localStorage.setItem('email', response['email']);
          return window.location.reload(true);
        });
        return false;
      });

      $("#btn_submit_reg").click(function(event) {
        console.log('eve', event)
        register_data = {
          username: $("#username").val(),
          password1: $("#password").val()
        };
        register_data['email'] = register_data['username'] + "@mail.com";
        register_data['password2'] = register_data['password1'];
        if (!register_data.username || !register_data.password1) {
          alert("Username & Password Shouldn't Empty");
          return false;
        }
        let do_reg = confirm("Are you sure you want to Register? " + register_data['username']);
        if (!do_reg) { return false }
        console.log('register_data', register_data);
        $.ajax({
          type: "POST",
          url: "/api/register/",
          data: JSON.stringify(register_data),
          contentType: "application/json"
        }).then(function(response) {
        //   console.log('ress', response);
          alert("Dear " + response["username"] + " Registeration Succesful! Please Login!")
          return window.location.reload(true);
        });
        return false;
      });
      return true;
    };
  
    $(function() {
      $(document).ajaxError(function(event, jqxhr, settings, thrownError) {
        var server_msg;
        server_msg = "";
        _.each(jqxhr.responseJSON, function(value, key) {
          return server_msg += value.join('<br/>');
        });
        alert(server_msg);
        return true;
      });
      return true;
    });
  
  }).call(this);