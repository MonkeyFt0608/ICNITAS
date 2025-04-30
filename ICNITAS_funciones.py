# ICNITAS_funciones.py

def calcular_altura(longitud_huella, profundidad_huella, tipo_fosil):
    if tipo_fosil == 'dinosaurio_bipedo':
        return (longitud_huella * 7.5) + (profundidad_huella * 2.5)
    elif tipo_fosil == 'dinosaurio_cuadrupedo':
        return (longitud_huella * 5) + (profundidad_huella * 2)
    elif tipo_fosil == 'mamifero_fosil':
        return (longitud_huella * 6) + (profundidad_huella * 2)
    else:
        return None

def calcular_peso(longitud_huella, profundidad_huella, tipo_fosil):
    if tipo_fosil == 'dinosaurio_bipedo':
        return (longitud_huella * 3) + (profundidad_huella * 1.5)
    elif tipo_fosil == 'dinosaurio_cuadrupedo':
        return (longitud_huella * 4) + (profundidad_huella * 2)
    elif tipo_fosil == 'mamifero_fosil':
        return (longitud_huella * 2.5) + (profundidad_huella * 1.5)
    else:
        return None

def determinar_epoca_geologica(antiguedad):
    if antiguedad <= 66:
        return "Cenozoico"
    elif antiguedad <= 145:
        return "Cretácico (Mesozoico)"
    elif antiguedad <= 201:
        return "Jurásico (Mesozoico)"
    elif antiguedad <= 252:
        return "Triásico (Mesozoico)"
    elif antiguedad <= 299:
        return "Pérmico (Paleozoico)"
    elif antiguedad <= 359:
        return "Carbonífero (Paleozoico)"
    elif antiguedad <= 419:
        return "Devónico (Paleozoico)"
    elif antiguedad <= 444:
        return "Silúrico (Paleozoico)"
    elif antiguedad <= 485:
        return "Ordovícico (Paleozoico)"
    elif antiguedad <= 541:
        return "Cámbrico (Paleozoico)"
    else:
        return "Precámbrico (antes de 541 millones de años)"