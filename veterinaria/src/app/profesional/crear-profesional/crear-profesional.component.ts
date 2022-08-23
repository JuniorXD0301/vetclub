import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { Profesional } from 'src/app/models/profesional';
import { ProfesionalService } from 'src/app/services/profesional.service';

@Component({
  selector: 'app-crear-profesional',
  templateUrl: './crear-profesional.component.html',
  styleUrls: ['./crear-profesional.component.css']
})
export class CrearProfesionalComponent implements OnInit {

  constructor(private router:Router, private form:FormsModule, private profesional:ProfesionalService) { }

  formProfesional = new FormGroup({
    tipo_profesional : new FormControl(''),
    nombre : new FormControl(''),
    correo : new FormControl(''),
    nickname : new FormControl('')
  })

  ngOnInit(): void {
  }

  postform(form: Profesional){
    this.profesional.agregarPro(form).subscribe(info=>{
      alert('Se ha registrado con exito')
      console.log(info)
      this.router.navigate(['profesionales'])
    })
  }

  regresar(){
    this.router.navigate(['profesionales'])
  }

}
