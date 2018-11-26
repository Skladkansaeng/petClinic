// Vue.config.delimiters["[[","]]"]

new Vue({
  el:"#userProfile",
  data:{
    // user information
    name:'Warisa',
    surname:'Saisema',
    tel:'0806922292',
    email:'wariffon@gmail.com',
    // show pop-up for edit profile
    dialogFormVisible:false,
    // form edit profile
    form: {
      firstName:'',
      lastName:'',
      telNo:'',
      emailAddr:''
    }
  },
  methods:{
    openDialog() {
      // show pop-up
      this.dialogFormVisible = true;
      // set default value on input bar
      this.form.firstName = this.name;
      this.form.lastName = this.surname;
      this.form.telNo = this.tel;
      this.form.emailAddr = this.email;
    },
    changeProfile() {
      axios
        .get('http://localhost:8000/user/summit')
        .then(response => {
          this.name = response.name
          console.log('great!');
        })
      // save changes
      this.dialogFormVisible = false;
      // this.name = this.form.firstName;
      // this.surname = this.form.lastName;
      // this.tel = this.form.telNo;
      // this.email = this.form.emailAddr;
    }
  },
  delimiters: ['[[', ']]']
});

new Vue({
  el:"#petList",
  data:{
    // list of pet information
    listPet:[
      { petName:'Memi',
        type:'Cat',
        birthDate:'20/10/2000',
        age:'18y1m',
        breed:'unknown',
        sick:'-' },
      { petName:'Huli',
        type:'Cat',
        age:'4y3m',
        birthDate:'5/8/2014',
        breed:'unknown',
        sick:'-' }
    ],
    selectedIndex:0,
    // show pop-up for each pet information, medical record and vaccine record
    petDialogVisible:false,
    allPetDialogVisible:false,
    // show edit form
    editPetInfo:false,
    // form edit name, breed and date of birth of pet
    editPetForm:{
      petName:'',
      breed:'',
      birthDate:''
    },
    // data which showed in medical record table
    medicalRec: [{
      date:'',
      age:'',
      symptom:'',
      medicine:'',
      notation:'',
      vet:''
    }],
    // data which showed in vaccine record table
    vaccineRec:[{
      givenDate:'',
      age:'',
      immunization:'',
      vaccine:'',
      dose:'',
      nextDue:'',
      vet:''
    }]
  },
  methods:{
    openPetDialog(x) {
      // show pop-up
      this.petDialogVisible = true;
      this.editPetInfo = false;
      // x is obj to find which index of pet is selected
      this.selectedIndex = this.listPet.indexOf(x);
    },
    openEditForm() {
      this.editPetInfo = !this.editPetInfo;
      this.editPetForm.petName = this.listPet[this.selectedIndex].petName;
      this.editPetForm.breed = this.listPet[this.selectedIndex].breed;
      var date = this.listPet[this.selectedIndex].birthDate.split("/");
      this.editPetForm.birthDate = new Date(date[2],date[1]-1,date[0]);
    },
    deletePet() {
      console.log(this.selectedIndex,this.listPet[this.selectedIndex].petName);
      // this.listPet.pop(this.selectedIndex);
      // document.getElementById("petList").reload(true); // maybe work with front-back
      this.editPetInfo = false;
      this.petDialogVisible = false;
      // show meg
      this.$message({
        message: 'Pet Deleted',
        type: 'error',
        center: true
      });
    },
    changePetInfo() {
      // close edit form
      this.editPetInfo = false;
      // change information
      this.listPet[this.selectedIndex].petName = this.editPetForm.petName;
      this.listPet[this.selectedIndex].breed = this.editPetForm.breed;
      var date = new Date(this.editPetForm.birthDate);
      this.listPet[this.selectedIndex].birthDate = date.getDate()+'/'+(date.getMonth()+1)+'/'+date.getFullYear();
      this.listPet[this.selectedIndex].age = this.computeAge(this.listPet[this.selectedIndex].birthDate);
      // show meg
      this.$message({
        message: 'Changes Saved',
        type: 'success',
        center: true
      });

    },
    computeAge(bd) {
      var t = bd.split("/");
      var bdate = new Date(t[2],t[1],t[0]);
      var today = new Date();
      var str = '';
      var year = today.getFullYear() - bdate.getFullYear();
      var month = today.getMonth()+1 - bdate.getMonth();
      var day = today.getDate() - bdate.getDate();
      if (month<0 || (month==0 && day<0))  year--;
      if (year==0 && month<5) var week = month*4;
      if (year ==0) {
        if (month<5) str = week+'weeks';
        else str = month+'m';
      }
      else {
        if (month==0) str = year+'y';
        else str = year+'y'+month+'m';
      }
      return str;
    }
  },
  delimiters: ['[[', ']]']
});

new Vue({
  el:"#appointment",
  // data which showed in appointment table
  data:{
    appointmentList:[{
      date:'18/10/2019',
      time:'10:00',
      pet:'Memi',
      description:'check'
    }, {
      date:'18/10/2019',
      time:'14:00',
      pet:'Huli',
      description:'check'
    }]
  },
  delimiters: ['[[', ']]']
});

// send ogj
// var myObj = {
//     building: this.customer[this.selectedIndex].building,
//     room: this.customer[this.selectedIndex].room,
//     firstname: this.customer[this.selectedIndex].customerFirst.firstname,
//     lastname: this.customer[this.selectedIndex].customerFirst.lastname,
//     tel: this.customer[this.selectedIndex].customerFirst.tel,
//     id: this.customer[this.selectedIndex].customerFirst.id
//   };
//   console.log(myObj);
//    axios.post('/yay', myObj).then(res => {
//      console.log(res.data)
//    });

// receive
// axios.get('/yay').then(res => {
//       console.log(res.data)
//       this.customer=res.data
//     })
