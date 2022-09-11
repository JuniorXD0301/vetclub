import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, FormsModule } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { mostrarMascota } from 'src/app/models/mostrar-mascota';
import { MascotaService } from 'src/app/services/mascota.service';

@Component({
  selector: 'app-mascota',
  templateUrl: './mascota.component.html',
  styleUrls: ['./mascota.component.css']
})
export class MascotaComponent implements OnInit {

  constructor(private router:Router, private form:FormsModule, private mascota:MascotaService) { }

  formMascota = new FormGroup({
    tipo_mascota: new FormControl(''),
    nombre: new FormControl(''),
    raza: new FormControl(''),
    historial: new FormControl(''),
  });
  
  ngOnInit(): void {
  }

  postform(form: mostrarMascota){
    this.mascota.agregarMasco(form).subscribe(info=>{
      alert('Se ha registrado con exito')
      console.log(info)
      this.router.navigate(['/mascotas']);
    })
    
  }

  regresar(){
    this.router.navigate(['/mascotas']);
  }

}
