import { Injectable } from '@angular/core';
import { HttpClient,HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Profesional } from '../models/profesional';

@Injectable({
  providedIn: 'root'
})
export class ProfesionalService {

  constructor(private http: HttpClient) { }

  url = "http://localhost:5000/profesional"

  //metodo para llamar la info de profesional conectados a bd y usando la interfaz
  obtenerProfesional():Observable<Profesional[]>{
    return this.http.get<Profesional[]>(this.url)
  }

  agregarPro(form: Profesional):Observable<Profesional>{
    return this.http.post<Profesional>(this.url,form)
  }

  //metodo para eliminar un profesional
  eliminarPro(id_profesional:number):Observable<Profesional>{
    let ruta2 = this.url+'/'+id_profesional

    return this.http.delete<Profesional>(ruta2, {
      headers: new HttpHeaders({ 'Content-Type': 'aplication/json'})
    })
  }

}
