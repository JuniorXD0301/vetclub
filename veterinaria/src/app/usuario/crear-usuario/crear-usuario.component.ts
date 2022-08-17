import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { Usuario } from 'src/app/models/usuario';
import { UsuarioService } from 'src/app/services/usuario.service';

@Component({
  selector: 'app-crear-usuario',
  templateUrl: './crear-usuario.component.html',
  styleUrls: ['./crear-usuario.component.css']
})
export class CrearUsuarioComponent implements OnInit {

  constructor(private router:Router, private form:FormsModule, private usuario:UsuarioService) { }

  formUsuario = new FormGroup({
    nombre : new FormControl(''),
    correo : new FormControl(''),
    telefono : new FormControl(''),
    nickname : new FormControl('')
  });

  ngOnInit(): void {
  }

  postform(form: Usuario){
    this.usuario.agregarUser(form).subscribe(info=>{
      alert('Se ha registrado con exito')
      console.log(info)
      this.router.navigate(['usuarios'])
    })
  }

  regresar(){
    this.router.navigate(['usuarios'])
  }

}
