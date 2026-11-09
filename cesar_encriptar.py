"""Encriptacion Cesar.

Formula: C = (P + K) mod 26
"""

from alfabeto import ALFABETO, N, a_numeros


def cifrado_cesar(texto, k):
    resultado = ""
    for letra in texto.upper():
        if letra in ALFABETO:
            p = ALFABETO.index(letra)
            c = (p + k) % N
            resultado += ALFABETO[c]
        else:
            resultado += letra  # espacios y simbolos se quedan igual
    return resultado


def main():
    print("===== ENCRIPTACION CESAR =====")
    k_cesar = int(input("Ingresa K: "))
    texto_cesar = input("Ingresa la(s) palabra(s) a encriptar: ")
    encriptado = cifrado_cesar(texto_cesar, k_cesar)
    print("Texto original:   ", texto_cesar.upper())
    print("Num original:     ", a_numeros(texto_cesar))
    print("Num encriptado:   ", a_numeros(encriptado))
    print("Texto encriptado: ", encriptado)


if __name__ == "__main__":
    main()
