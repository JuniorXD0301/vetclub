from crypt import methods
from dataclasses import field, fields
from enum import unique
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, supports_credentials=True)

#ligar base de datos a la app en flask, recurso unico conocido como URI
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://Mauricio:Mauricio@localhost/vetclub'
#eliminacion de errores, es una configuracion por defecto(eliminar warningus)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
CORS(app, supports_credentials=True)
#paso la configuracion al orm
db = SQLAlchemy(app)

#Esquema para la creacion de instacias
#Serializacion y deserializacion de objetos JSON
ma = Marshmallow(app)

#DEFINICION DE MODELOS, que representaria mis tablas
#tabla usuario
class usuario(db.Model):
    id_usuario = db.Column(db.Integer,primary_key=True,unique=True,autoincrement=True)
    nombre = db.Column(db.String(50))
    correo = db.Column(db.String(50))
    telefono = db.Column(db.BigInteger)
    nickname = db.Column(db.String(50))

    #constructor usuario
    def __init__(self,nombre,correo,telefono,nickname):
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.nickname = nickname

#tabla Secretario
class secretario(db.Model):
    id_secretario = db.Column(db.Integer,primary_key=True,unique=True,autoincrement=True)
    nombre = db.Column(db.String(50))
    correo = db.Column(db.String(50))
    nickname = db.Column(db.String(50))

    #constructor Secretario
    def __init__(self,nombre,correo,nickname):
        self.nombre = nombre
        self.correo = correo
        self.nickname = nickname

#tabla Profesional
class profesional(db.Model):
    id_profesional = db.Column(db.Integer,primary_key=True,unique=True,autoincrement=True)
    tipo_profesional = db.Column(db.ForeignKey('tipo_profesional.id_tipoProfesional'))
    nombre = db.Column(db.String(50))
    correo = db.Column(db.String(50))
    nickname = db.Column(db.String(50))

    #constructor profesional
    def __init__(self,tipo_profesional,nombre,correo,nickname):
        self.tipo_profesional = tipo_profesional
        self.nombre = nombre
        self.correo = correo
        self.nickname = nickname

#tabla tipo_profesional
class tipo_profesional(db.Model):
    id_tipoProfesional = db.Column(db.Integer,primary_key=True,unique=True,autoincrement=True)
    profesion = db.Column(db.String(20))
    descripcion = db.Column(db.String(100))

    #constructor tipo_profesional
    def __init__(self,profesion,descripcion):
        self.profesion = profesion
        self.descripcion = descripcion

#tabla mascota
class mascota(db.Model):
    id_mascota = db.Column(db.Integer,primary_key=True,unique=True,autoincrement=True)
    tipo_mascota = db.Column(db.ForeignKey('tipo_mascota.id_tipoMascota'))
    nombre = db.Column(db.String(50))
    raza = db.Column(db.String(20))
    historial = db.Column(db.String(100))

    #constructor mascota
    def __init__(self,tipo_mascota,nombre,raza,historial):
        self.tipo_mascota = tipo_mascota
        self.nombre = nombre
        self.raza = raza
        self.historial = historial

#tabla tipo_mascota
class tipo_mascota(db.Model):
    id_tipoMascota = db.Column(db.Integer,primary_key=True,unique=True,autoincrement=True)
    animal = db.Column(db.String(15))

    #constructor tipo_mascota
    def __init__(self,animal):
        self.animal = animal

#tabla cita
class cita(db.Model):
    id_cita = db.Column(db.Integer,primary_key=True,unique=True,autoincrement=True)
    profesional = db.Column(db.ForeignKey('profesional.id_profesional'))
    tipo_mascota = db.Column(db.ForeignKey('tipo_mascota.id_tipoMascota'))
    nickname = db.Column(db.String(60))
    tipo_proceso = db.Column(db.ForeignKey('tipo_proceso.id_tipoProceso'))
    fecha = db.Column(db.Date)
    hora = db.Column(db.Time)

    #constructor cita
    def __init__(self,profesional,mascota,nickname,tipo_proceso,fecha,hora):
        self.profesional = profesional
        self.mascota = mascota
        self.nickname = nickname
        self.tipo_proceso = tipo_proceso
        self.fecha = fecha
        self.hora = hora

#tabla tipo_proceso
class tipo_proceso(db.Model):
    id_tipoProceso = db.Column(db.Integer,primary_key=True,unique=True,autoincrement=True)
    nombre = db.Column(db.String(30))
    descripcion = db.Column(db.String(80))
    costo = db.Column(db.Float)

    #constructor tipo_proceso
    def __init__(self,nombre,descripcion,costo):
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo

