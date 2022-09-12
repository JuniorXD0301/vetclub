import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MascotaComponent } from './todo_mascota/mascota/mascota.component';
import { ListarMascotasComponent } from './todo_mascota/listar-mascotas/listar-mascotas.component';
import { CrearUsuarioComponent } from './usuario/crear-usuario/crear-usuario.component';
import { ListarUsuarioComponent } from './usuario/listar-usuario/listar-usuario.component';
import { CrearProfesionalComponent } from './profesional/crear-profesional/crear-profesional.component';
import { ListarProfesionalComponent } from './profesional/listar-profesional/listar-profesional.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { IndexComponent } from './principal/index/index.component';
import { TiendaComponent } from './principal/tienda/tienda.component';
import { CitaComponent } from './agenda/cita/cita.component';
import { ProgramadaComponent } from './agenda/programada/programada.component';
import { CitaStyleComponent } from './agenda/cita-style/cita-style.component';
import { AdminComponent } from './principal/admin/admin.component';
import { EditarUsuarioComponent } from './usuario/editar-usuario/editar-usuario.component';
import { EditarProfesionalComponent } from './profesional/editar-profesional/editar-profesional.component';
import { EditarMascotaComponent } from './todo_mascota/editar-mascota/editar-mascota.component';
import { EditarProgramadaComponent } from './agenda/editar-programada/editar-programada.component';
import {MatDatepickerModule } from '@angular/material/datepicker';
import { MatNativeDateModule } from '@angular/material/core';
import {MatInputModule} from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';

@NgModule({
  declarations: [
    AppComponent,
    MascotaComponent,
    ListarMascotasComponent,
    CrearUsuarioComponent,
    ListarUsuarioComponent,
    CrearProfesionalComponent,
    ListarProfesionalComponent,
    IndexComponent,
    TiendaComponent,
    CitaComponent,
    ProgramadaComponent,
    CitaStyleComponent,
    AdminComponent,
    EditarUsuarioComponent,
    EditarProfesionalComponent,
    EditarMascotaComponent,
    EditarProgramadaComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MatDatepickerModule,
    MatFormFieldModule,
    MatInputModule,
    MatNativeDateModule
  ],
  providers: [MatDatepickerModule, MatNativeDateModule ],
  bootstrap: [AppComponent]
})
export class AppModule { }
