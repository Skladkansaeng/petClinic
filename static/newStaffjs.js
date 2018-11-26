new Vue({
  el:"#newStaff",
  data: {
      form: {
        firstName:'',
        lastName:'',
        email:'',
        tel:'',
        status:'',
        username:'',
        password:'',
        cfPassword:''
      }
    },
    methods: {
      createAccount() {
          axios({
               method: 'post',
               url: 'created/',
               data: {
                    'firstname':this.form.username,
                    'lastname':this.form.lastName,
                    'tel':this.form.tel,
                    'email':this.form.email,
                    'status':this.form.status,
                    'username':this.form.username,
                    'password':this.form.password,
               },
               xsrfCookieName: 'csrftoken',
               xsrfHeaderName: 'X-CSRFToken',
               headers: {
                        'X-Requested-With': 'XMLHttpRequest',
                        'Content-Type': 'application/json //x-www-form-urlencoded; charset=UTF-8'},
               }).then(res => {
                       window.location.href="../";
               });


        console.log(this.form.firstName,this.form.lastName,this.form.email,this.form.tel,this.form.status);
        this.form.firstName = '';
        this.form.lastName = '';
        this.form.email = '';
        this.form.tel = '';
        this.form.status = '';
        this.username = '',
        this.password = '',
        this.cfPassword = ''
        this.$message({
          message: 'Account Created',
          type: 'success',
          center: true
        });
      },
      discard() {
        axios({
             method: 'get',
             url: '../staff',
             }).then(res => {
                     window.location.href="../staff";
             });
        this.form.firstName = '';
        this.form.lastName = '';
        this.form.email = '';
        this.form.tel = '';
        this.form.status = '';
        this.username = '',
        this.password = '',
        this.cfPassword = ''
        this.$message({
          message: 'Change Discarded',
          type: 'error',
          center: true
        });
      }
    }
});

// var input = document.getElementById("telInput");
// input.addEventListener("keyup", function(event) {
//     event.preventDefault();
//     if (event.keyCode === 13) {
//       document.getElementById("createBt").click();
//     }
// });
