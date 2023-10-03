class Animales:
    def __init__(self):
        self.produccion = 0
        self.tipo = self.tipo_animal()
        self.nombre = input("¿Cual es el nombre del animal?: ")
        self.edad = 0
        self.salud = 100
        self.energia = 100
        self.felicidad = 100
        self.muerto = False

    # RESPIRACION DEL ANIMAL
    def respirar(self):
        if self.energia > 0:
            self.energia -= 10
        else:
            if self.salud <= 0:
                self.muerto = True
                print(f"{self.nombre} - {self.tipo} ha muerto.")

    # ACARICIAR AL ANIMAL
    def happy(self):
        if self.felicidad > 0:
            self.felicidad -= 2

    def acariciar(self):
        if self.felicidad > 0:
            self.felicidad += 40

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
        print("------------------------------------------")
        tipo = input("|      ¿Que tipo de animal quiere?:      |"
                     "\n|                1.Vaca.                 |"
                     "\n|                2.Gallina.              |"
                     "\n|                3.Oveja.                |"
                     "\n        Escoja un tipo(1 o 2 o 3): ")
        print("------------------------------------------")

        if tipo == "1":
            self.produccion = "Leche"
            return "Vaca"
        elif tipo == "2":
            self.produccion = "Huevos"
            return "Gallina"
        elif tipo == "3":
            self.produccion = "Lana"
            return "Oveja"

    def producir(self):
        return self.produccion
