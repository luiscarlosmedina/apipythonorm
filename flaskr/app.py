from flaskr import create_app
from .modelos import db, Cancion, Album, Usuario, Medio

app = create_app("default")
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
with app.app_context():
    #c =Cancion(titulo='prueba', minutos =2, segundos=25, interprete='artista')
    u = Usuario(nombre="luiscarlos", contrasenha="adminluis")
    a = Album(titulo='prueba', anho=2012, descripcion='origen puertoriqueño', medio=Medio.CD)
    u.albunes.append(a)
    db.session.add(u)
    db.session.commit()
    print(Usuario.query.all())
    print(Usuario.query.all()[0].albunes)
    db.session.delete(u)
    print(Usuario.query.all())
    print(Album.query.all())
