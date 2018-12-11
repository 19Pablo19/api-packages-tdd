from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from models import Filmsq
from authlib.flask.oauth2 import AuthorizationServer
import os
from authlib.specs.rfc7519 import jwt
from flask import abort
from functools import wraps
# abort(404)
#from functools import wraps

app = Flask(__name__)
api = Api(app)
#api = flask_restful.Api(app, errors=errors)
errors = {
    'UserAlreadyExistsError': {
        'message': "A user with that username already exists.",
        'status': 409,
    },
    'ResourceDoesNotExist': {
        'message': "A resource with that ID no longer exists.",
        'status': 410,
        'extra': "Any extra information you want.",
    },
    'InvalidCredentials': {
        'message': "Invalid Credentials",
        'status': 401,
        "location": "Authorization",
    }
}


header = {'alg': 'HS256'}
key = 'SECRET'

#https://stackabuse.com/single-page-apps-with-vue-js-and-flask-jwt-authentication/
def authenticate(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        print(request.headers.get('Authorization')[7:]) #Aqui llega
        encoded_token = request.headers.get('Authorization')[7:] #Salta Baerer

        try:
            payload = jwt.decode(encoded_token, key)
        except: #raise RuntimeError('Invalid credentials')
            return errors['InvalidCredentials']
        return func(*args, **kwargs) #Se ejecuta el endpoint'
    return decorated


class Films(Resource):
    #Devuelve 1 sola pelicula si existe
    @authenticate
    def get(self, name):
        #Comprobamos que existe la pelicula
        for film in films:
            if name == film['tittle']:
                return {"GET":film}, 200
        return {"No existe la pelicula":name}

#os.environ['AUTHLIB_INSECURE_TRANSPORT'] = 'true'
# pelicula1 = Filmsq('Avatar', 300)
# print(pelicula1.__dict__)

class ListUsers(Resource):
    def get(self):
        return {"Listado de usuarios":users}

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
            abort(404)


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

# Utilizar la clase models
def pruebaz(name):
    #films.append(filmf)>
    return name

# Clase prueba para ver como controlar los enlaces FUNCIONA
class Hello(Resource):
    def get(self, name):
        return {"Hello":name}
api.add_resource(Hello, '/hello/<name>', endpoint = 'hello')





# def verificar(token):
#     payload = jwt.decode(token, key)
#     for user in users:
#         if user['name'] == payload['name']:
#             return True
#     return False

#No esta en uso
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
api.add_resource(Films, '/films/<name>')
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