#tabla agenda
class agenda(db.Model):
    id_agenda = db.Column(db.Integer,primary_key=True,unique=True,autoincrement=True)
    cita = db.Column(db.ForeignKey('cita.id_cita'))

    #constructor agenda
    def __init__(self,cita):
        self.cita = cita

#creacion en mysql
db.create_all()

#creacion de esquema, para interactuar con el
class MascotaSchema(ma.Schema):
    class Meta:
        fields = ('id_mascota','tipo_mascota', 'nombre', 'raza', 'historial')
#instanciar esquema
mascotaSchema = MascotaSchema()
#multiples datos o respuestas apartir de la base de datos
mascotaMultipleSchema = MascotaSchema(many = True)

#creacion de esquema, para interactuar con el
class TipoMascotaSchema(ma.Schema):
    class Meta:
        fields = ('id_tipoMascota','animal')
#instanciar esquema
tipoMascotaSchema = TipoMascotaSchema()
#multiples datos o respuestas apartir de la base de datos
tipoMascotaMultipleSchema = TipoMascotaSchema(many = True)

#creacion de esquema, para usuario
class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('id_usuario', 'nombre', 'correo', 'telefono', 'nickname')
#instancia del esquema para 1
usuarioSchema = UsuarioSchema()
#instancia multiples datos
usuarioMultipleSchema = UsuarioSchema(many = True)

#creacion de esquema, para profesional
class ProfesionalSchema(ma.Schema):
    class Meta:
        fields = ('id_profesional', 'tipo_profesional', 'nombre', 'correo', 'nickname')
#instanciar esquema
profesionalSchema = ProfesionalSchema()
#multiples datos o respuestas apartir de la bd
profesionalMultipleSchema = ProfesionalSchema(many = True)

#creacion de esquema, para citas
class CitaSchema(ma.Schema):
    class Meta:
        fields = ('id_cita', 'profesional', 'tipo_mascota', 'nickname', 'tipo_proceso', 'fecha', 'hora')
#instanciar esquema
citaSchema = CitaSchema()
#multiples datos o respuestas apartir de la bd
citaMultipleSchema = CitaSchema(many = True)

#Endpoints de rest-api, Apartado de Mascotas
#crear una mascota
@app.route('/mascota', methods=['POST'])
def addMascota():
    #recibo y guardo los datos
    tipo_mascota = request.json['tipo_mascota']
    nombre = request.json['nombre']
    raza = request.json['raza']
    historial = request.json['historial']
    #creo la masco
    new_mascota = mascota(tipo_mascota, nombre, raza, historial)
    #guardo en bd
    db.session.add(new_mascota)
    print(new_mascota)
    db.session.commit()
    #respondemos con la info de creacion, de 1 sola tarea
    return mascotaSchema.jsonify(new_mascota)

#get mascotas
@app.route('/mascota', methods=['GET'])
def get_mascota():
    #consulatar todo del modelo de mascota especifica
    mascotas = mascota.query.all()
    #metodo dump para pasar datos de la consulta
    mas = mascotaMultipleSchema.dump(mascotas)
    return jsonify(mas)

#get masco
@app.route('/mascota/<id_mascota>', methods=['GET'])
def get_mascoById(id_mascota):
    mascoById = mascota.query.get(id_mascota)
    return mascotaSchema.jsonify(mascoById)

#actualizar masco
@app.route('/mascota/<id_mascota>', methods=['PUT'])
def actualizarMasco(id_mascota):
    actualizar = mascota.query.get(id_mascota)
    tipo_mascota = request.json['tipo_mascota']
    nombre = request.json['nombre']
    raza = request.json['raza']
    historial = request.json['historial']
    #update entre variables definidas a los datos
    actualizar.tipo_mascota = tipo_mascota
    actualizar.nombre = nombre
    actualizar.raza = raza
    actualizar.historial = historial
    #update bd
    db.session.commit()
    #mostrar el update al usuario
    return mascotaSchema.jsonify(actualizar)
    
#eliminar masco
@app.route('/mascota/<id_mascota>', methods=['DELETE'])
def borrarMasco(id_mascota):
    delMasco = mascota.query.get(id_mascota)
    #borrar en bd
    db.session.delete(delMasco)
    #update bd
    db.session.commit()
    
    return mascotaSchema.jsonify(delMasco)

#Endpoints de rest-api, Apartado tipo Mascota
#crear un tipo mascota
@app.route('/tipo_mascota', methods=['POST'])
def addTipoMascota():
    animal = request.json['animal']
    #creo el animal
    new_animal = tipo_mascota(animal)
    db.session.add(new_animal)
    db.session.commit()
    return tipoMascotaSchema.jsonify(new_animal)

