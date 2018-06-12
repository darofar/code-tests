"""
PROBLEM
Starting with the number 1 and moving to the right in a clockwise direction a 5
by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101. What is
the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the
same way?

Análisis
Queremos encontrar una relación entre el numero de anillos formados, el ancho del
cuadrado y los valores en las esquinas. Analizando la espiral de tamaño 1 podemos
ver que:

    7  8  9
    6  1  2
    5  4  3

El valor del lado del cuadrado formado por la espira es 3 elementos. Expresado
en el numero de iteraciones necesarias para construir la espira n=1 tenemos:

LADO = 2n+1 = 3.

El valor de la esquina superior derecha (a partir de ahora E4) coincide con el
numero total de elementos en el cuadrado. Este número puede también expresarse
en función del LADO y por tanto del número de iteraciones necesarias para formar
la espira como:

E4 = AREA =  3² = (2n+1)².

Verificando esto con la espiral de 5x5 vemos que es la segunda iteración n=2 donde
el tamaño del lado es 2n+1=5 y el area, y por tanto valor del número de la esquina
superior derecha (E4) es (2n+1)²=5²=25.

Con esto podemos averiguar facilmente los valores de todos los elementos E4 de
cualquier espira si tenemos su lado, el numero de iteraciones necesarias o el
numero total de elementos. Ahora solo nos queda relacionar el valor de las otras
tres esquinas con este, obteniendo así el valor de la suma de todos sus elementos
en diagonal.

Notese que para n=0 tenemos un valor especial la matriz 1.
LADO = 1
AREA = 1
DIAGONAL = 1

EL valor de la esquina superior izquierda es el valor que ya tenemos menos el
numero de elementos en un lado menos uno:

E4(n) = AREA - LADO-1 => (2n+1)²-(2n+1-1) = (2n+1)²

Comprobando para n=1

E4(1) = (2n+1)²-2n = 7

Comprobando para n=2

E4(2) = (2n+1)²-2n = 21

Para las otras dos esquinas será entonces:

E3(n) = (2n+1)²-4n
E3(n) = (2n+1)²-6n

EL valor de la suma de todos los números de las esquinas será

ESQUINAS(n) = E1(n) + E2(n) + E3(n) + E4(n)
ESQUINAS(n) = 4(2n+1)²-12n

El valor de la suma de todos los números en diagonal se puede obtener como la
iteración de la suma recursiva de las esquinas para todas las iteraciones desde
la n=N hasta la n=0.

DIAGONAL(n) = ESQUINAS(n) + DIAGONAL(n-1)

compronado para n=1

DIAGONAL(1) = 4(2(1)+1)²-12(1) + DIAGONAL(0)
DIAGONAL(1) = 36        -12    + 1 = 25

DIAGONAL(2) = 4(2(2)+1)²-12(2) + DIAGONAL(1)
DIAGONAL(1) = 100       -24    + 25 = 101

"""


def squares(n):
    return 4*(pow((2*n+1), 2)) - 12*n


def get_diagonal_sum_for_iterations(n):
    if n == 0:
        return 1
    return squares(n)+get_diagonal_sum_for_iterations(n-1)


def get_diagonal_sum_for_spiral(side):
    if side < 0 or not isinstance(side, int) or side %2 == 0:
        print("ERROR: An spiral can only have an odd integer number as the valor of its side")
        return None
    result = get_diagonal_sum_for_iterations(int((side - 1)/2))
    print("The sum of all numbers in diagonals for the spiral of "+str(side)+"x"+str(side)+" is: "+str(result))


if "__main__" in __name__:
    get_diagonal_sum_for_spiral(1001)

