import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, FormsModule } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { Cita } from 'src/app/models/cita';
import { CitaService } from 'src/app/services/cita.service';

@Component({
  selector: 'app-editar-programada',
  templateUrl: './editar-programada.component.html',
  styleUrls: ['./editar-programada.component.css']
})
export class EditarProgramadaComponent implements OnInit {

  constructor(private activeroute:ActivatedRoute, private router:Router, private form:FormsModule, private cita:CitaService) { }

  datoscita !: Cita

  editarCita = new FormGroup({
    profesional : new FormControl(''),
    tipo_mascota : new FormControl(''),
    nickname : new FormControl(''),
    tipo_proceso : new FormControl(''),
    fecha : new FormControl(''),
    hora : new FormControl('')
  })

  ngOnInit(): void {
    let id_cita = this.activeroute.snapshot.paramMap.get('id_cita')
    this.cita.extraerCita(id_cita).subscribe(datos=>{
      this.datoscita = datos;
      console.log(datos)
      this.editarCita.setValue({
        'profesional': this.datoscita.profesional,
        'tipo_mascota': this.datoscita.tipo_mascota,
        'nickname': this.datoscita.nickname,
        'tipo_proceso': this.datoscita.tipo_proceso,
        'fecha': this.datoscita.fecha,
        'hora': this.datoscita.hora,
      })
    })
  }

  putform(form: Cita){
    let citaid_up = this.activeroute.snapshot.paramMap.get('id_cita');
    this.cita.putCita(form,citaid_up).subscribe(datos=>{
      console.log(datos)
      alert("Cita actualizada exitosamente")
      this.router.navigate(['programadas']);
    })
  }

  regresar(){
    this.router.navigate(['programadas']);
  }
}
