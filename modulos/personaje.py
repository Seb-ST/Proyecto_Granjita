class Personaje:
    def __init__(self):
        print("|                                        |")
        self.nombre = input("|          ¿Cual es tu nombre?:          |\n                  ")
        print("__________________________________________")
        print("|      Iniciaras con 100 monedas :3      |")
        self.dinero = 100
        self.animales = []
        self.cultivos = []
        self.objetos = []
        self.animales_mejora_1 = False
        self.animales_mejora_2 = False
        self.cultivos_mejora_1 = False
        self.cultivos_mejora_2 = False
