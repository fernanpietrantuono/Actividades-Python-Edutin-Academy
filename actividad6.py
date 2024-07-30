class Persona:
    def __init__(self):
        self.nombre = input("Ingresá tu nombre: ")
        self.edad = input("Ingresá tu edad: ")

    def imprimir(self):
        print(f'Nombre: {self.nombre}')
        print(f'Edad: {self.edad}')


class Ciudadano(Persona):
    def __init__(self):
        super().__init__()
        self.deposito = float(input("Ingresá el dinero a depositar: "))

    def imprimir(self):
        super().imprimir()
        print(f'Depósito: U$S {self.deposito}')

    def impuestos(self):
        if self.deposito > 4000:
            print(f'El/la ciudadano/a {self.nombre} debe pagar los impuestos')
        else:
            print(f'El/la ciudadano/a {self.nombre} no debe pagar los impuestos')


# Instancias
ciudadano1 = Ciudadano()
ciudadano1.imprimir()
ciudadano1.impuestos()

"""
Estado financiero de los siguientes ciudadanos:

Manuel Chima, de 25 años de edad, debe pagar los impuestos
Fayle García, de 56 años de edad, no debe pagar los impuestos
Lesly Rodríguez, de 34 años de edad, debe pagar los impuestos
Mario Herrera, de 45 años de edad, no debe pagar los impuestos
"""
