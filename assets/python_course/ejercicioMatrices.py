import recursos as mtx
import numpy as np


""" matrizA = [[1, -3, 2], [5, 6,-1], [4, -1, 3]]
matrizB = [[10, -30, 20], [50, 60,-10], [40, -10, 30]]
print(" SUMANDO MATRICES")
print(" MATRIZ A ".center(40,'='))
mtx.matrices.printMatriz(matrizA)
print(" MATRIZ B ".center(40,'='))
mtx.matrices.printMatriz(matrizB)
print(" SUMA A + B ".center(40,'='))
mtx.matrices.sumaMatrices(matrizA, matrizB)

print("Matriz Transpuesta de la matriz A".center(40))
mtx.matrices.printMatriz(matrizA)
mtx.matrices.transpuestaMatriz(matrizA)

print("Escalar por matriz c*A".center(40))
mtx.matrices.printMatriz(matrizA)
mtx.matrices.escalarMatriz(10, matrizA)

print(" PRODUCTO MATRICES")
print(" MATRIZ A ".center(40,'='))
mtx.matrices.printMatriz(matrizA)
print(" MATRIZ B ".center(40,'='))
mtx.matrices.printMatriz(matrizB)
print(" PRODUCTO A * B ".center(40,'='))
mtx.matrices.productoMatrices(matrizA, matrizB)

print("DETERMINANTE DE UNA MATRIZ A ")
print(" MATRIZ A ".center(40,'='))
mtx.matrices.printMatriz(matrizA)
mtx.matrices.detMatriz(matrizA)

print("COFACTORES DE UNA MATRIZ A ")
print(" MATRIZ A ".center(40,'='))
mtx.matrices.printMatriz(matrizA)
mtx.matrices.cofactores(matrizA)
 """

print('\n\n\n\n')

matrizA = [[1, -3, 2], [5, 6,-1], [4, -1, 3]]
# matrizA = [[10, -30, 20], [50, 60,-10], [40, -10, 30]]
# matrizA = [[3, 2, 5], [2, -1, 4], [-1, 2, 1]]   # det -24 -24
# matrizA = [[2, 1, -3, 2], [-4, 2, 4, -1], [-2, 1, 1, 4], [1, -2, -1, 4]]    # det -12   -12
# matrizA = [[2, -1, 0, 3], [0, 2, 3, 3], [1, -1, 3, 0], [-2, 3, 0, -1]]      # det -24  -24
# matrizA = [[1, 1, 2, 5], [2, 3, 6, 12], [1, 2, 5, 8], [1, 1, 2, 6]]      # det 1        1
# matrizA = [[1, 1, 2, 5, -4], [2, 3, 6, 12, -2], [1, 2, 5, 8, -5], [1, 1, 2, 6, -1], [8, 5, 4, 2, 3]]      # det 89        89

print()

print(f"\t=== Determinante del sistema {round(mtx.matrices.detMatriz(matrizA), 2)}")
B = np.array(matrizA)
print(f"Determinante de la matriz calculado en base a librería numpy:  {round(np.linalg.det(B),2)} " )
print(" MATRIZ A ".center(40,'='))
mtx.matrices.printMatriz(matrizA)


print(" MATRIZ INVERSA DE UNA MATRIZ A ".center(40,'='))
invmatrizA = mtx.matrices.inversaMatriz(matrizA, 2)
mtx.matrices.printMatriz( mtx.matrices.redondeaMatriz( invmatrizA ) )
print(f"\t=== Determinante de la matriz inversa {round( mtx.matrices.detMatriz(invmatrizA), 2 ) }")

print(" PRODUCTO A por su inversa o viceversa ".center(40,'='))
mtx.matrices.printMatriz( mtx.matrices.productoMatrices(matrizA, invmatrizA) )


print("\n\nREEMPLAZANDO COLUMNAS")
matrizIncognitas = [[1, -3, 2], [5, 6,-1], [4, -1, 3]]
variables = [8, 14, 9]
mtx.matrices.printMatriz( matrizIncognitas )
print(variables)
mtx.matrices.printMatriz( mtx.matrices.reemplazaColumna( matrizIncognitas, variables, 2 ))


print("\n\nSISTEMAS DE ECUACIONES")
ecuaciones = [[1, 0, 2, -1],[1,1,2,1],[4,2,2,-3],[0,2,1,4]]
variables = [3, 2, 1, 1]
mtx.matrices.printMatriz( ecuaciones )
print("   Determinante del sistema: ", mtx.matrices.detMatriz( ecuaciones ) )
print(variables)
print(" SOLUCION SISTEMA DE ECUACIONES ".center(40,'='))
mtx.matrices.printMatriz( mtx.matrices.sistemaEcuaciones(ecuaciones, variables) )

print("\n\nSISTEMAS DE ECUACIONES")
ecuaciones = [[1, -3, 2],[5, 6, -1],[4, -1, 3]]
variables = [-3, 13, 8]
mtx.matrices.printMatriz( ecuaciones )
print("   Determinante del sistema: ", mtx.matrices.detMatriz( ecuaciones ) )
print(variables)
print(" SOLUCION SISTEMA DE ECUACIONES ".center(40,'='))
mtx.matrices.printMatriz( mtx.matrices.sistemaEcuaciones(ecuaciones, variables) )

