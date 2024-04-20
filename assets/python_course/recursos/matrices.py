""" Tres dias de desarrollo de esta libreria 8 * 4 = 32 horas """
def esMatriz(matriz) :
    nRows = len(matriz)
    if isinstance(matriz, list) and nRows > 0 and isinstance(matriz[0], list) :
        return True
    return False
    
def dimencionMatriz(matriz):
    nRows = len(matriz)
    nCols = 0
    if isinstance(matriz, list) and nRows > 0 and isinstance(matriz[0], list) :
        for rows in matriz:
            if not isinstance(rows,list) or nCols > len(rows):
                nCols = 0
                nRows = 0
                break
            else :
                if nCols == 0 and len(rows) > 0 :
                    nCols = len(rows)                
    else :
        nRows = 0
    dimesiones = []
    dimesiones.append(nRows)
    dimesiones.append(nCols)
    return dimesiones

def numFilasMatriz(matrix) :
    arreglo = dimencionMatriz(matrix)
    return arreglo[0]

def numColumnasMatriz(matrix) :
    arreglo = dimencionMatriz(matrix)
    return arreglo[1]

def transpuestaMatriz(matriz) :
    if esMatriz(matriz) :
        transpuesta = []
        numfilas = numFilasMatriz(matriz)
        numcolums = numColumnasMatriz(matriz)
        for colM1 in range(numcolums) :
            fila = []
            for rowM1 in range(numfilas) :
                fila.append(matriz[rowM1][colM1])
            transpuesta.append(fila)        
        # printMatriz(transpuesta)
        # print('SE EJECUTO TRANSPUESTA '.center(40), end='')
        return transpuesta
    else :
        print("ERROR: TRANSPUESTA DE UNA MATRIZ - No es una matriz, no existe la transpuesta")
        return []

def printMatriz(matriz) :
    if esMatriz(matriz) :
        maxlen = 0
        for row in matriz :
            for col in row :
                if maxlen < len(str(col)) :
                    maxlen = len(str(col))
        maxlen += 1
        print("=".center(40,"="))
        for row in matriz :
            print('',end='|')
            for item in row :
                print(str(item).rjust(maxlen), end=' |')
            print()
    else :
        print("ERROR: método printMatriz, No es una matriz.")

def escalarMatriz(escalar, matriz) :
    if esMatriz(matriz) :
        rows = numFilasMatriz(matriz)
        cols = numColumnasMatriz(matriz)
        newMatriz = []
        for row in range(rows) :
            fila = []
            for col in range(rows) :
                fila.append(escalar * matriz[row][col])
            newMatriz.append(fila)
        # printMatriz(newMatriz)
        return newMatriz
    else :
        print("ERROR: método escalarPorMatriz - No es una matriz, o matriz vacia")
        return []

def sumaMatrices(matrizA, matrizB) :
    if esMatriz(matrizA) and esMatriz(matrizB) :
        numRowsA = numFilasMatriz(matrizA)
        numColsA = numColumnasMatriz(matrizA)
        numRowsB = numFilasMatriz(matrizB)
        numColsB = numColumnasMatriz(matrizB)
        print(f"elementos A[{numRowsA}][{numColsA}] + B[{numRowsB}][{numColsB}]".center(40))
        matrixSuma = []
        if ( numRowsA == numRowsB and numColsA == numColsB and numRowsA > 0 and numRowsA > 0) :
            for row in range(numRowsB):
                matrixSumaFila = []
                for col in range(numColsB):
                    matrixSumaFila.append(matrizA[row][col] + matrizB[row][col])
                matrixSuma.append(matrixSumaFila)
            # printMatriz(matrixSuma)
            return matrixSuma
        else :
            print("Error::Método sumaMatrices, matrices deben ser de iguales dimensiones nxm")
    else :
        print("Error::Método sumaMatrices, Alguno de los operadores no es una matriz")
    return []

