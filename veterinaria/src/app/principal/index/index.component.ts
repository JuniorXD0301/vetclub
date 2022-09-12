import { Component, Input, OnInit, Output } from '@angular/core';
import { Profesional } from 'src/app/models/profesional';
import { ProfesionalService } from 'src/app/services/profesional.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-index',
  templateUrl: './index.component.html',
  styleUrls: ['./index.component.css']
})
export class IndexComponent implements OnInit {

  profesional : Profesional[] = [];

  constructor(private profesionalService: ProfesionalService, private router: Router) { }

  ngOnInit(): void {
    this.cargarProfesional()
  }

  scrollUp(){
    window.scrollTo(0,0);
  }

  cargarProfesional(){
    this.profesionalService.obtenerProfesional().subscribe(datos=> {
      this.profesional = datos
      console.log(this.profesional)
    })
  }

  veterinario(){
    this.router.navigate(['programadas/cita'])
  }

  estilismo(){
    this.router.navigate(['programadas/style'])
  }

  admin(){
    this.router.navigate(['admin'])
  }

  tienda(){
    this.router.navigate(['tienda'])
  }
}
