# Calculadora en Python

Calculadora de consola desarrollada en Python para la materia **Actualización Tecnológica** (Práctica 2).

## Descripción

Programa de consola que permite realizar operaciones matemáticas básicas y avanzadas desde un menú.
Valida los datos ingresados para no cerrarse ante entradas incorrectas, controla casos no válidos
(como la división entre cero o la raíz de un número negativo), permite hacer varias operaciones
seguidas sin reiniciar y guarda un historial de las operaciones realizadas.

Su finalidad es practicar Python junto con el flujo de trabajo de Git, GitHub Issues y Markdown.

## Operaciones y estado

| N.º | Operación | Descripción | Estado |
|----:|-----------|-------------|:------:|
| 1 | Suma | `a + b` | ✅ Completada |
| 2 | Resta | `a - b` | ✅ Completada |
| 3 | Multiplicación | `a × b` | ✅ Completada |
| 4 | División | `a ÷ b`, no permite dividir entre cero | ✅ Completada |
| 5 | Potencia | Base elevada a un exponente (positivo, negativo o cero) | ✅ Completada |
| 6 | Módulo | Residuo de una división, no permite divisor cero | ✅ Completada |
| 7 | Raíz cuadrada | No acepta números negativos | ✅ Completada |
| 8 | Porcentaje | Porcentaje de una cantidad (15 % de 200 = 30) | ✅ Completada |
| 9 | Valor absoluto | `\|-7\| = 7` | ✅ Completada |
| 10 | Factorial | Enteros no negativos (hasta 1000) | ✅ Completada |
| 11 | Promedio | Promedio de varios números separados por espacios | ✅ Completada |
| 12 | Redondeo | Redondea a la cantidad de decimales indicada | ✅ Completada |
| H | Ver historial | Muestra las operaciones realizadas | ✅ Completada |
| L | Limpiar historial | Borra el historial | ✅ Completada |

**Además:**

- ✅ **Validación de entradas:** si se escribe algo que no es un número, el programa lo vuelve a pedir. Acepta coma o punto decimal (`3,5` o `3.5`).
- ✅ **Menú organizado:** operaciones agrupadas en básicas, avanzadas y otras.
- ✅ **Repetir operaciones:** después de cada operación se vuelve al menú, hasta elegir `0. Salir`.

## Tecnologías

- **Python 3** (solo la biblioteca estándar, no requiere instalar paquetes)
- **Git** para el control de versiones
- **GitHub** e **Issues** para organizar las tareas
- **Markdown** para la documentación

## Instalación y ejecución

Requisito: tener instalado Python 3.

```bash
git clone https://github.com/senju325/Calculadora.git
cd Calculadora
python3 calculadora.py
```

En Windows se ejecuta con `python calculadora.py`.

## Ejemplos de uso

Menú principal:

```text
==================================
          CALCULADORA
==================================

 Básicas
   1. Suma
   2. Resta
   3. Multiplicación
   4. División

 Avanzadas
   5. Potencia
   6. Módulo
   7. Raíz cuadrada
   8. Porcentaje

 Otras
   9. Valor absoluto
  10. Factorial
  11. Promedio
  12. Redondeo

 Historial
   H. Ver historial
   L. Limpiar historial

   0. Salir
==================================
```

Calcular un porcentaje:

```text
Elige una opción: 8

-- Porcentaje --
  Porcentaje (%): 15
  Cantidad: 200
  Resultado: 15% de 200 = 30
```

Entrada no válida y división entre cero (el programa no se cierra):

```text
Elige una opción: 4

-- División --
  Dividendo: diez
  Entrada no válida: escribe un número (por ejemplo 12 o 3.5).
  Dividendo: 10
  Divisor: 0
  Error: no se puede dividir entre cero.
```

Promedio de varios números:

```text
Elige una opción: 11

-- Promedio --
  Números separados por espacios: 4 8 6
  Resultado: promedio(4, 8, 6) = 6
```

Ver el historial:

```text
Elige una opción: h

-- Historial --
  1. 15% de 200 = 30
  2. promedio(4, 8, 6) = 6
```

## Estructura del proyecto

```text
Calculadora/
├── README.md
├── calculadora.py    # menú, lectura de datos, resultados, historial y repetición
└── operaciones.py    # funciones matemáticas
```

## Autor

**Gabriel Antonio Menacho Condorcet**
