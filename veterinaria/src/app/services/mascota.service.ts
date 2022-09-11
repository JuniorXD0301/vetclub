import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { Observable } from 'rxjs';
import { mostrarMascota } from '../models/mostrar-mascota';

@Injectable({
  providedIn: 'root'
})
export class MascotaService {

  constructor(private http: HttpClient) { }

  url = "http://localhost:5000/mascota";

  //metodo para llamar la informacion de las mascotas conectandose a la bd y usando la interfaz
  obtenerMascotas():Observable<mostrarMascota[]>{
    return this.http.get<mostrarMascota[]>(this.url);
  }

  extraerMascota(id_mascota:any):Observable<mostrarMascota>{
    let ruta1 = this.url+'/'+id_mascota;
    return this.http.get<mostrarMascota>(ruta1)
  }

  //poner informacion de la mascota
  putMascota(form:mostrarMascota, id:any):Observable<mostrarMascota>{
    let ruta2 = this.url+'/'+id;
    return this.http.put<mostrarMascota>(ruta2, form)
  }

  //metodo para agregar una nueva mascota
  agregarMasco(form:mostrarMascota):Observable<mostrarMascota>{
    return this.http.post<mostrarMascota>(this.url,form)
  } 

  //metodo para eliminar una mascota
  eliminarMasco(id_mascota:number):Observable<mostrarMascota>{
    let ruta2 = this.url+'/'+id_mascota;

    return this.http.delete<mostrarMascota>(ruta2, {
      headers: new HttpHeaders({ 'Content-Type': 'aplication/json'})
    })

  }

}
