import { Component, NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MascotaComponent } from './todo_mascota/mascota/mascota.component'
import { ListarMascotasComponent } from './todo_mascota/listar-mascotas/listar-mascotas.component';
import { ListarUsuarioComponent } from './usuario/listar-usuario/listar-usuario.component';
import { CrearUsuarioComponent } from './usuario/crear-usuario/crear-usuario.component';
import { ListarProfesionalComponent } from './profesional/listar-profesional/listar-profesional.component';
import { CrearProfesionalComponent } from './profesional/crear-profesional/crear-profesional.component';
import { IndexComponent } from './principal/index/index.component';
import { CitaComponent } from './agenda/cita/cita.component';
import { ProgramadaComponent } from './agenda/programada/programada.component';
import { CitaStyleComponent } from './agenda/cita-style/cita-style.component';
import { AdminComponent } from './principal/admin/admin.component';
import { EditarUsuarioComponent } from './usuario/editar-usuario/editar-usuario.component';
import { EditarProfesionalComponent } from './profesional/editar-profesional/editar-profesional.component';
import { EditarMascotaComponent } from './todo_mascota/editar-mascota/editar-mascota.component';
import { EditarProgramadaComponent } from './agenda/editar-programada/editar-programada.component';
import { TiendaComponent } from './principal/tienda/tienda.component';

//para que funcionen los componentes de rutas
const routes: Routes = [
  {
    path: '',
    component: IndexComponent
  },
  {
    path: 'mascotas',
    component: ListarMascotasComponent
  },
  {
    path: 'mascotas/mascota',
    component: MascotaComponent
  },
  {
    path: 'mascotas/editarMascota/:id_mascota',
    component: EditarMascotaComponent
  },
  {
    path: 'usuarios',
    component: ListarUsuarioComponent
  },
  {
    path: 'usuarios/usuario',
    component: CrearUsuarioComponent
  },
  {
    path: 'usuarios/editarUsuario/:id_usuario',
    component: EditarUsuarioComponent
  },
  {
    path: 'profesionales',
    component: ListarProfesionalComponent
  },
  {
    path: 'profesionales/profesional',
    component: CrearProfesionalComponent
  },
  {
    path: 'profesionales/editarProfesional/:id_profesional',
    component: EditarProfesionalComponent
  },
  {
    path: 'programadas/cita',
    component: CitaComponent
  },
  {
    path: 'programadas/style',
    component: CitaStyleComponent
  },
  {
    path: 'programadas',
    component: ProgramadaComponent
  },
  {
    path: 'programadas/editarCita/:id_cita',
    component: EditarProgramadaComponent
  },
  {
    path: 'admin',
    component: AdminComponent
  },
  {
    path: 'tienda',
    component: TiendaComponent
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