def productoMatrices(matrizA, matrizB) :
    if esMatriz(matrizA) and esMatriz(matrizB) :
        numRowsA = numFilasMatriz(matrizA)
        numColsA = numColumnasMatriz(matrizA)
        numRowsB = numFilasMatriz(matrizB)
        numColsB = numColumnasMatriz(matrizB)
        if (numColsA == numRowsB and numColsA > 0 and numRowsB > 0) :
            matrixProducto = []
            # print(f"Por cada fila del multiplicando crear una submatriz de resultados e ir tomando cada valor de las columnas de esta fila y multiplicando por cada columna de la matriz multiplicadora {numRowsA} x {numColsB}, el pivote recorre entre rowM2 = colM1 - {numColsA} elementos")
            for rowM1 in range(numRowsA):
                filaProd = []
                for colM2 in range(numColsB) :
                    sumaRowCol = 0 
                    for pivote in range(numColsA) :
                      # print(f"rM1-{rowM1},pv-{pivote},cM2-{colM2}   {sumaRowCol}", end=" + ")
                      sumaRowCol += (matrizA[rowM1][pivote] * matrizB[pivote][colM2])
                      # print(f"({matrizA[rowM1][pivote]} * {matrizB[pivote][colM2]}) = {sumaRowCol} ")
                    filaProd.append(sumaRowCol)
                matrixProducto.append(filaProd)
            print(f" A[{numRowsA}][{numColsA}] x B[{numRowsB}][{numColsB}] = PRODUCTO[{numRowsA}][{numColsB}]".center(40))
            # printMatriz(matrixProducto)
            return matrixProducto
        else :
            print("ERROR::Método productoMatrices, número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz")                
    else :
       print("Error::Método productoMatrices, Alguno de los operadores no es una matriz")
    return []

def detMatriz2x2(matriz) :
    if esMatriz(matriz) :
        numRows = numFilasMatriz(matriz)
        numCols = numColumnasMatriz(matriz)        
        # print(f"Para matriz A[{numRows}][{numCols}] se calcula determinante")
        # printMatriz(matriz)
        if numRows == numCols and numRows > 0 and numCols > 0  and numRows == 2:
            introw = numRows # dimensiones de la matriz cuadrada ej. 2x2 sera 2
            determinante = 0  # resultado final de la matriz es la diferencia de diagonalPrincipalSumas - diagonalSecundariaRestas
            if (introw == 2) :
                determinante = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
                # print(f"Determinante de la matriz en base a procedimiento: {determinante}")
                return determinante
        else :
            print("ERROR::método detMatriz2x2, debe ser una matriz cuadrada nxm, donde n sea igual a m y mayores que cero")
    else :
        print("ERROR::método detMatriz2x2, no es una matriz el determinante no se calcula")
    return 0

def detMatriz(matriz) :
    if esMatriz(matriz) :
        numRows = numFilasMatriz(matriz)
        numCols = numColumnasMatriz(matriz)        
        # print(f"Para una matriz A[{numRows}][{numCols}]")
        # printMatriz(matriz)
        if numRows == numCols and numRows > 0 and numCols > 0 :
            introw = numRows # dimensiones de la matriz cuadrada ej. 3x3 sera 3
            posrow = list(range(introw))  #0,1,2 Cambios crecientes cada fila a multiplicar por la diagonal principal
            posrow2 = list(range(introw-1, -1, -1))  #2,1,0 Cambios decrecientes, filas a multiplicar por diagonal secundaria
            poscol = list(range(introw))  #0,1,2  No tendrá cambios en su contenido, id de cada columna
            pivote = 0    # Cantidad de diagonales principales y secundarias osea numero de interacciones
            diagonalPrincipalSumas = 0  # Suma los productos de la diagonal principal
            diagonalSecundariaRestas = 0  # Suma los productos de la diagonal secundaria
            determinante = 0  # resultado final de la matriz es la diferencia de diagonalPrincipalSumas - diagonalSecundariaRestas
            if (introw == 2) :
                return detMatriz2x2(matriz)
            if introw > 3 :                
                determinante = 0
                for pivcols in range(introw) :
                    adj = (-1)**((posrow[0] + poscol[pivcols] + 2))
                    # print(f"+ ( {adj} * {matriz[0][pivcols]} * {detMatriz(cofactorMatriz(matriz, 0, pivcols))} )", end=" ")
                    determinante += adj * matriz[0][pivcols] * detMatriz(cofactorMatriz(matriz, 0, pivcols))
                return determinante            
            # End if introw > 3
            while pivote < introw :
                pivote += 1
                productos = 1   # calcula los productos de los elementos de las diagonales principales y secundarias
                for posnew in range(introw) :
                    # adj = (-1)**((posrow[posnew] + poscol[posnew] + 2))
                    # print(f" {posrow[posnew]}: {poscol[posnew]} : {adj} : {(adj * matriz[posrow[posnew]][poscol[posnew]])} ", end='|')
                    productos *= (matriz[posrow[posnew]][poscol[posnew]])
                    # print(f" productos *= Matriz[{posrow[posnew]}][{poscol[posnew]}]  *= {matriz[posrow[posnew]][poscol[posnew]]}")
                # print(f"diagonalPrincipalSumas += productos {productos}")
                diagonalPrincipalSumas += productos

                productos = 1   # calcula los productos de los elementos de las diagonales principales y secundarias
                for posnew in range(introw) :
                    # adj = (-1)**((posrow[posnew] + poscol[posnew] + 2))
                    productos *= (matriz[posrow2[posnew]][poscol[posnew]])
                    # print(f" productos *= Matriz[{posrow2[posnew]}][{poscol[posnew]}] *= {matriz[posrow2[posnew]][poscol[posnew]]}")
                # print(f"diagonalSecundariaRestas += productos {productos}")
                diagonalSecundariaRestas += productos

                for posnew in range(introw) :
                    posrow[posnew] += 1
                    posrow2[posnew] -= 1
                    if (posrow[posnew] >= introw) :
                        posrow[posnew] -= introw
                    if (posrow2[posnew] < 0) :
                        posrow2[posnew] = introw - 1

            determinante = diagonalPrincipalSumas - diagonalSecundariaRestas
            # print(f"Determinante de la matriz en base a procedimiento: {determinante}")
            return determinante
        else :
            print("ERROR::método detMatriz, debe ser una matriz cuadrada nxm, donde n sea igual a m y mayores que cero")
    else :
        print("ERROR::método detMatriz, no es una matriz el determinante no se calcula")
    return 0

