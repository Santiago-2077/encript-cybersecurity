"""Constantes y utilidades compartidas por todos los cifrados."""

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N = len(ALFABETO)


def a_numeros(texto):
    """Convierte cada letra a su numero (A=0 ... Z=25).

    Los espacios se muestran como "|" para separar palabras.
    Cualquier otro simbolo se ignora.
    """
    numeros = []
    for letra in texto.upper():
        if letra in ALFABETO:
            numeros.append(str(ALFABETO.index(letra)))
        elif letra == " ":
            numeros.append("|")
    return " ".join(numeros)
