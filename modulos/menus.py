import animales
import personaje

dia = 0
mes = 0
anio = 0
carisias = False


def menu_bienvenida():
    print("------------------------------------------")
    print("|                                        |")
    print("|  Hola, bienvenido a GranjitaSimulator  |")
    print("|                    :3                  |")
    print("__________________________________________")
    print("|                                        |")
    print("|            Crea tu personaje:          |")
    persona = personaje.Personaje()
    print("|     Iniciaras con un animal, puede     |\n"
          "|     comprar mas cosas en la tienda     |")
    print("------------------------------------------")
    animal = animales.Animales()

    persona.animales.append(animal)

    return persona


jugador = menu_bienvenida()


def menu_pricipal():
    print("------------------------------------------")
    print("|          ¿Que quiere hacer?:           |")
    print("------------------------------------------")
    print("|          1.Ver a los animales          |")
    print("|          2.Ver a las plantas           |")
    print("|          3.Ir a la tienda              |")
    print("|          4.Pasar al dia siguiente      |")
    print("|          5.Salir                       |")
    print("------------------------------------------")

    opcion = input("Escoja la opcion que desea(1/2/3/4): ")

    print()

    if opcion == '1':
        menu_animales()
    elif opcion == '2':
        pass
        print("Aun no disponible :D.")
    elif opcion == '3':
        menu_tienda()
    elif opcion == '4':
        return 1000
    elif opcion == '5':
        exit()
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")


def menu_tienda():
    global jugador
    while True:
        print("------------------------------------------")
        print("|          ¿Que quiere hacer?:           |")
        print("------------------------------------------")
        print("|         1.Comprar animales - $100      |")
        print("|         2.Comprar semillas - $20       |")
        print("|         3.Ver las mejoras              |")
        print("|         4.Vender objetos               |")
        print("|         5.Regresar al menu             |")
        print("------------------------------------------")

        opcion = input("Escoja la opcion que desea(1/2/3/4): ")

        print()

        if opcion == '1':
            if jugador.dinero > 100:
                animal = animales.Animales()
                jugador.animales.append(animal)
            else:
                print("Dinero insuficiente. ):")

        elif opcion == '2':
            pass

        elif opcion == '3':
            print("------------------------------------------------------")
            print("|                 Mejoras disponibles:               |\n"
                  "|   1.Mejora de produccion de animales - 1 Moneda    |\n"
                  "|   2.Mejora de cuidado de animales - 1 Moneda       |\n"
                  "|   3.Mejora de produccion de plantas - 1 Moneda     |\n"
                  "|   4.Mejora de cuidado de plantas - 1 Moneda        |   ")
            print("------------------------------------------------------")

            opcion_sub = input("Escoja la opcion que desea(1/2/3/4): ")

            if opcion_sub == "1":
                jugador.animales_mejora_1 = True
                jugador.dinero -= 1
            elif opcion_sub == "2":
                jugador.animales_mejora_2 = True
                jugador.dinero -= 1
            elif opcion_sub == "3":
                jugador.cultivos_mejora_1 = True
                jugador.dinero -= 1
            elif opcion_sub == "4":
                jugador.cultivos_mejora_2 = True
                jugador.dinero -= 1

        elif opcion == '4':
            objetos = int(len(jugador.objetos)) * 20
            jugador.dinero += objetos
            for i in range(0, len(jugador.objetos)):
                del jugador.objetos[i]

            print(f"Ha vendido sus objetos a {objetos} monedas.")

        elif opcion == '5':
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")


