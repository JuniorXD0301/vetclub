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

@NgModule({
  declarations: [
    AppComponent,
    MascotaComponent,
    ListarMascotasComponent,
    CrearUsuarioComponent,
    ListarUsuarioComponent,
    CrearProfesionalComponent,
    ListarProfesionalComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    BrowserAnimationsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
