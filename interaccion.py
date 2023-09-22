from animales import Vaca
from tiempo import RepeatTimer


def main():
    print('                         ')
    print('                         ')
    print('Bienvenido al simulador de granaja')
    print('                         ')
    nombre = input('Ingrese El nombre Del animal: ')
    print('                         ')
    animal1 = Vaca(nombre)

    timer = RepeatTimer(3, animal1.respirar)
    timer.start()

    timer = RepeatTimer(30, animal1.años)
    timer.start()

    timer = RepeatTimer(5, animal1.happy)
    timer.start()

    while True:                            #MENU PRINCIPAL
        print('                         ')
        print('                         ')
        print('Animales de mi Granaja: ')
        print('Nombre: ', animal1.nombre)
        print('1 - Estadisticas del animal ')
        print('2 - Alimentar al animal ')
        print('3 - Acariciar al animal ')
        print('4 - Curar al animal ')
        opcion = int(input('Ingrese una opcion:  '))
        print('                         ')
        
        if opcion == 1:
            print('                         ')
            print('ESTADISTICAS DE MI MASCOTA:') #OPCION 1
            print('                         ')
            print('Animal No. 1: ')
            print('Nombre: ', animal1.nombre)
            print('Salud', animal1.salud)
            print('Felicidad ', animal1.felicidad)
            print('Energia ', animal1.energia )
            print('                         ')

        if opcion == 2:
            while True:
                print('                         ')
                print('ALIMENTAR A LA VACA:')   #OPCION 2
                print('                         ')
                print('1 - Consentrado. ')
                print('2 - Cesped. ')
                print('3 - Regresar al menú principal.')
                print('                         ')
                opcion = int(input('Elija una opcion:  '))
                print('                         ')
                if opcion == 1:
                    animal1.concentrado()
                if opcion == 2:
                    animal1.cesped()
                if opcion == 3:
                    break

        if opcion == 3:
            animal1.acariciar() #OPCION 3
            
            
        if opcion == 4:
            while True:
                print('                         ')
                print('CURAR A MI MASCOTA:')  #OPCION 4
                print('                         ')
                print('1 - Vitamina.  ')
                print('2 - Jarabe para la tos. ')
                print('3 - Vacuna. ')
                print('4 - Regresar al menú principal. ')
                opcion = int(input('Ingrese una opcion'))
                print('                         ')
                if opcion == 1:
                    animal1.vitamina()
                if opcion == 2:
                    animal1.jarabe()
                if opcion == 3:
                    animal1.vacuna()
                if opcion == 4:
                    break
                    
        if opcion == 5:
            break

main()
