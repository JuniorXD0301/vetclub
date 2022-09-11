import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Cita } from 'src/app/models/cita';
import { CitaService } from 'src/app/services/cita.service';

@Component({
  selector: 'app-programada',
  templateUrl: './programada.component.html',
  styleUrls: ['./programada.component.css']
})
export class ProgramadaComponent implements OnInit {

  cita : Cita[] = []

  constructor(private citaService: CitaService, private router: Router) { }

  ngOnInit(): void {
    this.cargarCita()
  }

  cargarCita(){
    this.citaService.obtenerCita().subscribe(datos=> {
      this.cita = datos
      console.log(this.cita)
    })
  }

  nuevaCita(){
    this.router.navigate(['programadas/cita'])
  }

  nuevaCitaStyle(){
    this.router.navigate(['programadas/style'])
  }

  editarCita(id_cita: any){
    this.router.navigate(['programadas/editarCita', id_cita])
  }

  eliminarCita(id_cita: any){
    this.citaService.eliminarCita(id_cita).subscribe(fin=> {
      this.cargarCita()
      console.log(fin)
      alert("Cita eliminada con exito")
    })
  }

  regresar(){
    this.router.navigate(['admin'])
  }
}