def cofactorMatriz(matriz, intfila, intcol) :
    if esMatriz(matriz) :
        numRows = numFilasMatriz(matriz)
        numCols = numColumnasMatriz(matriz)
        if numRows == numCols and numRows > 0 and numCols > 0 :
            introw = numRows # dimensiones de la matriz cuadrada ej. 3x3 sera 3
            matrizCofactor = []            
            for rows in range(introw):
                filaCofactor = []
                if rows != intfila :
                    for cols in range(introw) :
                        if cols != intcol :
                            filaCofactor.append(matriz[rows][cols])
                    matrizCofactor.append(filaCofactor)
            return matrizCofactor                    
    return []
        
def cofactores(matriz, modoDepuracion = 0) :
    if esMatriz(matriz) :
        numRows = numFilasMatriz(matriz)
        numCols = numColumnasMatriz(matriz)        
        if numRows == numCols and numRows > 0 and numCols > 0 :
            introw = numRows # dimensiones de la matriz cuadrada ej. 3x3 sera 3
            matrizCofactores = []
            for rows in range(introw):
                filaCofactor = []
                for cols in range(introw):
                    cofactorMatriz = []                    
                    # print(f"Iterancia de : {celrow}{celcol}")
                    for celRMat in range(introw) :
                        subfila = []
                        for celCMat in range(introw) :
                            if (celRMat != rows and celCMat!= cols) :
                                # print(f"{celRMat}{celCMat}",end=" ")
                                subfila.append(matriz[celRMat][celCMat])
                        # print()
                        if len(subfila) > 0:
                            cofactorMatriz.append(subfila)

                    detCofactor = detMatriz(cofactorMatriz)
                    if modoDepuracion == 1 :
                        print(f"cofactor A[{rows}][{cols}] = det(A) = {detCofactor}, ", end='')
                        printMatriz(cofactorMatriz)                        
                    filaCofactor.append(detCofactor)
                matrizCofactores.append(filaCofactor)
            # printMatriz( matrizCofactores )
            return matrizCofactores
        else :
            print("ERROR::método cofactores, debe ser una matriz cuadrada nxm, donde n sea igual a m y mayores que cero")
    else :
        print("ERROR::método cofactores, no es una matriz el determinante no se calcula")
    return []

def efectoReglaSigno(matriz) :
    if esMatriz(matriz) :
        numRows = numFilasMatriz(matriz)
        numCols = numColumnasMatriz(matriz)
        ubirow = 0
        ubicol = 0
        reglasignos = []
        signos = []
        for row in range(numRows) :
            if row % 2 == 0 :
                ubirow = 1
            else :
                ubirow = -1
            filaAfectada = []
            signosFila = []
            for col in range(numCols) :
                if col % 2 == 0 :
                    ubicol = 1
                else :
                    ubicol = -1
                filaAfectada.append( ubirow * ubicol * matriz[row][col] )
                signosFila.append(ubirow * ubicol)
            reglasignos.append(filaAfectada)
            signos.append(signosFila)
        # print(" SE EJECUTO EFECTO REGLA DE SIGNOS ".center(40,), end='')
        # printMatriz(reglasignos)
        # printMatriz(signos)
        return reglasignos
    return []

