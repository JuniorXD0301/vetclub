import { Injectable } from '@angular/core';
import { HttpClient,HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Usuario } from '../models/usuario';

@Injectable({
  providedIn: 'root'
})
export class UsuarioService {

  constructor(private http: HttpClient) { }

  url = "http://localhost:5000/usuario"

  //metodo para llamar la informacion de las mascotas conectandose a bd y usando la interfaz
  obtenerUsuario():Observable<Usuario[]>{
    return this.http.get<Usuario[]>(this.url);
  }

  //metodo para llamar un solo usuario
  extraerUsuario(id:any):Observable<Usuario>{
    let ruta1 = this.url+'/'+id;
    return this.http.get<Usuario>(ruta1)
  }

  //poner informacion de un solo usuario
  putUsuario(form:Usuario, id:any):Observable<Usuario>{
    let ruta2 = this.url+'/'+id;
    return this.http.put<Usuario>(ruta2, form)
  }

  //metodo para agregar usuario
  agregarUser(form: Usuario):Observable<Usuario>{
    return this.http.post<Usuario>(this.url,form)
  }

  editar(usuario: string): Observable<any>{
    return this.http.put(`${this.url}/usuario`, JSON.stringify(usuario));
  }

  //metodo para eliminar un usuario
  eliminarUsuario(id_usuario:number):Observable<Usuario>{
    let ruta2 = this.url+'/'+id_usuario;

    return this.http.delete<Usuario>(ruta2, {
      headers: new HttpHeaders({ 'Content-Type': 'aplication/json'})
    })
  }

}