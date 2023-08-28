from flaskr import create_app
from .modelos import db, Cancion, Albun, Usuario

app = create_app("default")
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
with app.app_context():
    c =Cancion(titulo='prueba', minutos =2, segundos=25, interprete='artista')
    a = Albun(titulo='prueba', anho=2012, descripcion='origen puertoriqueño', medio="2")
    u = Usuario(nombre="luiscarlos", contrasenha="adminluis")
    db.session.add(c)
    db.session.add(a)
    db.session.add(u)
    db.session.commit()
    print(Cancion.query.all(), Albun.query.all(), Usuario.query.all())