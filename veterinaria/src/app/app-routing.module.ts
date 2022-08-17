import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MascotaComponent } from './todo_mascota/mascota/mascota.component'
import { ListarMascotasComponent } from './todo_mascota/listar-mascotas/listar-mascotas.component';
import { ListarUsuarioComponent } from './usuario/listar-usuario/listar-usuario.component';
import { CrearUsuarioComponent } from './usuario/crear-usuario/crear-usuario.component';

//para que funcionen los componentes de rutas
const routes: Routes = [
  {
    path: '',
    component: ListarMascotasComponent
  },
  {
    path: 'mascota',
    component: MascotaComponent
  },
  {
    path: 'usuarios',
    component: ListarUsuarioComponent
  },
  {
    path: 'usuarios/usuario',
    component: CrearUsuarioComponent
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