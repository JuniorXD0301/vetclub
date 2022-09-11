import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, FormsModule } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { Profesional } from 'src/app/models/profesional';
import { ProfesionalService } from 'src/app/services/profesional.service';

@Component({
  selector: 'app-editar-profesional',
  templateUrl: './editar-profesional.component.html',
  styleUrls: ['./editar-profesional.component.css']
})
export class EditarProfesionalComponent implements OnInit {

  constructor(private activeroute:ActivatedRoute, private router:Router, private form:FormsModule, private profesional:ProfesionalService) { }

  datosprofesional !: Profesional;

  editarProfesional = new FormGroup({
    tipo_profesional : new FormControl(''),
    nombre : new FormControl(''),
    correo : new FormControl(''),
    nickname : new FormControl('')
  })

  ngOnInit(): void {
    let id_user = this.activeroute.snapshot.paramMap.get('id_profesional')
    this.profesional.extraerProfesional(id_user).subscribe(datos=>{
      this.datosprofesional = datos;
      console.log(datos)
      this.editarProfesional.setValue({
        'tipo_profesional': this.datosprofesional.tipo_profesional,
        'nombre': this.datosprofesional.nombre,
        'correo': this.datosprofesional.correo,
        'nickname': this.datosprofesional.nickname,
      })
    })
  }

  putform(form: Profesional){
    let proid_up = this.activeroute.snapshot.paramMap.get('id_profesional');
    this.profesional.putProfesional(form,proid_up).subscribe(datos=>{
      console.log(datos)
      alert("Profesional actualizada exitosamente")
      this.router.navigate(['profesionales']);
    })
  }

  regresar(){
    this.router.navigate(['profesionales']);
  }

}
