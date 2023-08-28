from flask_sqlalchemy import SQLAlchemy
import enum

db = SQLAlchemy()

class Cancion(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(128))
    minutos = db.Column(db.Integer)
    segundos = db.Column(db.Integer)
    interprete = db.Column(db.String(128))

    def __repr__(self):
        return "{}-{}-{}-{}".format(self.titulo, self.minutos, self.segundos, self.interprete)

class Medio(enum.Enum):
    DISCO = 1
    CASETE = 2
    CD = 3
class Albun(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    anho = db.Column(db.Integer)
    descripcion = db.Column(db.String(100))
    medio = db.Column(db.Enum(Medio))

    def __repr__(self):
        return "{}-{}-{}-{}".format(self.titulo, self.anho, self.descripcion, self.medio)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre= db.Column(db.String(128))
    contrasenha = db.Column(db.String(128))

    def __repr__(self):
        return "{}-{}".format(self.nombre, self.contrasenha)

