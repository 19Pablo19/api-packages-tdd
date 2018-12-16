#Clase para las peliculas
class Filmsq():
    def __init__(self,name, quantity):
        self.name = name
        self.quantity = quantity

    def p(self):
        cadena = {'name':self.name, 'quantity':self.quantity}
        return cadena