def inversaMatriz(matriz, numDec = 6) :
    if esMatriz(matriz) :
        numRows = numFilasMatriz(matriz)
        numCols = numColumnasMatriz(matriz)        
        if numRows == numCols and numRows > 0 and numCols > 0 :
            detmatriz = round( detMatriz(matriz), numDec )
            if detmatriz != 0 :
                matrizInversa = escalarMatriz( 1/detmatriz, transpuestaMatriz(  efectoReglaSigno( cofactores(matriz) ) ) )
                return matrizInversa
            else :
                print('ERROR::método inversaMatriz, matriz singular, determinante cero.')
            # print(" MATRIZ INVERSA ".center(40,'='))
            # printMatriz(matrizInversa)
        else :
            print("ERROR::método inversaMatriz, debe ser una matriz cuadrada nxm, donde n sea igual a m y mayores que cero")
    else :
        print("ERROR::método inversaMatriz, no es una matriz el determinante no se calcula, no existe matriz inversa")
    return []
    
def setMatriz() :
    print("""Definir una matriz. 
    1° Establecer las dimensiones de la matriz numFilas y numColumnas 
    2° Ingresar cada uno de los elementos de la matriz """)
    numRows = int(input("Cantidad de filas de la matriz: "))
    numCols = int(input("Cantidad de columnas de la matriz: "))
    matrix = []
    if numRows > 0 and numCols > 0 :
        print("Establezca los elementos de la matriz")
        for row in range(numRows):
            rowMatrix = []
            for col in range(numCols):
                rowMatrix.append(float(input(f"Matriz row-{row}, col-{col} : ")))
            matrix.append(rowMatrix)
        print(" MATRIZ GENERADA ".center(40,"="))
    else :
        print("ERROR::método setMatriz, no contiene elementos la matriz")
    return matrix

def redondeaMatriz(matriz, numDec = 2) :
    if esMatriz(matriz) :
        numRows = numFilasMatriz(matriz)
        numCols = numColumnasMatriz(matriz)
        matrizRedodeada = []
        for i in range(numRows) :
            filaRedondeada = []
            for j in range(numCols) :
                filaRedondeada.append( round(matriz[i][j], numDec) )
            matrizRedodeada.append(filaRedondeada)
        return matrizRedodeada
    return []
        
def reemplazaColumna(matriz, columna, parCol = 0) :
    if esMatriz(matriz) and isinstance(columna, list) :
        numRows = numFilasMatriz(matriz)
        numCols = numColumnasMatriz(matriz)
        numitem = len(columna)        
        if numRows > 0 and numCols > 0 and numRows >= numitem :
            newMatriz = []
            for i in range(numRows) :
                newFila = []
                for j in range(numCols) :
                    elemento = matriz[i][j] 
                    if parCol == j and i <= numitem :
                        elemento = columna[i]
                    # print(f"i<=numitem: {i} <= {numitem}, j==parcol: {j}=={parCol}, item: {elemento}, \t", end='')
                    newFila.append(elemento)
                newMatriz.append(newFila)
            return newMatriz
    else :
        print("ERROR: método reemplazaColumna primer parametro no es matriz o segundo parametro no es lista")
    return []
        
def sistemaEcuaciones(ecuaciones, incongnitas) :
    if esMatriz(ecuaciones) and isinstance(incongnitas, list) :
        numRows = numFilasMatriz(ecuaciones)
        numCols = numColumnasMatriz(ecuaciones)
        numitem = len(incongnitas)
        if numRows == numCols == numitem and numRows > 0:
            # print("Procede")
            detSistem = detMatriz(ecuaciones)
            if (detSistem != 0) :
                # print("Matriz no es singular")
                matrizEcuaciones = []
                varX = 'X'
                for i in range(numCols) :
                    filaReemplazos = []
                    matrizReemplazada = reemplazaColumna(ecuaciones, incongnitas, i)
                    filaReemplazos.append(varX + str(i))
                    filaReemplazos.append(detMatriz(matrizReemplazada) / detSistem)
                    matrizEcuaciones.append(filaReemplazos)
                return matrizEcuaciones
            else:
                print("Matriz es singular")
        else :
            print("ERROR::metodo sistemaEcuaciones, no es matriz cuadrada y/o no coincide cantidad de elementos de las constantes no coincide con cantidad de variables")
    else:
        print("ERROR::metodo sistemaEcuaciones, no es una matriz o incongnitas no es lista")
    return []
