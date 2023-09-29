
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
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

    # ACARICIAR AL ANIMAL
    def happy(self):
        if self.felicidad > 0:
            self.felicidad -= 2
    
    def acariciar(self):
        if self.felicidad > 0:
            self.felicidad += 2

    # ENFERMEDADES DEL ANIMAL
    def enfermedad(self):
        if self.felicidad == 0:
            self.salud -= 5
            self.energia -= 10
    
    # PRODUCCION DEL ANIMAL
    def produccion(self):
        if self.salud < 100:
            self.produccion -= 20
        else:
            if self.salud == 0:
                self.produccion == 100 


    # EDAD DEL ANIMAL
    def años(self):
        if self.edad == 0:
            self.edad +=1

            
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
                self.salud +=5


    #CURAR AL ANIMAL

    def vitamina(self):
        if self.salud >= 0:
            self.salud += 5

    def jar(self):
        if self.salud >= 0:
            self.salud += 20

    def vacuna(self):
        if self.salud >= 0:
            self.salud += 50

