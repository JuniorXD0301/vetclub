import { Component, NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MascotaComponent } from './todo_mascota/mascota/mascota.component'
import { ListarMascotasComponent } from './todo_mascota/listar-mascotas/listar-mascotas.component';
import { ListarUsuarioComponent } from './usuario/listar-usuario/listar-usuario.component';
import { CrearUsuarioComponent } from './usuario/crear-usuario/crear-usuario.component';
import { ListarProfesionalComponent } from './profesional/listar-profesional/listar-profesional.component';
import { CrearProfesionalComponent } from './profesional/crear-profesional/crear-profesional.component';

//para que funcionen los componentes de rutas
const routes: Routes = [
  {
    path: 'mascota',
    component: ListarMascotasComponent
  },
  {
    path: '',
    component: MascotaComponent
  },
  {
    path: 'usuarios',
    component: ListarUsuarioComponent
  },
  {
    path: 'usuarios/crearusuario',
    component: CrearUsuarioComponent
  },
  {
    path: 'profesionales',
    component: ListarProfesionalComponent
  },
  {
    path: 'profesionales/profesional',
    component: CrearProfesionalComponent
  }

];

//declaraciones para rutas for.Root(routes)
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

export const routingComponenetes =
{
  ListarMascotasComponent,
  MascotaComponent,
  ListarUsuarioComponent,
  CrearUsuarioComponent
}
