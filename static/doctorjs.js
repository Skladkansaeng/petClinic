new Vue({
  el:"#queue",
  data: {
    firstName:'SETTAKARN',
    lastName:'KLADKANSAENG',
    listQ:[
      { petName:'Memi',
        type:'Cat',
        breed:'pitbull',
        age:'2y6m',
        weight:6,
        heartRate:56,
        restRate:23,
        dehydration:'yes',
        task:'Vaccine' },
      { petName:'Huli',
        type:'Cat',
        breed:'siamese',
        age:'8m',
        weight:8,
        heartRate:96,
        restRate:52,
        dehydration:'no',
        task:'Medical' }
    ],
    dialogFormVisible:false,
    appointment:false,
    medicalForm:{
      symptom:'',
      medicine:'',
      notation:''
    },
    vaccineForm:{
      immunization:'',
      vaccine:'',
      dose:'',
      nextDue:'',
      nextTime:'',
      description:''
    },
    vaccineRec:[{
      givenDate:'',
      age:'',
      immunization:'',
      vaccine:'',
      dose:'',
      nextDue:'',
      vet:''
    }],
    medicalRec: [{
      date:'',
      age:'',
      symptom:'',
      medicine:'',
      notation:'',
      vet:''
    }],
    appointmentForm:{
      date:'',
      time:'',
      description:''
    },
    selectedIndex:0
  },
  methods: {
      openDialog(x) {
        this.selectedIndex = this.listQ.indexOf(x);
        this.dialogFormVisible = true;
        this.appointment = false;
      },
      submit() {
        this.dialogFormVisible = false;
        if (this.appointment) {
          this.appointment = false;
          var date = new Date(this.appointmentForm.date);
          // data to create Appointment
          console.log('Asend'+date.getDate()+'/'+(date.getMonth()+1)+'/'+date.getFullYear(),
          this.appointmentForm.time,this.listQ[this.selectedIndex].petName,this.appointmentForm.description);
          this.appointmentForm.date = '';
          this.appointmentForm.time = '';
          this.appointmentForm.description = '';
        }
        if (this.listQ[this.selectedIndex].task == 'Medical') {
          var today = new Date();
          // data to create MedicalRec
          console.log('MRsend'+today.getDate()+'/'+(today.getMonth()+1)+'/'+today.getFullYear(),
          this.listQ[this.selectedIndex].age,this.medicalForm.symptom,this.medicalForm.medicine,
          this.medicalForm.notation,this.firstName,this.lastName);
          this.medicalForm.symptom = '';
          this.medicalForm.medicine = '';
          this.medicalForm.notation = '';
        }
        else if (this.listQ[this.selectedIndex].task == 'Vaccine') {
          var today = new Date();
          var date = new Date(this.vaccineForm.nextDue);
          // data to create VaccineRec
          console.log('VRsend'+today.getDate()+'/'+(today.getMonth()+1)+'/'+today.getFullYear(),
          this.listQ[this.selectedIndex].age,this.vaccineForm.immunization,this.vaccineForm.vaccine,
          this.vaccineForm.dose,date.getDate()+'/'+(date.getMonth()+1)+'/'+date.getFullYear(),this.firstName,this.lastName);
          console.log('Asend'+date.getDate()+'/'+(date.getMonth()+1)+'/'+date.getFullYear(),this.vaccineForm.nextTime,
          this.listQ[this.selectedIndex].petName,this.vaccineForm.description);
          this.vaccineForm.immunization = '';
          this.vaccineForm.vaccine = '';
          this.vaccineForm.dose = '';
          this.vaccineForm.nextDue = '';
          this.vaccineForm.nextTime = '';
          this.vaccineForm.description = '';
        }
      },
      discard() {
        this.dialogFormVisible = false;
        this.appointment = false;
        this.appointmentForm.date = '';
        this.appointmentForm.time = '';
        this.appointmentForm.description = '';
        this.vaccineForm.immunization = '';
        this.vaccineForm.vaccine = '';
        this.vaccineForm.dose = '';
        this.vaccineForm.nextDue = '';
        this.vaccineForm.nextTime = '';
        this.vaccineForm.description = '';
        this.medicalForm.symptom = '';
        this.medicalForm.medicine = '';
        this.medicalForm.notation = '';
      }
    }
});
