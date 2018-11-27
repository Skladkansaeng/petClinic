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
      console.log(item);
      window.location.href = item.link;
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
      tel:''
    },
    dialogAccount:false
  },
  methods: {
    createAccount() {
     
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
                window.location.href="../";
        });


   //console.log(this.form.firstName,this.form.lastName,this.form.email,this.form.tel);
   //this.$refs[formName].resetFields();
   this.dialogAccount = false;
   this.$message({
     message: 'Account Created',
     type: 'success',
     center: true
   });
    },
    discard() {
      this.form.firstName = '';
      this.form.lastName = '';
      this.form.email = '';
      this.form.tel = '';
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
