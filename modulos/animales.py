class Animales:
    def __init__(self):
        self.produccion = ""
        self.tipo = self.tipo_animal()
        self.nombre = input("¿Cual es el nombre del animal?: ")
        self.edad = 0
        self.salud = 100
        self.energia = 100
        self.felicidad = 100

    # RESPIRACION DEL ANIMAL
    def respirar(self):
        if self.energia > 0:
            self.energia -= 1
        else:
            if self.salud <= 0:
                print('Estoy muerto...')
            else:
                self.salud -= 2

    # ACARICIAR AL ANIMAL
    def happy(self):
        if self.felicidad > 0:
            self.felicidad -= 2
    
    def acariciar(self):
        if self.felicidad > 0:
            self.felicidad += 2

    # EDAD DEL ANIMAL
    def anios(self):
        if self.edad == 0:
            self.edad += 1
            
    # ALIMENTAR A EL ANIMAL
    def concentrado(self):
        if self.energia >= 0:
            self.energia += 5
            if self.salud >= 0:
                self.salud += 1

    def cesped(self):
        if self.energia >= 0:
            self.energia += 20
            if self.salud >= 0:
                self.salud += 5

    # CURAR AL ANIMAL
    def vitamina(self):
        if self.salud >= 0:
            self.salud += 5

    def jar(self):
        if self.salud >= 0:
            self.salud += 20

    def vacuna(self):
        if self.salud >= 0:
            self.salud += 50

    def __str__(self):
        return f"El Nombre de la Vaca es: {self.nombre}"

    def tipo_animal(self):
        tipo = input("¿Que tipo de animal quiere comprar?: "
                     "\n1.Vaca"
                     "\n2.Gallina"
                     "\n3.Oveja"
                     "\nEscoja un tipo(1 o 2 o 3): ")

        if tipo == "1":
            self.produccion = "Leche"
            return "Vaca"
        elif tipo == "2":
            self.produccion = "Huevos"
            return "Gallina"
        elif tipo == "3":
            self.produccion = "Lana"
            return "Oveja"
