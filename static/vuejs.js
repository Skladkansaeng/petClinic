new Vue({
  el:"#loginCard",
  data:{
    status:'staff',
    loginForm:{
      username:'',
      password:''
    }
  },
  methods:{
    userLogin:function() {

      axios({
           method: 'post',
           url: 'check/',
           data: {
                'username':this.loginForm.username,
                'password':this.loginForm.password,
           },
           xsrfCookieName: 'csrftoken',
           xsrfHeaderName: 'X-CSRFToken',
           headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'Content-Type': 'application/json //x-www-form-urlencoded; charset=UTF-8'},
           }).then(res => {
                   console.log(res.data['status']);
                   var path = "../"
                   if (res.data['status'] === 'User') {
                       path = path+ "user/"+res.data['pk']
                   }
                   else if (res.data['status'] === 'Doctor') {
                        path = path+ "doctor/"+res.data['pk']
                   }
                   else if (res.data['status'] === 'Staff') {
                        path = path+ "staff/"+res.data['pk']
                   }
                   window.location.href=path;
                   // window.location.href="../";
           });

      console.log("User:",this.loginForm.username,this.loginForm.password);
      this.loginForm.username = '';
      this.loginForm.password = '';
    }
  }
});

var input = document.getElementById("usernameInput");
input.addEventListener("keyup", function(event) {
    event.preventDefault();
    if (event.keyCode === 13) {
        document.getElementById("loginBt").click();
    }
});

var input = document.getElementById("passwordInput");
input.addEventListener("keyup", function(event) {
    event.preventDefault();
    if (event.keyCode === 13) {
        document.getElementById("loginBt").click();
    }
});
