# Encriptación César y Afín

Implementación en Python de dos cifrados clásicos por sustitución: **César** y **Afín**. Incluye encriptación, desencriptación y un ataque de fuerza bruta contra César.

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
└── afin_encriptar.py       # encriptación Afín
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

## Uso

Desde la carpeta del proyecto:

```bash
python3 cesar_encriptar.py
python3 cesar_desencriptar.py
python3 afin_encriptar.py
```

Las funciones también se pueden importar desde otro script:

```python
from cesar_encriptar import cifrado_cesar
from cesar_desencriptar import descifrado_cesar
from afin_encriptar import cifrado_afin

cifrado_cesar("hola", 3)        # 'KROD'
descifrado_cesar("KROD", 3)     # 'HOLA'
cifrado_afin("hola", 5, 8)      # 'RALI'
```

## Limitaciones

Estos cifrados son educativos y **no son seguros** para proteger información real:

- **César**: solo 26 claves, se rompe por fuerza bruta en segundos.
- **Afín**: solo 312 claves (12 valores de `a` × 26 de `b`), también vulnerable a fuerza bruta y a análisis de frecuencias.
- Solo trabajan con letras `A`–`Z`. La `Ñ` y las vocales con tilde no se cifran y se dejan tal cual.
