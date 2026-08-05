#Lizett Velandia
#Ejercicio Librería Números Complejos
#Julio 29 de 2026

import math


def suma(complejo1, complejo2):
    parte_real = complejo1[0] + complejo2[0]
    parte_imaginaria = complejo1[1] + complejo2[1]
    return (parte_real, parte_imaginaria)


def producto(complejo1, complejo2):
    parte_real = (complejo1[0] * complejo2[0]) - (complejo1[1] * complejo2[1])
    parte_imaginaria = (complejo1[0] * complejo2[1]) + (complejo1[1] * complejo2[0])
    return (parte_real, parte_imaginaria)


def resta(complejo1, complejo2):
    parte_real = complejo1[0] - complejo2[0]
    parte_imaginaria = complejo1[1] - complejo2[1]
    return (parte_real, parte_imaginaria)


def division(complejo1, complejo2):
    divisor = complejo2[0] ** 2 + complejo2[1] ** 2

    if divisor == 0:
        return None

    parte_real = ((complejo1[0] * complejo2[0]) + (complejo1[1] * complejo2[1])) / divisor
    parte_imaginaria = ((complejo2[0] * complejo1[1]) - (complejo1[0] * complejo2[1])) / divisor

    return (parte_real, parte_imaginaria)


def modulo(complejo):
    return math.sqrt(complejo[0] ** 2 + complejo[1] ** 2)


def conjugado(complejo):
    parte_real = complejo[0]
    parte_imaginaria = -complejo[1]
    return (parte_real, parte_imaginaria)


def polar_a_cartesiano(complejo_polar):
    magnitud = complejo_polar[0]
    angulo = complejo_polar[1]

    parte_real = magnitud * math.cos(angulo)
    parte_imaginaria = magnitud * math.sin(angulo)

    return (parte_real, parte_imaginaria)


def cartesiano_a_polar(complejo):
    magnitud = modulo(complejo)
    angulo = fase(complejo)

    return (magnitud, angulo)


def fase(complejo):
    return math.atan2(complejo[1], complejo[0])


def main():
    complejo1 = (1, 1)
    complejo2 = (5, -2)

    print(suma(complejo1, complejo2))
    print(producto(complejo1, complejo2))



if __name__ == "__main__":
    main()
