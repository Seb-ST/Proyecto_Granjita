import animales
import personaje

dia = 0
mes = 0
anio = 0


def menu_bienvenida():
    print("------------------------------------------")
    print("|                                        |")
    print("|  Hola, bienvenido a GranjitaSimulator  |")
    print("|                    :3                  |")
    print("__________________________________________")
    print("|                                        |")
    print("|            Crea tu personaje:          |")
    jugador = personaje.Personaje()
    print("|     Iniciaras con un animal, puede     |\n"
          "|     comprar mas cosas en la tienda     |")
    print("------------------------------------------")
    animal = animales.Animales()

    jugador.animales.append(animal)

    return jugador


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
        print("|          1.Comprar animales            |")
        print("|          2.Comprar semillas            |")
        print("|          3.Ver las mejoras             |")
        print("|          4.Vender objetos              |")
        print("|          5.Regresar al menu            |")
        print("------------------------------------------")

        opcion = input("Escoja la opcion que desea(1/2/3/4): ")

        print()

        if opcion == '1':
            animal = animales.Animales()
            jugador.animales.append(animal)

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
            objetos = int(len(jugador.objetos)) * 10
            jugador.dinero += objetos

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
            for i in jugador.animales:
                while True:
                    print("------------------------------------------")
                    print('|           ALIMENTAR A LA VACA:          |')  # OPCION 2
                    print("------------------------------------------")
                    print('|           1 - Consentrado.              |')
                    print('|           2 - Cesped.                   |')
                    print('|           3 - Regresar al menú.         |')
                    print("------------------------------------------")
                    opcion = int(input('Elija una opcion:  '))
                    print('                         ')
                    if opcion == 1:
                        i.concentrado()
                    if opcion == 2:
                        i.cesped()
                    if opcion == 3:
                        break

        if opcion == 3:
            for i in jugador.animales:
                i.acariciar()  # OPCION 3

        if opcion == 4:
            for i in jugador.animales:
                while True:
                    print("------------------------------------------")
                    print('|           CURAR A MI MASCOTA:          |')  # OPCION 4
                    print("------------------------------------------")
                    print('|           1 - Vitamina.                |')
                    print('|           2 - Jarabe.                  |')
                    print('|           3 - Vacuna.                  |')
                    print('|           4 - Regresar al menú.        |')
                    print("------------------------------------------")

                    opcion = int(input('Ingrese una opcion'))
                    print('                         ')
                    if opcion == 1:
                        i.vitamina()
                    if opcion == 2:
                        i.jarabe()
                    if opcion == 3:
                        i.vacuna()
                    if opcion == 4:
                        break

        if opcion == 5:
            break


def juego_principal():
    global dia, mes, anio

    horas = 6

    # Ciclo del juego infinito
    while True:
        # Ciclo de un dia
        while horas < 24:
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
