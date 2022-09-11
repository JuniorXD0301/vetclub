import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { NgbDateStruct } from '@ng-bootstrap/ng-bootstrap';
import { Cita } from 'src/app/models/cita';
import { CitaService } from 'src/app/services/cita.service';
@Component({
  selector: 'app-cita',
  templateUrl: './cita.component.html',
  styleUrls: ['./cita.component.css']
})
export class CitaComponent implements OnInit {

  model!: NgbDateStruct;

  constructor(private router: Router, private form:FormsModule, private cita:CitaService) { }

  formCita1 = new FormGroup({
    profesional : new FormControl(''),
    tipo_mascota : new FormControl(''),
    nickname : new FormControl(''),
    tipo_proceso : new FormControl(''),
    fecha : new FormControl(''),
    hora : new FormControl('')
  })

  ngOnInit(): void {
  }

  postform(form: Cita){
    this.cita.agregarCita(form).subscribe(info=>{
      alert('Se a programado la lista con exito')
      console.log(info)
      this.router.navigate([''])
    })
  }

  regresar(){
    this.router.navigate([''])
  }
}
