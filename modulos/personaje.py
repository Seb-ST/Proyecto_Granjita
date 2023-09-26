class Personaje:
    def __init__(self):
        print("|                                        |")
        self.nombre = input("|          ¿Cual es tu nombre?:          |\n                  ")
        print("__________________________________________")
        print("|      Iniciaras con 100 monedas :3      |")
        self.dinero = 100
        self.vacas = {}
        self.gallinas = {}
        self.ovejas = {}
