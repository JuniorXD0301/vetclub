from crypt import methods
from dataclasses import field
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
    descripcion = db.Column(db.String(50))

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
    mascota = db.Column(db.ForeignKey('mascota.id_mascota'))
    usuario = db.Column(db.ForeignKey('usuario.id_usuario'))
    tipo_proceso = db.Column(db.ForeignKey('tipo_proceso.id_tipoProceso'))
    fecha = db.Column(db.Date)
    hora = db.Column(db.Time)

    #constructor cita
    def __init__(self,profesional,mascota,usuario,tipo_proceso,fecha,hora):
        self.profesional = profesional
        self.mascota = mascota
        self.usuario = usuario
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

#inicializacion del programa app
if __name__ == "__main__":
    app.run(debug=True)


#agregar datos predeterminados por flask o por sql
#  new_tipo = tipo_mascota(animal=1)
#   guardo en bd
#   db.session.add(new_tipo)
#   print(new_tipo)
#   db.session.commit()
    