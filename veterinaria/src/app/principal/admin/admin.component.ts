import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.css']
})
export class AdminComponent implements OnInit {

  constructor(private router:Router) { }

  ngOnInit(): void {
  }

  usuarios(){
    this.router.navigate(['usuarios'])
  }

  mascotas(){
    this.router.navigate(['mascotas'])
  }

  programadas(){
    this.router.navigate(['programadas'])
  }

  profesionales(){
    this.router.navigate(['profesionales'])
  }

  home(){
    this.router.navigate([''])
  }

}
