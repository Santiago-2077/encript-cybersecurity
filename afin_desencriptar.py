"""Desencriptacion Afin.

Formula: D(y) = a^-1 * (y - b) mod 26

- y    = numero de la letra encriptada
- a^-1 = inverso modular de a (el numero que cumple a * a^-1 mod 26 = 1)
- b    = desplazamiento usado al encriptar

Opciones:
1. Ingresar a y b
2. Fuerza bruta: probar las 312 combinaciones (12 valores de a x 26 de b)
   y sugerir las mas inteligibles
"""

from math import gcd, log

from alfabeto import ALFABETO, N, a_numeros

# valores de a que tienen inverso modulo 26
A_VALIDOS = [a for a in range(1, N) if gcd(a, N) == 1]

# frecuencia aproximada (%) de cada letra en textos en espanol
FRECUENCIAS = {
    "A": 12.53, "B": 1.42, "C": 4.68, "D": 5.86, "E": 13.68, "F": 0.69,
    "G": 1.01, "H": 0.70, "I": 6.25, "J": 0.44, "K": 0.02, "L": 4.97,
    "M": 3.15, "N": 6.71, "O": 8.68, "P": 2.51, "Q": 0.88, "R": 6.87,
    "S": 7.98, "T": 4.63, "U": 3.93, "V": 0.90, "W": 0.01, "X": 0.22,
    "Y": 0.90, "Z": 0.52,
}


def puntaje(texto):
    """Mientras mas alto, mas se parece el texto al espanol.

    Suma el logaritmo de la frecuencia de cada letra: las letras raras
    (K, W, X...) restan mucho, las comunes (E, A, O...) restan poco.
    """
    return sum(log(FRECUENCIAS[letra]) for letra in texto if letra in FRECUENCIAS)


def inverso_modular(a):
    """Devuelve a^-1 tal que (a * a^-1) mod 26 = 1."""
    for i in range(1, N):
        if (a * i) % N == 1:
            return i
    raise ValueError(f"{a} no tiene inverso modulo {N}")


def descifrado_afin(texto, a, b):
    a_inv = inverso_modular(a)
    resultado = ""
    for letra in texto.upper():
        if letra in ALFABETO:
            y = ALFABETO.index(letra)      # numero de la letra encriptada
            x = (a_inv * (y - b)) % N      # formula a^-1 (y - b) mod 26
            resultado += ALFABETO[x]       # letra original
        else:
            resultado += letra
    return resultado


def fuerza_bruta(texto_cifrado, top=5):
    """Prueba todas las claves (a, b) y devuelve las 'top' mas probables."""
    intentos = []
    for a in A_VALIDOS:
        for b in range(N):
            intento = descifrado_afin(texto_cifrado, a, b)
            intentos.append((puntaje(intento), a, b, intento))
    intentos.sort(key=lambda t: t[0], reverse=True)
    return intentos[:top]


def main():
    print("===== DESENCRIPTACION AFIN =====")
    texto_cifrado = input("Ingresa el texto encriptado: ")
    print("Texto encriptado:    ", texto_cifrado.upper())
    print("Num encriptado:      ", a_numeros(texto_cifrado))
    print()
    print("1) Ingresar a y b")
    print(f"2) Probar todas las posibilidades (fuerza bruta, {len(A_VALIDOS) * N} claves)")
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        a_des = int(input("Ingresa a (coprimo con 26): "))
        while gcd(a_des, N) != 1:
            print("Error: 'a' debe ser coprimo con 26. Valores validos: 1,3,5,7,9,11,15,17,19,21,23,25")
            a_des = int(input("Ingresa a (coprimo con 26): "))
        b_des = int(input("Ingresa b: "))
        print(f"Inverso de a:         {inverso_modular(a_des)}")
        desencriptado = descifrado_afin(texto_cifrado, a_des, b_des)
        print("Num desencriptado:   ", a_numeros(desencriptado))
        print("Texto desencriptado: ", desencriptado)
    elif opcion == "2":
        candidatos = fuerza_bruta(texto_cifrado)
        print()
        print("Candidatos mas probables:")
        for pts, a, b, intento in candidatos:
            print(f"a = {a:2d}, b = {b:2d} (puntaje {pts:7.2f}): {intento}")
        _, mejor_a, mejor_b, probable = candidatos[0]
        print()
        print(f"Mas probable: a = {mejor_a}, b = {mejor_b}")
        print("Num desencriptado:   ", a_numeros(probable))
        print("Texto desencriptado: ", probable)
    else:
        print("Opcion no valida")


if __name__ == "__main__":
    main()