#tipos de mascotas
@app.route('/tipo_mascota', methods=['GET'])
def get_tipo_mascota():
    tipo_mascotas = tipo_mascota.query.all()
    tipo_m = tipoMascotaMultipleSchema.dump(tipo_mascotas)
    return jsonify(tipo_m)

#get tipo masco
@app.route('/tipo_mascota/<id_tipoMascota>', methods=['GET'])
def get_tipomascoById(id_tipoMascota):
    tipomascoById = tipo_mascota.query.get(id_tipoMascota)
    return tipoMascotaSchema.jsonify(tipomascoById)

#actualizar tipo_masco
@app.route('/tipo_mascota/<id_tipoMascota>', methods=['PUT'])
def actualizar_tipo_Masco(id_tipoMascota):
    actualizar = tipo_mascota.query.get(id_tipoMascota)
    animal = request.json['animal']
    #update entre variables definidas a los datos
    actualizar.animal = animal
    #update bd
    db.session.commit()
    #mostrar el update al usuario
    return tipoMascotaSchema.jsonify(actualizar)
    
#eliminar tipo_masco
@app.route('/tipo_mascota/<id_tipoMascota>', methods=['DELETE'])
def borrartipoMasco(id_tipoMascota):
    delMasco = tipo_mascota.query.get(id_tipoMascota)
    #borrar en bd
    db.session.delete(delMasco)
    #update bd
    db.session.commit()
    
    return tipoMascotaSchema.jsonify(delMasco)

#Endpoints de rest-api, Apartado de Usuario
#crear una usuario
@app.route('/usuario', methods=['POST'])
def addUsuario():
    #recibo y guardo los datos
    nombre = request.json['nombre']
    correo = request.json['correo']
    telefono = request.json['telefono']
    nickname = request.json['nickname']
    #creo la masco
    new_usuario = usuario(nombre, correo, telefono, nickname)
    #guardo en bd
    db.session.add(new_usuario)
    print(new_usuario,'hola')
    db.session.commit()
    #respondemos con la info de creacion, de 1 sola tarea
    return usuarioSchema.jsonify(new_usuario)

#get usuarios
@app.route('/usuario', methods=['GET'])
def get_usuario():
    #consulatar todo del modelo de usuarios
    usuarios = usuario.query.all()
    #metodo dump para pasar datos de la consulta
    us = usuarioMultipleSchema.dump(usuarios)
    return jsonify(us)

#get usuario
@app.route('/usuario/<id_usuario>', methods=['GET'])
def get_userById(id_usuario):
    userById = usuario.query.get(id_usuario)
    return usuarioSchema.jsonify(userById)

#actualizar usuario
@app.route('/usuario/<id_usuario>', methods=['PUT'])
def actualizarUser(id_usuario):
    actualizar = usuario.query.get(id_usuario)
    nombre = request.json['nombre']
    correo = request.json['correo']
    telefono = request.json['telefono']
    nickname = request.json['nickname']
    #update entre variables definidas a los datos
    actualizar.nombre = nombre
    actualizar.correo = correo
    actualizar.telefono = telefono
    actualizar.nickname = nickname
    #update bd
    db.session.commit()
    #mostrar el update al usuario
    return usuarioSchema.jsonify(actualizar)
    
#eliminar user
@app.route('/usuario/<id_usuario>', methods=['DELETE'])
def borrarUser(id_usuario):
    delUser = usuario.query.get(id_usuario)
    #borrar en bd
    db.session.delete(delUser)
    #update bd
    db.session.commit()
    
    return usuarioSchema.jsonify(delUser)

#Endpoints de rest-api, Apartado de Profesional
#crear una profesional
@app.route('/profesional', methods=['POST'])
def addPro():
    #recibo y guardo los datos
    tipo_profesional = request.json['tipo_profesional']
    nombre = request.json['nombre']
    correo = request.json['correo']
    nickname = request.json['nickname']
    #creo al profesional
    new_profesional = profesional(tipo_profesional, nombre, correo, nickname)
    #guardo en bd
    db.session.add(new_profesional)
    print(new_profesional)
    db.session.commit()
    #respondemos con la info de creacion, de 1 sola tarea
    return profesionalSchema.jsonify(new_profesional)

#get profesionales
@app.route('/profesional', methods=['GET'])
def get_pro():
    #consultar todo del modelo de mascota especifica
    profesionales = profesional.query.all()
    #metodo dump para pasar datos de la consulta
    pro = profesionalMultipleSchema.dump(profesionales)
    return jsonify(pro)

#get profesional
@app.route('/profesional/<id_profesional>', methods=['GET'])
def get_proById(id_profesional):
    proById = profesional.query.get(id_profesional)
    return profesionalSchema.jsonify(proById)

