class growing:
    def __init__(self,plant,stages, days, water, fertilize, plague):
        self.plant=plant
        self.stages=stages
        self.days=days
        self.water=water
        self.fertilize=fertilize
        self.plague=plague
    def sprout(self):
        print("brote joven")
    def develop(self):
        print ("Planta en desarrollo")
    def mature(self):
        print ("Crecimiento completo, lista para cosechar")

