"""Encriptacion Afin.

Formula: E(x) = (a * x + b) mod 26

- x = numero de la letra original (A=0, B=1, ..., Z=25)
- a = multiplicador, debe ser coprimo con 26 (1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25)
- b = desplazamiento (lo que se suma)
- El resultado es el numero de la letra encriptada
"""

from math import gcd

from alfabeto import ALFABETO, N, a_numeros


def cifrado_afin(texto, a, b):
    resultado = ""
    for letra in texto.upper():
        if letra in ALFABETO:
            x = ALFABETO.index(letra)    # numero de la letra original
            e = (a * x + b) % N          # formula (ax + b) mod 26
            resultado += ALFABETO[e]     # letra encriptada
        else:
            resultado += letra
    return resultado


def main():
    print("===== ENCRIPTACION AFIN =====")
    a_afin = int(input("Ingresa a (coprimo con 26): "))
    while gcd(a_afin, N) != 1:
        print("Error: 'a' debe ser coprimo con 26. Valores validos: 1,3,5,7,9,11,15,17,19,21,23,25")
        a_afin = int(input("Ingresa a (coprimo con 26): "))
    b_afin = int(input("Ingresa b: "))
    texto_afin = input("Ingresa la(s) palabra(s) a encriptar: ")
    encriptado = cifrado_afin(texto_afin, a_afin, b_afin)
    print("Texto original:   ", texto_afin.upper())
    print("Num original:     ", a_numeros(texto_afin))
    print("Num encriptado:   ", a_numeros(encriptado))
    print("Texto encriptado: ", encriptado)


if __name__ == "__main__":
    main()
