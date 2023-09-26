import personaje
import animales

tiempo = 0
jugador = ""


def pasar_tiempo():
    global tiempo
    tiempo += 1


def bienvenida():
    global jugador
    print("__________________________________________")
    print("|                                        |")
    print("|  Hola, bienvenido a GranjitaSimulator  |")
    print("|                    :3                  |")
    print("__________________________________________")
    print("|                                        |")
    print("|            Crea tu personaje:          |")
    jugador = personaje.Personaje()
    print("|     Iniciaras con un animal, puede     |\n"
          "|     comprar mas cosas en la tienda     |")
    print("__________________________________________")
    animal = animales.Animales()

    if animal.tipo == "Vaca":
        jugador.vacas[animal.nombre] = animal
    elif animal.tipo == "Gallina":
        jugador.gallinas[animal.nombre] = animal
    elif animal.tipo == "Oveja":
        jugador.ovejas[animal.nombre] = animal


bienvenida()
