new Vue({
  el:"#userProfile",
  data:{
    name:'Warisa',
    surname:'Saisema',
    tel:'0806922292',
    email:'wariffon@gmail.com',
    dialogFormVisible:false,
    form: {
      firstName:'',
      lastName:'',
      telNo:'',
      emailAddr:''
    }
  },
  methods:{
    openDialog() {
      this.dialogFormVisible = true;
      this.form.firstName = this.name;
      this.form.lastName = this.surname;
      this.form.telNo = this.tel;
      this.form.emailAddr = this.email;
    },
    changeProfile() {
      this.dialogFormVisible = false;
      this.name = this.form.firstName;
      this.surname = this.form.lastName;
      this.tel = this.form.telNo;
      this.email = this.form.emailAddr;
    }
  }
});

new Vue({
  el:"#petList",
  data:{
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
      sick:'-' },
      { petName:'Fon',
      type:'Human',
      age:'50y',
      birthDate:'5/8/1999',
      breed:'unknown',
      sick:'-' }
    ],
    selectedIndex:0,
    taskDialogVisible:false,
    editTaskInfo:false,
    vaccine:false,
    medical:false,
    desTask:false,
    openAddPetDialog:false,
    task:{
      petName:'',
      breed:'',
      weight:'',
      heartRate:'',
      restRate:'',
      dehydration:'',
      description:'',
      vet:''
    },
    newPet:{
      petName:'',
      type:'',
      birthDate:'',
      age:'',
      breed:'',
      sick:''
    }
  },
  methods:{
    openTaskDialog(x) {
      this.editTaskInfo = false;
      this.vaccine = false;
      this.medical=false;
      this.desTask = false;
      this.taskDialogVisible = true;
      this.task.dehydration='';
      this.selectedIndex = this.listPet.indexOf(x);
      console.log(this.listPet[this.selectedIndex].petName);
    },
    createTask(){
      this.task.petName = this.listPet[this.selectedIndex].petName;
      this.task.breed = this.listPet[this.selectedIndex].breed;
    },
    resetStatus(){
      this.editTaskInfo = false;
      this.vaccine = false;
      this.medical=false;
      this.desTask = false;
      this.taskDialogVisible = false;
      this.task.dehydration='';
    },
    submitTask(){
      this.resetStatus();

      this.$message({
        message: 'Task Submitted',
        type: 'success',
        center: true
      });
    },
    submitNewPet(){
      this.openAddPetDialog = false;
      this.newPet.age = this.computeAge(this.newPet.birthDate);

      this.$message({
        message: 'New Pet Added',
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
  }
});
