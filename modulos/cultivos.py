import random


class Growing:
    def __init__(self):
        self.plant = self.tipe_plant()
        self.days = self.days_time()
        self.water = False
        self.fertilize = False
        self.estate = "Semilla"
        self.live = False
        self.plaguein = False

    def tipe_plant(self):
        print("------------------------------------------")
        tipo = input("|          ¿Que semilla quiere?:         |"
                     "\n|               1.Trigo.                 |"
                     "\n|               2.Remolocha.             |"
                     "\n|               3.Zanahoria.             |"
                     "\n|               4.Coliflor.              |"
                     "\n|               5.Brocoli.               |"
                     "\n        Escoja un tipo(1 o 2 o 3): ")
        print("------------------------------------------")

        if tipo == "1":
            return "Trigo"
        elif tipo == "2":
            return "Remolacha"
        elif tipo == "3":
            return "Zanahoria"
        elif tipo == "4":
            return "Coliflor"
        elif tipo == "5":
            return "Brocoli"

    def days_time(self):
        if self.plant == "Trigo":
            return 4
        elif self.plant == "Remolacha":
            return 6
        elif self.plant == "Zanahoria":
            return 10
        elif self.plant == "Coliflor":
            return 15
        elif self.plant == "Brocoli":
            return 15

    def health(self):
        self.water = True

    def fert(self):
        if self.fertilize:
            self.days -= 1

    def passtime(self):
        self.water = False
        self.fertilize = False

    def die(self):
        if self.water < 0:
            print(f"Planta {self.plant} esta seca y ha muerto.")
            self.live = False

    def plague(self):
        plaga = random.randint(0, 100000)

        if plaga == 1:
            self.plaguein = True

    def produce(self):
        if self.days <= 0:
            self.estate = "Maduro y listo para cosechar :)."

    def estate_change(self):
        if self.days // 2 == 0 and self.days > 0:
            self.estate = "Brote"
