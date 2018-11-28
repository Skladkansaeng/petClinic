new Vue({
  el:"#newStaff",
  data: {
      form: {
        firstName:'',
        lastName:'',
        email:'',
        tel:'',
        status:'Staff',
        username:'',
        password:'',
        cfPassword:''
      },
        rules: {
          alphaStr: [
            { required: true, message: 'Please Input Information', trigger: 'change' },
            { min: 3, max: 30, message: 'Length should be 3 to 30', trigger: 'change' },
            { pattern: '^[A-Za-z]+$', message: 'Input Must be a Letters', trigger: 'change' }
          ],
          telNo: [
            { required: true, message: 'Please Input Telephone Number', trigger: 'change' },
            { min: 9, max: 10, message: 'Length should be 9 to 10', trigger: 'change' },
            { pattern: '^[0-9]+$', message: 'Input must be a Numbers', trigger: 'change' }
          ],
          emailAddr: [
            { required: true, message: 'Please Input Email', trigger: 'change' },
            { type:'email', message: 'Invalid Email', trigger: 'change' }
          ],
          username: [
            { required: true, message: 'Please Input Username', trigger: 'change' },
            { min: 3, max: 15, message: 'Length should be 3 to 15', trigger: 'change' },
            { pattern: '^[A-Za-z0-9]+$', message: 'Input Must be Letters or Numbers', trigger: 'change' }
          ],
          password: [
            { required: true, message: 'Please Input Password', trigger: 'change' },
            { min: 6, pattern: '(?=.*[0-9])(?=.*[A-Za-z])', required: true,
            message: 'Password must be a conbination of at least 6 numbers letters', trigger: 'change' }
            // { min: 8, message: 'Length should more than 8 Characters', trigger: 'change' },
            // { pattern: '(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])', required: true,
            // message: 'Password must be at least one number, uppercase and lowercase letter', trigger: 'change' }
          ],
          rePassword: [
            { required: true, message: 'Please Input Password Again', trigger: 'change' },
            { min: 6, pattern: '(?=.*[0-9])(?=.*[A-Za-z])', required: true,
            message: 'Password must be a conbination of at least 6 numbers letters', trigger: 'change' }
            // { min: 8, message: 'Length should more than 8 Characters', trigger: 'change' },
            // { pattern: '(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])', required: true,
            // message: 'Password must be at least one number, uppercase and lowercase letter', trigger: 'change' }
          ]
        }
    },
    methods: {
      createAccount() {
          this.$refs.form.validate((valid) => {
            if (valid) {
              if(this.form.password === this.form.cfPassword){
                this.$message({
                  message: 'Account Created',
                  type: 'success',
                  center: true
                });
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
//                           window.location.href="../";
               });
                this.$refs.form.resetFields();
              }
              else {
                this.$message({
                  message: 'Password not Match',
                  type: 'error',
                  center: true
                });
              }
            }
            else {
              this.$message({
                message: 'Invalid Information',
                type: 'error',
                center: true
              });
            }
          });
      },
      discard() {
//        axios({
//             method: 'get',
//             url: '../staff',
//             }).then(res => {
//                     window.location.href="../staff";
//             });
        this.form.firstName = '';
        this.form.lastName = '';
        this.form.email = '';
        this.form.tel = '';
        this.form.status = 'Staff';
        this.form.username = '';
        this.form.password = '';
        this.form.cfPassword = '';
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
