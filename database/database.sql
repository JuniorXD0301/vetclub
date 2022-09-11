create database vetclub;

use vetclub;
show tables;

select * from tipo_mascota;

insert into tipo_profesional values(NULL,"Veterinario","Encargado de los procedimientos con las mascotas");
insert into tipo_profesional values(NULL,"Estilista","Encargado de la estetica de las mascotas");
insert into tipo_profesional values(NULL,"Secretario","Encargado de la administracion y el inventario");

insert into tipo_mascota values(NULL,"Perro");
insert into tipo_mascota values(NULL,"Gato");

insert into profesional values(NULL, 1, "Camila Ardila", "camila@vet.com", "camilaAdmin");
insert into profesional values(NULL, 2, "Jose Ramirez", "jose@estil.com", "josearch");
insert into profesional values(NULL, 1, "Carlos Navas", "carlito@vet.com", "carlitoNava");
insert into profesional values(NULL, 2, "Ximena Rosales", "ximena@estile.com", "ximenita");

select * from tipo_proceso;

insert into tipo_proceso values(NULL, "Cita General", "Revisión general del animal", 30);
insert into tipo_proceso values(NULL, "Corte de Pelo", "Peluquear animal", 20);
insert into tipo_proceso values(NULL, "Baño", "Servicio de limpieza", 15);
insert into tipo_proceso values(NULL, "Vacunaciones", "Servicio de vacunaciones", 10);
insert into tipo_proceso values(NULL, "Masaje Relajante", "Servicio de masaje", 15);
insert into tipo_proceso values(NULL, "Limpieza Dental", "Servicio de higiene", 30);
insert into tipo_proceso values(NULL, "Tests Serológicos", "Para identificar diversas enfermedades infecciosas", 60);


SET SQL_SAFE_UPDATES = 0;
select * from profesional;
delete from profesional where nombre = 'Jorge';
select * from tipo_profesional;