#actualizar profesional
@app.route('/profesional/<id_profesional>', methods=['PUT'])
def actualizarPro(id_profesional):
    actualizar = profesional.query.get(id_profesional)
    tipo_profesional = request.json['tipo_profesional']
    nombre = request.json['nombre']
    correo = request.json['correo']
    nickname = request.json['nickname']
    #update entre variables definidas a los datos
    actualizar.tipo_profesional = tipo_profesional
    actualizar.nombre = nombre
    actualizar.correo = correo
    actualizar.nickname = nickname
    #update bd
    db.session.commit()
    #mostrar el update al usuario
    return profesionalSchema.jsonify(actualizar)
    
#eliminar profesional
@app.route('/profesional/<id_profesional>', methods=['DELETE'])
def borrarPro(id_profesional):
    delPro = profesional.query.get(id_profesional)
    #borrar en bd
    db.session.delete(delPro)
    #update bd
    db.session.commit()
    
    return profesionalSchema.jsonify(delPro)

#Endpoints de rest-api, Apartado de Citas
#crear una cita
@app.route('/cita', methods=['POST'])
def addCita():
    #recibo y guardo los datos
    profesional = request.json['profesional']
    tipo_mascota = request.json['tipo_mascota']
    nickname = request.json['nickname']
    tipo_proceso = request.json['tipo_proceso']
    fecha = request.json['fecha']
    hora = request.json['hora']
    #creo la cita
    new_cita = cita(profesional, tipo_mascota, nickname, tipo_proceso, fecha, hora)
    #guardo en bd
    db.session.add(new_cita)
    print(new_cita)
    db.session.commit()
    #respondemos con la info de creacion, de 1 sola tarea
    return citaSchema.jsonify(new_cita)

#get citas todas
@app.route('/cita', methods=['GET'])
def get_cita():
    #consultar todo del modelo de mascota especifica
    citas = cita.query.all()
    #metodo dump para pasar datos de la consulta
    ci = citaMultipleSchema.dump(citas)
    return jsonify(ci)

#get una sola cita
@app.route('/cita/<id_cita>', methods=['GET'])
def get_citaById(id_cita):
    citaById = cita.query.get(id_cita)
    return citaSchema.jsonify(citaById)

#actualizar info de la cita
@app.route('/cita/<id_cita>', methods=['PUT'])
def actualizarCita(id_cita):
    actualizar = cita.query.get(id_cita)
    profesional = request.json['profesional']
    tipo_mascota = request.json['tipo_mascota']
    nickname = request.json['nickname']
    tipo_proceso = request.json['tipo_proceso']
    fecha = request.json['fecha']
    hora = request.json['hora']
    #update entre variables definidas a los datos
    actualizar.profesional = profesional
    actualizar.tipo_mascota = tipo_mascota
    actualizar.nickname = nickname
    actualizar.tipo_proceso = tipo_proceso
    actualizar.fecha = fecha
    actualizar.hora = hora
    #update bd
    db.session.commit()
    #mostrar el update al usuario
    return citaSchema.jsonify(actualizar)
    
#eliminar cita
@app.route('/cita/<id_cita>', methods=['DELETE'])
def borrarCita(id_cita):
    delCita = cita.query.get(id_cita)
    #borrar en bd
    db.session.delete(delCita)
    #update bd
    db.session.commit()
    
    return citaSchema.jsonify(delCita)

#inicializacion del programa app
if __name__ == "__main__":
    app.run(debug=True)

#Endpoints de rest-api, Apartado de tablas tipo
"""Este apartado se realizo directamente en sql"""

#Tambien se pueden agregar datos predeterminados por flask o por sql
#  new_tipo = tipo_mascota(animal=1)
#   guardo en bd
#   db.session.add(new_tipo)
#   print(new_tipo)
#   db.session.commit()

"""
insert into tipo_profesional values (NULL,"Veterinario","Encargado de los procedimientos principales");
insert into tipo_profesional values (NULL,"Estilista","Encargado de la parte estetica para los animales");
insert into tipo_profesional values (NULL,"Secretario","Encargado de la agenda, citas, inventario");

insert into tipo_mascota values (NULL,"perro");
insert into tipo_mascota values (NULL,"gato");

insert into tipo_proceso values (NULL,"Cita General", "Revision general del animal", 30.000);
insert into tipo_proceso values (NULL,"Peluquear", "Peluquear al animal", 20.000);
insert into tipo_proceso values (NULL,"Lavado", "Servicio de limpieza", 15.000);
insert into tipo_proceso values (NULL,"Desparacitar", "Servicio de limpieza", 10.000);
"""