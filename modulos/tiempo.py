def pasar_tiempo(tiempo):
    tiempo += 1
    return tiempo


def pasar_dia(tiempo):
    if tiempo == 24:
        tiempo = 6
    return tiempo


def ir_dormir(tiempo):
    tiempo = 24
    return tiempo
