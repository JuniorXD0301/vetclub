import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, FormsModule } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { mostrarMascota } from 'src/app/models/mostrar-mascota';
import { MascotaService } from 'src/app/services/mascota.service';

@Component({
  selector: 'app-editar-mascota',
  templateUrl: './editar-mascota.component.html',
  styleUrls: ['./editar-mascota.component.css']
})
export class EditarMascotaComponent implements OnInit {

  constructor(private activeroute:ActivatedRoute, private router:Router, private form:FormsModule, private mascota:MascotaService) { }

  datosmascotas !: mostrarMascota

  editarMascota = new FormGroup({
    tipo_mascota: new FormControl(''),
    nombre: new FormControl(''),
    raza: new FormControl(''),
    historial: new FormControl(''),
  });

  ngOnInit(): void {
    let id_masco = this.activeroute.snapshot.paramMap.get('id_mascota')
    this.mascota.extraerMascota(id_masco).subscribe(datos=>{
      this.datosmascotas = datos;
      console.log(datos)
      this.editarMascota.setValue({
        'tipo_mascota': this.datosmascotas.nombre,
        'nombre': this.datosmascotas.nombre,
        'raza': this.datosmascotas.raza,
        'historial': this.datosmascotas.historial,
      })
    })
  }

    putform(form: mostrarMascota){
    let masid_up = this.activeroute.snapshot.paramMap.get('id_mascota');
    this.mascota.putMascota(form,masid_up).subscribe(datos=>{
      console.log(datos)
      alert("Mascota actualizada exitosamente")
      this.router.navigate(['mascotas']);
    })
  }

  regresar(){
    this.router.navigate(['mascotas']);
  }

}
