class growing:
    def __init__(self,plant, days, water, fertilize):
        self.plant=plant
        self.days=days
        self.water= 0
        self.fertilize=0
    def health(self):
        regar=input("Presione w para regar la planta: ")
        while self.water<=10:
            if regar=="W" or regar == "W":
                self.water=self.water+2
    def fert(self):
        fertilizante=input("Presione f para darle fertilizante a la planta: ")
        while self.fertilize<=10:
            if fertilizante=="f" or fertilizante == "F":
                self.water=self.water+2
    def passtime(self):
        self.water=self.water-2
        self.fertilize=self.fertilize-2
    def die(self):
        if self.water<0:
            print ("Planta seca, presione x para eliminarla")

    def plague(self):
        if self.days in range (0,10,3):
            insecticida=input("Tu planta tiene una plaga, eliminela por favor presionando i")
            if insecticida == "i" or insecticida == "I":
                print ("La plaga se ha ido")


class wheat(growing):
    def __init__(self,plant,days,):
        super().__init__(plant,days)
    def sprout(self):
        if self.days>=0 and self.days <5:
            print ("Brote")
    def develop (self):
        if self.days>=5 and self.days <10:
            print ("Planta en desarrollo")
    def mature (self):
        if self.days>=5 and self.days <10:
            print ("Planta lista para cosechar")
class rice(growing):
    def __init__(self,plant,days,):
        super().__init__(plant,days)
    def sprout(self):
        if self.days>=0 and self.days <3:
            print ("Brote")
    def develop (self):
        if self.days>=3 and self.days <4:
            print ("Planta en desarrollo")
    def mature (self):
        if self.days>=4 and self.days <8:
            print ("Planta lista para cosechar")

class corn(growing):
    def __init__(self,plant,days,):
        super().__init__(plant,days)
    def sprout(self):
        if self.days>=0 and self.days <15:
            print ("Brote")
    def develop (self):
        if self.days>=15 and self.days <30:
            print ("Planta en desarrollo")
    def mature (self):
        if self.days>=30 and self.days <60:
            print ("Planta lista para cosechar")

