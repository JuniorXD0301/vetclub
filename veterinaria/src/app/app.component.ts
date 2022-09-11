import { Component } from '@angular/core';
import { Profesional } from 'src/app/models/profesional';
import { ProfesionalService } from 'src/app/services/profesional.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'veterinaria';

  profesional : Profesional[] = []

  constructor(private profesionalService: ProfesionalService, private router: Router) { }

  ngOnInit(): void {
    this.cargarProfesional()
  }

  cargarProfesional(){
    this.profesionalService.obtenerProfesional().subscribe(datos=> {
      this.profesional = datos
      console.log(this.profesional)
    })
  }
}

