


def multiplica(func):
    def decorated(*args, **kwargs):
        result = 4*4
        print(result)
        return func(*args, **kwargs)
    return decorated

@multiplica
def suma(a, b):
    result = a+b
    return print(result)


suma(4,1)





class Persona():

    def __init__(self, nom, apll):
        self.nombre = nom
        self.apellido = apll

    def imprimir(self):
        print("Nombre: %s" % (self.nombre))


p1 = Persona("Pepe", "Sanchez")
p2 = Persona("Juan", "Rodriguez")

Persona.imprimir(p1)

if __name__ == "__main__":
    pass
