"""Desencriptacion Cesar.

Formula: P = (C - K) mod 26

Opciones:
1. Ingresar K
2. Fuerza bruta: probar las 26 posibilidades y sugerir la mas inteligible
"""

from alfabeto import ALFABETO, N, a_numeros

# letras mas comunes en espanol, se usan para sugerir el resultado mas probable
FRECUENTES = "EAOSRNIDLCTU"


def descifrado_cesar(texto, k):
    resultado = ""
    for letra in texto.upper():
        if letra in ALFABETO:
            c = ALFABETO.index(letra)
            p = (c - k) % N
            resultado += ALFABETO[p]
        else:
            resultado += letra
    return resultado


def puntaje(texto):
    return sum(1 for letra in texto if letra in FRECUENTES)


def fuerza_bruta(texto_cifrado):
    """Prueba las 26 claves, imprime cada intento y devuelve la K mas probable."""
    mejor_k = 0
    mejor_puntaje = -1
    for k in range(N):
        intento = descifrado_cesar(texto_cifrado, k)
        print(f"K = {k:2d}: {intento}")
        if puntaje(intento) > mejor_puntaje:
            mejor_puntaje = puntaje(intento)
            mejor_k = k
    return mejor_k


def main():
    print("===== DESENCRIPTACION CESAR =====")
    texto_cifrado = input("Ingresa el texto encriptado: ")
    print("Texto encriptado:    ", texto_cifrado.upper())
    print("Num encriptado:      ", a_numeros(texto_cifrado))
    print()
    print("1) Ingresar K")
    print("2) Probar todas las posibilidades (fuerza bruta)")
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        k_des = int(input("Ingresa K: "))
        desencriptado = descifrado_cesar(texto_cifrado, k_des)
        print("Num desencriptado:   ", a_numeros(desencriptado))
        print("Texto desencriptado: ", desencriptado)
    elif opcion == "2":
        mejor_k = fuerza_bruta(texto_cifrado)
        probable = descifrado_cesar(texto_cifrado, mejor_k)
        print()
        print(f"Mas probable: K = {mejor_k}")
        print("Num desencriptado:   ", a_numeros(probable))
        print("Texto desencriptado: ", probable)
    else:
        print("Opcion no valida")


if __name__ == "__main__":
    main()
