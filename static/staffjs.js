new Vue({
  el:"#staff",
  data:{
    firstName:'',
    lastName:'',
  }
});

new Vue({
  el:"#searching",
  data() {
    return {
      links: [],
      state2: '',
      listQ:[],
    };
  },
  methods: {
    querySearch(queryString, cb) {
      if(queryString.length > 1){
      // this.links = this.loadAll(queryString);
      this.links =  this.loadAll(queryString);
      // var results = queryString ? links.filter(this.createFilter(queryString)) : links;
      // console.log(results);
      // call callback function to return suggestions
      cb(this.links);
      }
    },
    createFilter(queryString) {
      return (link) => {
        return (link.value.indexOf(queryString.toLowerCase()) === 0);
      };
    },
    loadAll(queryString) {
      axios({
        method: 'push',
        url: 'getuserInfor',
        data: {
             'str_input':queryString.toLowerCase(),
        },
        xsrfCookieName: 'csrftoken',
        
//  xsrfCookieName: '{{ csrf_token }}',
        xsrfHeaderName: 'X-CSRFToken',
        headers: {
                 'X-Requested-With': 'XMLHttpRequest',
                 'Content-Type': 'application/json //x-www-form-urlencoded; charset=UTF-8'},
        }).then(res => {
          console.log(res.data);
               return this.listQ = res.data;
        });
return this.listQ;
      // return [
      //   { "value": "vae"  ,"link" : "../userInfo"},
      //   { "value": "vue2" },
      //   { "value": "vue3" },
      //   { "value": "vae4" },
      //   { "value": "vue5" },
      //   { "value": "vbe6" },
      //   { "value": "vue7" }
      // ];
    },
    handleSelect(item) {
      console.log(item.link);
      window.location.href = "../userInfo/"+item.link;
      //window.location.href = "userInfo.html";
    }
  },
  mounted() {
    // this.links = this.loadAll();
    // console.log(links);
  }
});

new Vue({
  el:"#newAccount",
  data: {
    form: {
      firstName:'',
      lastName:'',
      email:'',
      tel:'',
      username:'',
      password:'',
      cfPassword:''
    },
    dialogAccount:false,
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
        // { min: 8, message: 'Length should more than 8 Characters', trigger: 'change' },
        { min: 6, pattern: '(?=.*[0-9])(?=.*[A-Za-z])', required: true,
        message: 'Password must be a conbination of at least 6 numbers letters', trigger: 'change' }
      ],
      rePassword: [
        { required: true, message: 'Please Input Password Again', trigger: 'change' },
        // { min: 8, message: 'Length should more than 8 Characters', trigger: 'change' },
        { min: 6, pattern: '(?=.*[0-9])(?=.*[A-Za-z])', required: true,
        message: 'Password must be a conbination of at least 6 numbers letters', trigger: 'change' }
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
                url: '../oak/',
                data: {
                     'firstname':this.form.firstName,
                     'lastname':this.form.lastName,
                     'email':this.form.email,
                     'tel':this.form.tel,
                     'username':this.form.username,
                     'password':this.form.password,
                },
                xsrfCookieName: 'csrftoken',
                xsrfHeaderName: 'X-CSRFToken',
                headers: {
                         'X-Requested-With': 'XMLHttpRequest',
                         'Content-Type': 'application/json //x-www-form-urlencoded; charset=UTF-8'},
                }).then(res => {
                  console.log('aas');
                });
            this.dialogAccount = false;
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
      this.form.firstName = '';
      this.form.lastName = '';
      this.form.email = '';
      this.form.tel = '';
      this.form.username = '';
      this.form.password = '';
      this.form.cfPassword = '';
      this.dialogAccount = false;
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
