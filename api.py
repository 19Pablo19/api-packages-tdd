from flask import Flask
from flask_restful import Resource, Api
from models import Filmsq
from authlib.flask.oauth2 import AuthorizationServer
import os
from authlib.specs.rfc7519 import jwt


app = Flask(__name__)
api = Api(app)

#Pablo
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoiUGFibG8ifQ.R4W-V2MKib5vuApe8wvFOGb7j61WhvtV2ElTh5_WOrU'


header = {'alg': 'HS256'}
key = 'SECRET'
#os.environ['AUTHLIB_INSECURE_TRANSPORT'] = 'true'
# pelicula1 = Filmsq('Avatar', 300)
# print(pelicula1.__dict__)

class ListUsers(Resource):
    def get(self):
        return {"Listado de usuarios":users}, 200

class Users(Resource):
    def post(self, name):
        if name:
            users.append({'id':len(users)+1, 'name': name}) #Nuevo usuario
            payload = {
                    #'id': id,
                    'name': name,
            }
            encoded_token = jwt.encode(header, payload, key)

            return print(encoded_token), print(jwt.decode(encoded_token, key))

        else:
            return 404



#app.config["DEBUG"] = False
#https://code.i-harness.com/es/q/13c16e6
#https://nearsoft.com/blog/how-to-create-an-api-and-web-applications-with-flask/
users = [
    {
        'id': '1',
        'name': 'Alex'
    }
]
films = [
    {
        'id': 1,
        'tittle': 'Avatar',
        'quantity': '30'
    },
    {
        'id': 2,
        'tittle': 'Madagascar',
        'quantity': '30'
    }
]


films.append({
    'id': 3,
    'tittle': 'Hola',
    'quantity': '30'
})
for film in films:
    print(film)

# Utilizar la clase models
def pruebaz(name):
    #films.append(filmf)>
    return name

# Clase prueba para ver como controlar los enlaces FUNCIONA
class Hello(Resource):
    def get(self, name):
        return {"Hello":name}
api.add_resource(Hello, '/hello/<name>', endpoint = 'hello')


class Films(Resource):

    #Devuelve 1 sola pelicula si existe
    def get(self, name, token):
        payload = jwt.decode(token, key)
        # Si tras decodificar ese usuario existe..
        if verificar(token):
                #Comprobamos que existe la pelicula
            for film in films:
                if name == film['tittle']:
                    return {"GET":film}, 200
                return {"No existe la pelicula":name}
        #Si no existe
        return {"No tienes permiso para acceder": token} #No se porque no me devuelve esto

def verificar(token):
    payload = jwt.decode(token, key)
    for user in users:
        if user['name'] == payload['name']:
            return True
    return False


class Films2(Resource):

    #Devuelve 1 sola pelicula si existe
    def get(self, name):
        for film in films:
            if name == film['tittle']:
                return {"GET":film}, 200
            return {"No existe":name}

    def put(self, name):
        for film in films:
            if name == film['tittle']:
                return {"Pelicula actualizada":name}, 200
            return {"La pelicula que quieres modificar no existe"}, 204

    def delete(self, name):
        return {"DELETE":name}, 200

    def post(self, name):
        for film in films:
            if name == film['tittle']:
                return {"Ya exite":name}, 200
        #Si no existe la pelicula se añade esta al final del listado
        films.append({'id':len(films)+1, 'tittle': name, 'quantity': 1})

        return {"Añadida":name}, 201

class ListFilms(Resource):
    def get(self):
        return {"Listado de peliculas":films}, 200



api.add_resource(ListFilms, '/films')
api.add_resource(ListUsers, '/users')
api.add_resource(Films, '/films/<name>/<token>')
api.add_resource(Users, '/users/<name>')




#Utiliza la funcion pruebaz!
class Prueba(Resource):
    def get(self, name):
        nombre = pruebaz(name)
        return nombre
api.add_resource(Prueba, '/prueba/<name>')




if __name__ == "__main__":
    app.run()

#Ejecutar en terminal
# export FLASK_APP=api.py
# flask run
