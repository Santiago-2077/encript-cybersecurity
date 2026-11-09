# Encriptación César y Afín

Implementación en Python de dos cifrados clásicos por sustitución: **César** y **Afín**. Incluye encriptación, desencriptación y ataques de fuerza bruta contra ambos.

Cada script muestra el texto como letras y como números (A=0 … Z=25) para ver cómo funciona la aritmética modular paso a paso.

## Requisitos

- Python 3.x
- Sin dependencias externas (solo la librería estándar)

## Estructura

```
encript-cybersecurity/
├── alfabeto.py             # constantes y utilidades compartidas
├── cesar_encriptar.py      # encriptación César
├── cesar_desencriptar.py   # desencriptación César (con K o fuerza bruta)
├── afin_encriptar.py       # encriptación Afín
└── afin_desencriptar.py    # desencriptación Afín (con a y b o fuerza bruta)
```

## Archivos

### `alfabeto.py`

Módulo base que importan los demás scripts.

- `ALFABETO`: las 26 letras del alfabeto inglés (`A`–`Z`).
- `N`: tamaño del alfabeto (26), el módulo de todas las operaciones.
- `a_numeros(texto)`: convierte un texto a su representación numérica. Los espacios se muestran como `|` para separar palabras.

```python
>>> a_numeros("Hola mundo")
'7 14 11 0 | 12 20 13 3 14'
```

### `cesar_encriptar.py`

Desplaza cada letra `K` posiciones en el alfabeto.

**Fórmula:** `C = (P + K) mod 26`

- `P`: número de la letra original
- `K`: clave (desplazamiento)
- `C`: número de la letra encriptada

Los espacios y símbolos no se modifican.

```
$ python3 cesar_encriptar.py
Ingresa K: 3
Ingresa la(s) palabra(s) a encriptar: hola mundo
Texto original:    HOLA MUNDO
Num original:      7 14 11 0 | 12 20 13 3 14
Num encriptado:    10 17 14 3 | 15 23 16 6 17
Texto encriptado:  KROD PXQGR
```

### `cesar_desencriptar.py`

Revierte el cifrado César.

**Fórmula:** `P = (C - K) mod 26`

Ofrece dos modos:

1. **Ingresar K**: si se conoce la clave, desencripta directamente.
2. **Fuerza bruta**: prueba las 26 claves posibles e imprime cada resultado. Para sugerir el más probable, asigna un puntaje a cada intento según cuántas letras frecuentes del español contiene (`E A O S R N I D L C T U`) y elige el de mayor puntaje.

La fuerza bruta funciona porque César solo tiene 26 claves posibles, lo que lo hace trivial de romper.

```
$ python3 cesar_desencriptar.py
Ingresa el texto encriptado: krod pxqgr
...
Elige una opcion: 2
K =  0: KROD PXQGR
K =  1: JQNC OWPFQ
K =  2: IPMB NVOEP
K =  3: HOLA MUNDO
...
Mas probable: K = 3
Texto desencriptado:  HOLA MUNDO
```

### `afin_encriptar.py`

Generaliza César: multiplica y luego desplaza.

**Fórmula:** `E(x) = (a · x + b) mod 26`

- `x`: número de la letra original
- `a`: multiplicador
- `b`: desplazamiento
- `E(x)`: número de la letra encriptada

`a` **debe ser coprimo con 26** (`gcd(a, 26) = 1`). Si no lo es, varias letras terminan en la misma letra cifrada y el mensaje no se puede desencriptar. Valores válidos: `1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25`. El script valida esto y vuelve a pedir `a` si no cumple.

Con `a = 1` el cifrado Afín equivale a César.

```
$ python3 afin_encriptar.py
Ingresa a (coprimo con 26): 5
Ingresa b: 8
Ingresa la(s) palabra(s) a encriptar: hola mundo
Texto original:    HOLA MUNDO
Num original:      7 14 11 0 | 12 20 13 3 14
Num encriptado:    17 0 11 8 | 16 4 21 23 0
Texto encriptado:  RALI QEVXA
```

### `afin_desencriptar.py`

Revierte el cifrado Afín.

**Fórmula:** `D(y) = a⁻¹ · (y − b) mod 26`

- `y`: número de la letra encriptada
- `a⁻¹`: inverso modular de `a`, el número que cumple `(a · a⁻¹) mod 26 = 1`
- `b`: desplazamiento usado al encriptar

No se puede "dividir" entre `a` en aritmética modular, así que se multiplica por su inverso. Por ejemplo, el inverso de `5` es `21`, porque `5 · 21 = 105` y `105 mod 26 = 1`. Este inverso solo existe cuando `a` es coprimo con 26, por eso la restricción al encriptar.

Ofrece dos modos:

1. **Ingresar a y b**: si se conoce la clave, desencripta directamente y muestra el inverso de `a`.
2. **Fuerza bruta**: prueba las 312 claves posibles (12 valores de `a` × 26 de `b`) y muestra los 5 candidatos más probables.

Con 312 candidatos, contar letras frecuentes (como en César) no basta para elegir el correcto. Por eso aquí cada intento recibe un puntaje con la frecuencia real de cada letra en español: se suma el logaritmo de esa frecuencia, de modo que las letras raras (`K`, `W`, `X`) bajan mucho el puntaje y las comunes (`E`, `A`, `O`) casi no lo bajan. Gana el texto que más se parece al español.

```
$ python3 afin_desencriptar.py
Ingresa el texto encriptado: FC DGDLNF FZ DC DJDQFRFS
...
Elige una opcion: 2

Candidatos mas probables:
a =  7, b =  3 (puntaje   40.30): EL ATAQUE ES AL AMANECER
a = 19, b =  5 (puntaje   37.24): AT ELEOKA AM ET ESERACAN
a = 15, b =  3 (puntaje   34.49): OT AVAESO OY AT AQANOUOB
a =  3, b = 19 (puntaje   30.97): ED MNMGYE EC MD MOMZEIER
a = 21, b = 25 (puntaje   29.99): EP UJUISE EA UP UYUHEMER

Mas probable: a = 7, b = 3
Texto desencriptado:  EL ATAQUE ES AL AMANECER
```

En textos muy cortos (una o dos palabras) hay poca información estadística y el primer candidato puede no ser el correcto. Por eso se muestran 5: la respuesta suele estar entre ellos.

## Uso

Desde la carpeta del proyecto:

```bash
python3 cesar_encriptar.py
python3 cesar_desencriptar.py
python3 afin_encriptar.py
python3 afin_desencriptar.py
```

Las funciones también se pueden importar desde otro script:

```python
from cesar_encriptar import cifrado_cesar
from cesar_desencriptar import descifrado_cesar
from afin_encriptar import cifrado_afin
from afin_desencriptar import descifrado_afin

cifrado_cesar("hola", 3)        # 'KROD'
descifrado_cesar("KROD", 3)     # 'HOLA'
cifrado_afin("hola", 5, 8)      # 'RALI'
descifrado_afin("RALI", 5, 8)   # 'HOLA'
```

## Limitaciones

Estos cifrados son educativos y **no son seguros** para proteger información real:

- **César**: solo 26 claves, se rompe por fuerza bruta en segundos.
- **Afín**: solo 312 claves (12 valores de `a` × 26 de `b`), también vulnerable a fuerza bruta y a análisis de frecuencias (`afin_desencriptar.py` lo demuestra).
- Solo trabajan con letras `A`–`Z`. La `Ñ` y las vocales con tilde no se cifran y se dejan tal cual.