def menu_animales():
    global jugador

    while True:  # MENU PRINCIPAL
        print("------------------------------------------")
        print('|         Animales de mi Granaja:        |')
        for i in jugador.animales:
            print(f"               {i.nombre}-{i.tipo}")
        print("------------------------------------------")
        print('|      1 - Estadisticas del animal       |')
        print('|      2 - Alimentar al animal           |')
        print('|      3 - Acariciar al animal           |')
        print('|      4 - Curar al animal               |')
        print('|      5 - Regresar al menu principal    |')
        opcion = int(input('Ingrese una opcion:  '))
        print("------------------------------------------")

        if opcion == 1:
            contador = 0
            for i in jugador.animales:
                contador += 1
                print("------------------------------------------")
                print('|      ESTADISTICAS DE MI MASCOTA:       |')  # OPCION 1
                print("------------------------------------------")
                print(f'               Animal No.{contador}:         ')
                print(f'           Nombre: {i.nombre}              ')
                print(f'           Salud: {i.salud}                ')
                print(f'           Felicidad: {i.felicidad}        ')
                print(f'           Energia: {i.energia}            ')
                print(f'           Tipo: {i.tipo}                  ')
                print("------------------------------------------")

        if opcion == 2:
            while True:
                print("------------------------------------------")
                print('|           ALIMENTAR A LA VACA:          |')  # OPCION 2
                print("------------------------------------------")
                print('|          1 - Consentrado - $10          |')
                print('|          2 - Cesped - $5                |')
                print('|          3 - Regresar al menú.          |')
                print("------------------------------------------")
                opcionsub = int(input('Elija una opcion:  '))
                print('                         ')
                if opcionsub == 1:
                    for i in range(0, len(jugador.animales)):
                        if jugador.dinero > 10:
                            jugador.dinero -= 10
                            jugador.animales[i].concentrado()
                            print(f"Se ha alimentado a {jugador.animales[i].nombre} con concentrado.")
                        else:
                            print("Dinero insuficiente. ):")
                if opcionsub == 2:
                    for i in range(0, len(jugador.animales)):
                        if jugador.dinero > 5:
                            jugador.dinero -= 5
                            print("Se ha alimentado con cesped.")
                            jugador.animales[i].concentrado()
                        else:
                            print("Dinero insuficiente. ):")
                if opcionsub == 3:
                    break

        if opcion == 3:
            global carisias
            carisiaas = carisias
            if not carisiaas:
                for i in range(0, len(jugador.animales)):
                    jugador.animales[i].acariciar()
                    carisias = True
                    print(f"Has acariciado a {jugador.animales[i].nombre}")

            else:
                print("Ya has acariciado a los animales hoy :D.")

        if opcion == 4:
            while True:
                print("------------------------------------------")
                print('|           CURAR A MI MASCOTA:          |')  # OPCION 4
                print("------------------------------------------")
                print('|           1 - Vitamina - $5            |')
                print('|           2 - Jarabe - $10             |')
                print('|           3 - Vacuna - $20             |')
                print('|           4 - Regresar al menú.        |')
                print("------------------------------------------")

                opcionsub = int(input('Ingrese una opcion'))
                print('                         ')
                if opcionsub == 1:
                    for i in range(0, len(jugador.animales)):
                        if jugador.dinero > 5:
                            jugador.dinero -= 5
                            jugador.animales[i].vitamina()
                            print(f"Se ha curado a {jugador.animales[i].nombre} con vitaminas.")
                        else:
                            print("Dinero insuficiente. ):")

                if opcionsub == 2:
                    for i in range(0, len(jugador.animales)):
                        if jugador.dinero > 10:
                            jugador.dinero -= 10
                            jugador.animales[i].jarabe()
                            print(f"Se ha curado a {jugador.animales[i].nombre} con jarabe.")
                        else:
                            print("Dinero insuficiente. ):")

                if opcionsub == 3:
                    for i in range(0, len(jugador.animales)):
                        if jugador.dinero > 20:
                            jugador.dinero -= 20
                            jugador.animales[i].vacuna()
                            print(f"Se ha curado a {jugador.animales[i].nombre} con vacunas.")
                        else:
                            print("Dinero insuficiente. ):")
                if opcionsub == 4:
                    break

        if opcion == 5:
            break


def juego_principal():
    global dia, mes, anio

    horas = 6

    # Ciclo del juego infinito
    while True:
        global carisias
        carisias = False
        # Ciclo de un dia
        while horas < 24:
            for i in range(0, len(jugador.animales)):
                jugador.animales[i].salud -= 20
                jugador.animales[i].energia -= 20
                jugador.animales[i].felicidad -= 20
                jugador.animales[i].respirar()

                if jugador.animales[i].muerto:
                    del jugador.animales[i]
                if jugador.animales[i].felicidad > 50:
                    jugador.objetos.append(jugador.animales[i].producir())
                    print(f"{jugador.animales[i].nombre} - {jugador.animales[i].tipo} "
                          f"ha producido algo hoy. :)")
                else:
                    print(f"{jugador.animales[i].nombre} - {jugador.animales[i].tipo} "
                          f"esta tan triste que no puede porducir. ):")

            print(f"\n\nJugador: {jugador.nombre} Dinero: {jugador.dinero} Fecha: {dia}/{mes}/{anio} Hora: {horas}")
            menu_pricipal()
        dia += 1

        # Ciclo de un mes
        if dia == 24:
            dia = 0
            mes += 1

        # Ciclo de un anio
        if mes == 12:
            mes = 10
            anio += 1


juego_principal()
