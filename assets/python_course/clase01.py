import os
print("Hola mundo")
print("estar aprendiendo Phyton")
print("Operación de suma")
var_int = 2
var_float = 2.5
var_str = "Hola mundo"
resultado = 6.96 + 4.23
""" El resultado de la operacion como comentario """
print(var_int + var_float)
resultado += 11.6
print("El resultado es " + str(resultado))

print("BUSCAR SUBCADENA con metodo find, retorna -1 si no encuentra, var_str.find(\"Leonel\")")
var_str = "Buenas tardes Leonel"
print("Buscando subcadena Leon, retorna la posición: " + str(var_str.find("Leonel")))

print("""\nEXTRACCION DE SUBCADENA mediante [ini : fin : salto], ej. var_str[1 : 9 : 2] otro caso var_str[ini:fin], desde ini hasta fin-1. Salto implica cantidad de caracteres menos 1 a obviar por omision salto es 1, puede obviarse el valor ini ej. var_str[ : 3] """)
ini=1
fin=9
print(var_str[ini:fin])

print("\nCOMPARACION usa el operador == generando un True o un False")
var_str1 = "Hola"
var_str2 = "hola"
print(var_str1 == var_str2)

print("\nOPERADORES suma +, resta -, multiplicacion *, exponenciacion **, residuo o modulo %, division /, division entera //")
var_resp = 7 + 6
print("Resultado de la suma 7 + 6 = " + str(var_resp))
var_resp = 17.33 + 6.66
print("Resultado de la suma 17.33 + 6.66 = " + str(var_resp))
print("Resultado de la resta 17.33 - 6.66 = " + str(17.33 - 6.66))
print("Resultado de la multiplicacion 17.33 * 6.66 = " + str(17.33 * 6.66))
print("Resultado de la exponenciación 17.33 ** 3 = " + str(17.33 ** 3))
print("Resultado de la división 17.33 / 3 = " + str(17.33 / 3))
print("Resultado de la división entera 17.33 // 3 = " + str(17.33 // 3))
print("Resultado de la residuo o modulo 17 % 3 = " + str(17 % 3))

print("\nCOMENTARIOS - Se usa el gato o almohadilla #Comentario de linea simple, las comillas dobles Ej. \"Esto es un comentario\" o triple comillas dobles para comentar varias lineas \"\"\"Comentado en varias lineas de código\"\"\" ")
# Comentario de linea simple
"Comentario"
""" Comentar varias 
    líneas de código """

datonum = 777
tipos_datos = """\nTIPOS DE DATOS - 
1. Enteros y Largos (int o long)
2. Flotantes o reales (float)
3. Complejos (complex) Ej. var = 5 + 6j
4. Cadenas se respetan los saltos de linea sin necesitar recurrir a \\n
5. Booleanos (bool)
Con el método type(datonum) se obtiene el tipo de dato contenido en la variable datonum """
print(tipos_datos)
print('1.', datonum, type(datonum))
datonum = 16.68
print('2.', datonum, type(datonum))
datonum = 5 + 6j
print('3.', datonum, type(datonum))
datonum = "Leonel"
print('4.', datonum, type(datonum))
datonum = False
print('5.', datonum, type(datonum))
print('5.', "verdadero_falso = 3 == 3", 3 == 3, type(3 == 3))
print('5.', "verdadero_falso = 5 == 3", 5 == 3, type(5 == 3))

print("""
CONDICIONALES SIMPLES - Respetar el indentado o tabulacion
if CondicionLogica :
  Instrucciones
  ...
elif otraCondicionLogica :
  Instrucciones
  ...
else :
  Instrucciones
  ...
Instrucciones fuera de la condicionLogica
""")
datonum = 8
if datonum <= 5 :
    print("El número es menor o igual que cinco")
elif datonum>5 and datonum<10:
    print("El número es mayor que cinco pero menor que 10")
else :
    print("El número es mayor o igual que diez")
print("Fin de la condicion usando el if en condición lógica básica\n")

print("""CICLOS O BUCLES la sentencias BREAK y CONTINUE operan igual que en otros lenguajes recordar break y continue
while condicion:
  Instrucciones
  ...
Instrucciones una vez no se cumpla la condicion para el while
""")
x=3
while x<10:
    print(x,end=",")
    x+=1
print("\nFin de while, x tendría", x, sep = " ")

print("""\nCICLOS O BUCLES FOR el objetoIterable puede ser un string, lista
for nomVar in objetoIterable : 
  instrucciones
  ...
Instrucciones una vez se termine el for  """)
cadena = "Esto es un objeto iterable"
for caracter in cadena :
    print(caracter)
print("Fin del for")

print("""\nOPERADORES RELACIONALES <, >, ==, !=, <= y >= \n """)
print("""OPERADORES LOGICOS conjunción (and), disyunció (or) y negación (not) \n """)
print("""PARAMETRO end y sep - al definir end como parametro puede eliminar el salto de linea en un print, Ej. print(\"Texto sin salto de linea\", end=\" \").
El parametro sep da formato a las cadenas de caracteres que deben imprimirse en pantalla, agregando un separador entre las cadenas que se imprimiran, por omision es el \" \". Ej. 
print("1","2","3","4","5",sep="") """)
print("Esto es un texto", end=". ")
print("Esto es un texto que iria en la siguiente linea.")
print("1","2","3","4","5",sep=", ",end="\n\n")

print("FUNCION len(\"Cantidad de caracteres\"), retorna la longitud de la cadena de caracteres, igual al length de javascript\n")

print("""CONCATENACION MEDIANTE METODO format
nombre = "Leonel"
edad = 52.00146
print("Hola {} tienes {} años de edad".format(nombre, round(edad,2)))
print("Hola {nombre} tienes {edad} años de edad".format(nombre = "Sebastian", edad = 23.667))
print("Hola {1} tienes {0} años de edad".format(nombre, round(edad,2)))
""")
nombre = "Leonel"
edad = 52.00146
print("Hola {} tienes {} años de edad".format(nombre, round(edad,2)))
print("Hola {nombre} tienes {edad} años de edad".format(nombre = "Sebastian", edad = 23.667))
print("Hola {1} tienes {0} años de edad".format(nombre, round(edad,2)))

print("""\nCONCATENACION CON f-Strings - Son evaluadas al momento de su ejecución
Debe existir un f"Hola {nombre} tienes {edad+2-1} años"
nombre = "Sebastian"
edad = 23
print(f"Usando f-Strings. Hola {nombre} tienes {edad+2-1} años")""")
nombre = "Sebastian"
edad = 23
print(f"Usando f-Strings. Hola {nombre.upper()} tienes {edad+2-1} años")
print(f"Usando f-Strings. 4 + 7 = {4 + 7}\n")

print("""EL METODO strip(), lstrip() y rstrip(), elimina el caracter especificado o por default espacios vacios al inicio, al final o a ambos lados similar a metodos ltrim, rtrim y trim de java. Ej.
cadena = " Hola    Leonel    "
cadena = "...Hola    Leonel    ...."
cadena.strip(" ")  equivalente a cadena.strip()
cadena.strip(". l")  """)
cadena = "...Hola    Leonel    ...."
print(f"{cadena.strip('. l')}\n")

print("""METODOS istitle() y title()
cadena.istitle() retorna True o False
cadena.title() convierte la cadena a formato de título primera letra de cada palabra en mayusculas y el resto en minusculas """)
cadena = "carLOS galLarDo"
if not cadena.istitle():
    # cadena = cadena.lower()
    print(cadena.title(),"\n")

print("""METODOS islower(), isupper(), lower() y upper()
cadena.islower(), cadena.isupper retorna True o False en caso que contenga minusculas o mayusculas según el caso.
cadena.lower() y cadena.upper convierte la cadena completa a minusculas o mayusculas según el caso.""")
cadena = "carLOS galLarDo"
if not cadena.islower():
    print(cadena.lower(),"\n")

print("""METODOS swapcase()
cadena.swapcase(), convierte el contenido de las mayusculas a minusculas y minusculas a mayusculas.""")
cadena = "carLOS galLarDo"
print(cadena.swapcase(),"\n")

print("""METODOS capitalize()
cadena.capitalize(), convierte el contenido estableciendo la primera letra del contenido en mayuscula y el resto completo en minusculas""")
cadena = "carLOS galLarDo"
print(cadena.capitalize(),"\n")

print("""METODOS center(), ljust() y rjust()
cadena.center(new_len, unCaracter), cadena.ljust() y cadena.rjust para alineacion de texto segun la indicacion respectiva, new_len debe ser un entero mayor a la longitud del contenido de cadena y el caracter unico sera el caracter de los limites inferiores y superiores en caso de omitir el unCaracter este toma el valor de caracter vacio " "
print(cadena.center(100,"="))
print(cadena.ljust(100,"="))
print(cadena.rjust(100,"=")) """)
cadena = "carLOS galLarDo"
print(cadena.center(100,"="))
print(cadena.ljust(100,"="))
print(cadena.rjust(100,"="),"\n")

print("""METODO count()
cadena.count("subcadena" [, int1 [, int2]]) busca subcadena en parte especifica de la cadena, la subcadena es obligatoria
Si cadena = "mi mama me mima"
len(cadena) seria 15 y cadena.count("") genera 16 
cadena.count("M") retorna 0 por no encontrarse el substring M dentro de la cadena
cadena.count("m") retorna 6 porque encontró seis ocurrencias de substring m dentro de cadena 
cadena.count("me mima") retorna 1 porque encontró una ocurrencia de substring me mima dentro 
de cadena
cadena.count("m", 13) retorna 1 porque encontró una ocurrencia de substring m dentro de cadena a partir de la posición 13, recordar que empieza en posición 0
cadena.count("m", -3) retorna 1 porque encontró una ocurrencia de substring m dentro de cadena a partir de la posición -3, recordar que empieza en posición 0 de derecha a izquierda y avanza hacia la derecha el contador.
cadena.count("m", 0, 8) retorna 3 porque encontró tres ocurrencia de substring m dentro de cadena a partir de la posición 0 hasta la posición 8
cadena.count("m", -4, -1) retorna 2 porque encontró dos ocurrencia de substring m dentro de cadena a partir de la posición -4 hasta la posición -1""")
cadena = "mi mamá me mima"
print(len(cadena))
print(cadena.count(""))
print(cadena.count("M"))
print(cadena.count("m"))
print(cadena.count("me mima"))
print(cadena.count("m",13))
print(cadena.count("m",-3))
print(cadena.count("m", 0, 8))
print(cadena.count("m", -4, -1),'\n')

print("""METODOS startswith() y endswith()
Mínimo 1 parámetro y máximo 3 cadena.startswith("substring" [, int1 [, int2]]) 
retorna True o False si cadena inicia con un substring igual al definido o para el caso de endswith si la cadena termina con un substring igual al definido.
print(cadena.startswith("D"))
print(cadena.startswith("se", 6))
print(cadena.startswith("se", 6, 7)) retornara un False 
print(cadena.startswith("se", -4, -1)) """)
cadena = "Diana se peina sola"
print(cadena.startswith("D"))
print(cadena.startswith("se", 6))
print(cadena.startswith("se", 6, 7))
print(cadena.startswith("se", -4, -1), '\n')
print(cadena[ : : 2])
print(cadena[ : 15 : 2])

print("""ENTRADA DE DATOS DESE EL TECLADO - Se usa el metodo var = input(\'Palabras mensaje para el ingreso de datos\') 
Si se desea recibir un valor entero entones se gestiona asi var = int(input(\'Palabras mensaje para el ingreso de datos\'))
Para float seria var = float(input(\'Palabras mensaje para el ingreso de datos\')) 
Para complejo seria var = complex(input(\'Palabras mensaje para el ingreso de datos\'))
""")
# Practicas con input
datonum = input('Introduce una palabra: ')
print('Introdujo la palabra: \"', datonum,'\"', type(datonum))
datonum = int(input('Introduce un entero: '))
Sum = datonum
datonum = float(input('Introduce un número flotante: '))
Sum += datonum
print("El resultado de la suma es: " + str(Sum))
datonum = complex(input('Introduce un número complejo: '))
Sum += datonum
print("El resultado de la suma es: " + str(Sum),'\n')

print("""LA CLASE range - Genera una secuencia de numeros inmutables osea no se pueden modificar, es usada como objeto iterable en los ciclos for. range permite trabajar con un minimo de un argumento y un máximo de tres argumentos.
range(stop) donde stop indica el numero hasta el cual se generará la secuencia pero jamas formara parte de la secuencia. ej. range(10) genera valores entre [0 , 10)
range(start, stop) donde start es int a partir del que se inicia la generación de secuencia de números y el cual formara parte de la secuencia.
range(start, stop, step) donde step es int para indicar el incremento o decremento de la sucecion numérica. """)
print(range(10))
for i in range(1, 10, 2):
    print(i, end=", ")
print("\nFin del bucle for con el uso de range\n")

print("EJERCICIO PRACTICO - Tabla de multiplicar")
tablaDe = int(input("Qué tabla de multiplicar desea generar: "))
rango = range(13)
print(f"tabla de multiplicar del {tablaDe} es:")
for valMul in rango :
    print(f"{tablaDe} x {valMul} = {valMul*tablaDe}",'\n')

print("""LISTAS - Son objetos iterables que pueden ser usados en un ciclo for
listaVacia = []
listaHomogenea = ["Javier", "Carlos", "Maria"]
listaHeterogenea = ["Sebastián", 23, 3.1416, 1.83, True]""")
listaVacia = []
listaHomogenea = ["listaHomogenea", "Javier", "Carlos", "Maria"]
listaHeterogenea = ["listaHomogenea", "Sebastián", 23, 3.1416, 1.83, True]
print(listaVacia)
print(listaHomogenea)
print(listaHeterogenea,'\n')

print("""ACCEDER A LOS ELEMENTOS DE LISTAS - Son objetos iterables que pueden ser usados en un ciclo for
listaHomogenea[0], listaHomogenea[1], listaHomogenea[2]
listaHomogenea[-1], listaHomogenea[-2], listaHomogenea[-3]
listaHomogenea[1 : 3] toma el rango de datos desde [1,3), 
listaHomogenea[: 3] toma el rango de datos desde [0,3),
listaHomogenea[1 : ] toma el rango de datos desde [1,final],
listaHomogenea[-4 : -2] toma el rango de datos desde la posición [-4,-2)
len(listaHomogenea) obtiene la cantidad de elementos de la lista """)
print("longitud de la listaHomogenea",len(listaHomogenea))
print("listaHomogenea[3]", listaHomogenea[3])
print(listaHomogenea[-4 : -2])
print(listaHomogenea[ : 3])
print(listaHomogenea[ : len(listaHomogenea)],"\n")

print("""MODIFICAR LOS ELEMENTOS DE LISTAS
listaHomogenea[1] = "Sebastián"
listaHomogenea[2:4] = [5.6, 8.9]   # modifica los elementos en el rango [2,4)
Si se da el caso de tener mas elementos a modificar como en el caso siguiente, modifica los [1,3) e inserta los [3,5]
listaHomogenea[1:3] = ["Nombre1", 2, 3, 4] 
Para el caso que se tenga menos elementos a modificar entonces los agrega y recorre los contenidos hacia la izquierda como el caso siguiente, generando una reducción del tamaño de la lista 
listaHomogenea[2:5] = ["Leonel", "Emilio"] 
En la asignacion puede obviarse los corchetes
listaHomogenea[2:5] = "Leonel", "Emilio" 
listaHomogenea[1:3] = "Nombre1", 2, 3, 4 
listaHomogenea[:] = "x" resulta una lista de un solo elemento "x" """)
listaHomogenea[1:3] = ["Sebastián", 2, 3, 4]
listaHomogenea[2:5] = ["Leonel", "Emilio"]
print(listaHomogenea,'\n')

print("""AGREGAR ELEMENTOS A UNA LISTA - METODO append() un solo argumento es obligatorio
listaHomogenea.append("Nuevo elemento agregado al final de la lista")  # agregar solo un elemento a la lista""")
listaHomogenea.append("Nuevo elemento agregado al final de la lista usando append")
print(listaHomogenea,'\n')

print("""AGREGAR ELEMENTOS A UNA LISTA - METODO insert(), requiere de 2 parametros obligatorios
listaHomogenea.insert( int_Posicion, "Nuevo elemento") 
listaHomogenea.insert(len(listaHomogenea), "Agregando al final")
listaHomogenea.insert(0, "Agregando al principio")
listaHomogenea.insert(2, "Dos")
Si int_Posicion es mayor que el ultimo indice, entonces, inserta al final de la lista no coincidiendo el intPosicion con el len(lista)
listaHomogenea.insert(100, "Cien")""")
listaHomogenea.insert(len(listaHomogenea), "Agregando al final")
listaHomogenea.insert(0, "Agregando al principio")
listaHomogenea.insert(2, "Dos")
listaHomogenea.insert(100, "Cien")
print(listaHomogenea,'\n')

print("""ELIMINAR ELEMENTOS A UNA LISTA - METODO pop()
Elimina el último elemento de la lista o un elemento específico pero requiere especificar posicion del elemento a eliminar. Devuelve el valor del elemento eliminado
listaHomogenea.pop()  # elimina el ultimo elemento de la lista
ultimo = listaHomogenea.pop()
listaHomogenea.pop(int_Posicion)
listaHomogenea.pop(0), listaHomogenea.pop(2)
posCero = listaHomogenea.pop(0), posDos = listaHomogenea.pop(1)
int_Posicion puede ser positivo, negativo o el cero, si es mayor o igual que len(lista) genera error pop index out of range.""")
listaHomogenea.pop()
listaHomogenea.pop(0)
uno = listaHomogenea.pop(1)
print(listaHomogenea, uno,'\n')

print("""ELIMINAR ELEMENTOS A UNA LISTA - METODO remove() - Elimina un elemento de la lista especifico, requiere indicar el elemento contenido a eliminar. Solo elimina la primera coincidencia sin importar si existen repetidos. Retorna none, en caso de no existir el elemento error list.remove(x): x not in list.
No retorna el elemento removido a diferencia del método pop()
listaHomogenea.remove(elemento_a_eliminar)
listaHomogenea.remove("Agregando al final")""")
retorno = listaHomogenea.remove("Agregando al final")
print(listaHomogenea, retorno, '\n')

print("""ELIMINAR UNA LISTA - INSTRUCCION del() - Para eliminar toda una lista.
Eliminar un elemento indicando la posición.
Dos o mas elementos simultaneos indicando el rango de posiciones de los elementos a eliminar.del listaHeterogenea   # Elimina la lista incluida la variable, no se puede ni agregar elementos
del listaHeterogenea[intPosicion]   # intPosicion es entero + o -
del listaHeterogenea[intPosIni : intPosFin] # Elimina de lista desde [intPosini, intPosFin) 
del listaHeterogenea[ : ]   # similar a "del listaHeterogenea" a diferencia que lista aun existe como listaVacia""")
del listaHeterogenea[0]
del listaHeterogenea[2 : 4]
del listaHeterogenea[ : ]
print(listaHeterogenea, '\n')

print("""INVERTIR UNA LISTA - METODO reverse() - Significa que elemento 0 será en elemento n, el 1 será el n-1, 2 será el n-2, ..., n-2 será el 2, n-1 será el 1 y n será el 0. Si tener que crear una nueva lista.
listaHomogenea.reverse()
""")
listaHomogenea.reverse()
print(listaHomogenea)
listaHomogenea.reverse()
print(listaHomogenea, '\n')

print("""COPIAR UNA LISTA - METODO copy() - Genera copia completa de una lista
listaCopiada = listaHomogenea.copy() """)
listaCopiada = listaHomogenea.copy()
print(listaCopiada,'\n')


print("""ORDENAR ELEMENTOS DE UNA LISTA - METODO sort() - Ordenamiento puede ser ascendente (sin argumento) o descendente (con argumento)
listaCopiada.sort()
listaCopiada.sort(reverse = True)
listaCopiada.sort(key = len)""")
listaCopiada.sort()
print(listaCopiada, '\n')
listaCopiada.sort(key=len)
print(listaCopiada, '\n')
listaCopiada.sort(reverse = True)
print(listaCopiada, '\n')

print("""CASO EJEMPLO ORDENAR LISTA DE OBJETOS 
class student:
    name = ''
    age = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = student("Sebastián", 23)
s2 = student("Elena", 74)
s3 = student("Leonel", 52)
studentList = [s1, s2, s3]
studentList.sort()        # Genera un error
print("Estudiantes en orden ascendente", end=' ')
studentList.sort(key = lambda s: s.name)
for std in studentList:
    print(std.name, std.age, end=", ")
print("Estudiantes en orden descendente", end=' ')
studentList.sort(key = lambda s: s.name, reverse=True)
for std in studentList:
    print(std.name, std.age, end=", ")   """)
class student:
    name = ''
    age = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = student("Sebastián", 23)
s2 = student("Elena", 74)
s3 = student("Leonel", 52)
studentList = [s1, s2, s3]
# studentList.sort()        # Genera un error
print("Estudiantes en orden ascendente", end=' ')
studentList.sort(key = lambda s: s.name)
for std in studentList:
    # print(std)
    print(std.name, std.age, end=", ")
print("\nEstudiantes en orden descendente", end=' ')
studentList.sort(key = lambda s: s.name, reverse=True)
for std in studentList:
    # print(std)
    print(std.name, std.age, end=", ")

"""  """

print("""\n\nBUSCAR ELEMENTOS EN UNA LISTA - METODO index() - Retorna la posicion de la primera ocurrencia del elemento especificado. Genera valueError si no se encuentra ningún elemento.
listCopiado.index(elemento, intPosIni, intPosFin)  - elemento es obligatorio, intPosIni y intPosFin son opcionales y se usan para buscar en una seccion particular de la lista.
""")
print(listaHomogenea, '\n')

print("""EXTENDER UNA LISTA - METODO extend() - Agrega elementos completa desde un objeto iterable (list, tupla, set, dictionary, string). Se diferencia de append en que agrega elementos del objeto iterable al final de la lista mientras que append agrega todo el objetoIterable como un elemento al final de la lista. Puede usarse el operador + en las operaciones de extension
listaCopiada.extend(listaHomogenea) 
listaCopiada += listaHomogenea 
print("Lista actualizada: ", listaCopiada)
tupla = ('Delhi', "Chicago", "Quito")
listaCopiada.extend(tupla)
print("Lista actualizada: ", listaCopiada)
seT = {"1° Set", "2° Set"}
listaCopiada.extend(seT)
listaCopiada += seT
print("Lista actualizada: ", listaCopiada)
diccionario = {'clave1':'valor de clave 1', 'clave2':'valor de clave 2'}
listaCopiada.extend(diccionario)
print("Lista actualizada: ", listaCopiada)
numeros = [10, 20]
numeros.extend(range[30, 100, 10])
print(numeros)
""")
listaCopiada.extend(listaHomogenea)
print("Lista actualizada: ", listaCopiada)
tupla = ('Delhi', "Chicago", "Quito")
listaCopiada.extend(tupla)
print("Lista actualizada: ", listaCopiada)
seT = {"1° Set", "2° Set"}
# listaCopiada.extend(seT)
listaCopiada += seT
print("Lista actualizada: ", listaCopiada)
diccionario = {'clave1':'valor de clave 1', 'clave2':'valor de clave 2'}
listaCopiada.extend(diccionario)
print("Lista actualizada: ", listaCopiada,'\n')
nums = [10, 20]
nums.extend( range(30, 100, 10) )
print(nums)

print("""SUMAR ELEMENTOS DE UNA LISTA - METODO sum(), max(), min() - Revisar que no exista un nombre de variable sum definido en ninguna parte del codigo.
sum(objetoIterable [, intValorInicial])
print(sum(nums))
print(sum(nums, 10)) 
""")
print("lista nums es un objeto invocable: ",callable(nums))
print(sum(nums))
print(sum(nums), 10)
print(max(nums))
print(min(nums),'\n')

print("""CONVERTIR OBJETOS ITERABLES A LISTAS - CONSTRUCTOR list() 
list()  Crea una lista vacia []
listaResultante = list(objetoIterable)  objetoIterable puede ser string, tupla, set o dictionary 
list(range(0, 100, 10))""")
print(list(range(0, 100, 10)),'\n')

print("MATRICES")
matrix = [ [1, 20, 300], [4, 50, 600], [7, 80, 900] ]
maxlen = 0
nfilas = 0
ncolumnas = 0
nfilas = len(matrix)
for filas in matrix:
    if (ncolumnas == 0):
        ncolumnas = len(filas)
    else:
        if (ncolumnas != len(filas)):
            ncolumnas = -1
    for columnas in filas:
        if maxlen < len(str(columnas)) :
            maxlen = len(str(columnas))
if maxlen % 2 == 0:
    maxlen += 1
else:
    maxlen += 2
for filas in matrix:
    print('|', end="")
    for columna in filas:
        print(str(columna).rjust(maxlen," "),end=" |")
    print('')
print(f"Matriz de dimención {nfilas} x {ncolumnas}\n")

print("""DICCIONARIOS - Son objetos iterables y mutables que pueden ser usados en un ciclo for, puede contener homogeneidad o heterogeneidad, contener listas otro diccionario, numeros, string, tuplas. Si se duplica claves entonces se modifica la previa. Luego de : siempre debe ir un espacio
dictionaryEmpty = {}
diccionario = { key1: elemento1 [, key2: elemento2 [, keyN: elementoN]]}
simple = {"a": 1, "b": 2, "c": 3, "d": "Hola", "a": 3}
diccionarioHeterogeneo = {"nom": "Sebastián", "edad": 23, "pi": 3.1416, "estatura": 1.83, "verdad": True}""")
dictionaryEmpty = {}
diccionarioHeterogeneo = {"nom": "Sebastián", "edad": 23, "pi": 3.1416, "estatura": 1.83, "verdad": True}
diccionarioHomogeneo = {"a": 1, "b": 2, "c": 3, "d": 8, "a": 3}
dictionaryList = {"a": [1,2,3],"b": [4,5,6], "c": diccionarioHeterogeneo}
dictionaryKeysNum = {4: 1, 5: 2, 6: 3, 100: "cien"}
dictionaryRepeatedKeys = {"a": 1, "b": 2, "c": 3, "a": 28}
print(f"Diccionario vacio {dictionaryEmpty}")
print(f"Diccionario homogeneo {diccionarioHomogeneo}")
print(f"Diccionario heterogeneo {diccionarioHeterogeneo}")
print(f"Diccionario de listas {dictionaryList}")
print(f"Diccionario de claves numericas {dictionaryKeysNum}")
print(f"Diccionario de claves repetidas {dictionaryRepeatedKeys}")
print(type(diccionarioHeterogeneo))
print(isinstance(diccionarioHeterogeneo, dict),'\n')

print("""ACCEDER A LOS ELEMENTOS DE UN DICCIONARIO
diccionario[key]
dictionaryList["a"][2]
dictionaryList["c"]["nom]""")
print(f"Diccionario de listas dictionaryList['a'][2] {dictionaryList['a'][2]}")
print(f"Diccionario de listas dictionaryList['c'] {dictionaryList['c']}")
print(f"Diccionario de listas dictionaryList['c']['nom'] {dictionaryList['c']['nom']}",'\n')

print("""70. ACCEDER A LOS ELEMENTOS DE UN DICCIONARIO - Método items()
Ante desconocimiento de claves de un diccionario se tienen los metodos items(), keys() y values().
items() - Devuelve todos los elementos del diccionario como una lista de tuplas. Permitiendo acceder a diferentes partes del diccionario y trabajar con ellas de forma independiente.
El par clave valor se lo conoce como item
diccionarioHomogeneo.items()    Genera una lista de tuplas como sigue:
dict_items([('a', 3), ('b', 2), ('c', 3), ('d', 8)])
list( diccionarioHomogeneo.items() ) mediante el constructor list se obtiene la lista de tuplas """)
print( dictionaryList.items() )
print( list( diccionarioHomogeneo.items() ) )
listItems = list( diccionarioHomogeneo.items() )
print( f"Item del diccionario de la posicion 2 {listItems[1]}" )
tupla = listItems[1]
for i in tupla :
    print(i)
print()


print("""71 ACCEDER A LOS ELEMENTOS DE UN DICCIONARIO - Método keys()
Obtiene lista de todas las claves del diccionario como objeto list
diccionarioHomogeneo.keys()    Genera una lista de keys pero se debe usar el constructor list 
  dict_keys(['a', 'b', 'c', 'd'])  Para convertir a lista se usa el constructor list
list( diccionarioHomogeneo.keys() ) """)
print(diccionarioHomogeneo.keys())
print( list( diccionarioHomogeneo.keys() ))
listKeys = list( diccionarioHomogeneo.keys() )
for i in listKeys :
    print(i)
print()


print("""72 ACCEDER A LOS ELEMENTOS DE UN DICCIONARIO - Método values()
Obtiene lista de todas los valores del diccionario como objeto list
diccionarioHomogeneo.values()    Genera una lista de valores pero se debe usar el constructor list 
  dict_values([3, 2, 3, 8])
list( diccionarioHomogeneo.values() )  """)
print(diccionarioHomogeneo.values())
print( list( diccionarioHomogeneo.values() ))
listValues = list( diccionarioHomogeneo.values() )
for i in listValues :
    print(i)
print()


print("""73 DICCIONARIO - Método clear()
Eliminar todos los items o elementos, aplica a List, Set y Dictionary.
Produce o retorna un diccionario vacio {}
dictionaryKeysNum.clear()  """)
dictionaryKeysNum.clear()
print()

print("""74 MODIFICAR Y AGREGAR ELEMENTOS A UN DICCIONARIO
diccionarioHomogeneo["b"] = ['lunes', 'martes', 'miercoles', {'keyA': 'valorA', 'keyB': 77}]  
diccionarioHomogeneo['f'] = 1024    Clave e no existe, lo agrega al final """)
diccionarioHomogeneo["b"] = ['lunes', 'martes', 'miercoles', {'keyA': 'valorA', 'keyB': 77}]
diccionarioHomogeneo['f'] = 1024
diccionarioHomogeneo['e'] = 1023
print(diccionarioHomogeneo,'\n')

print("""75 DICCIONARIO - Método copy()
Crea una copia de un objeto como listas, matrices o diccionarios. Se puede modificar el objeto copiado sin afectar al objeto original.
dicCopy = diccionarioHomogeneo.copy()
dicCopy["f"] = 1024 * 28    """)
dicCopy = diccionarioHomogeneo.copy()
dicCopy["f"] = dicCopy["f"] * 28
print(f"original {diccionarioHomogeneo} -> copia con modificaciones {dicCopy}","\n")

print("""76 DICCIONARIO - Método fromkeys()
Crea diccionario nuevo con claves de una secuencia dada y valores previamente establecidos.
La palabra dict crea objetos de tipo diccionario o puede usarse en su lugar {}.
fromkeys() - requiere min 1 y max 2 parametros, (sequence) secuencia de claves, (value) valor preestablecido para todas las claves.
  name_dic = dict.fromkeys(sequence [, value])
  name_dic = {}.fromkeys(sequence [, value])
La sequence puede ser un String, una lista o un diccionario, en caso de ser un diccionario toma solo las claves e ignora los valores. Si fuera un String al ser iterable generaria tantos elementos como caracteres contenga el string
  sequence = ["uno","dos","tres"]
  name_dic = dict.fromkeys(sequence)  Generando un diccionario con tres elementos cada uno con value None
    {'uno': None, 'dos': None, 'tres': None}
  name_dic = dict.fromkeys(sequence, [1,2,3])  Generando un diccionario con tres elementos cada uno con el mismo value osea una lista de tres elementos
    {'uno': [1, 2, 3], 'dos': [1, 2, 3], 'tres': [1, 2, 3]}
  sequence = "Hola mundo cruel"
  name_dic = dict.fromkeys(sequence, 5)
    {'H': 5, 'o': 5, 'l': 5, 'a': 5, ' ': 5, 'm': 5, 'u': 5, 'n': 5, 'd': 5, 'c': 5, 'r': 5, 'e': 5}  """)
sequence = ["uno","dos","tres"]
name_dic = {}.fromkeys(sequence)
name_dic = dict.fromkeys(sequence)
print(name_dic)
name_dic = dict.fromkeys(sequence, [1,2,3])
print(name_dic)
sequence = "Hola mundo cruel"
name_dic = dict.fromkeys(sequence, 5)
print(name_dic,'\n')

print("""77 DICCIONARIO - Método get()
Obtener valores asociados a cada clave, evita errores de KeyError en cuyo caso retorna valor previamente establecido o simplemente palabra None. Es mas eficiente que el uso de condicional para verificar si clave existe antes de obtener el valor. Dos parametros, la clave y un valor por defecto opcional. 
  diccionario.get( key [, valor_Default_caso_no_existe_clave])
  name_dic.get("H", "No existe la clave")
  name_dic.get("cinco", "No existe la clave")
""")
print( name_dic.get("H", "No existe la clave") )
print( name_dic.get("cinco", "No existe la clave"), '\n' )

print("""78 DICCIONARIO - Método popitem()
Elimina y retorna (como una tupla de dos elementos) el último par clave-valor (item) agregado.
El primer elemento de la tupla corresponde a clave y el segundo a valor. """)
print(name_dic)
tupla = name_dic.popitem()
print(f"diccionario luego de popitem {name_dic}, contenido de tupla = {tupla} es tupla[0] = {tupla[0]} : tupla[1] = {tupla[1]}",'\n')


print("""79 COMO USAR EL METODO pop() CON DICCIONARIOS
Eliminar y devolver un elemento de una lista, diccionario o conjunto. Puede trabajar con valor predeterminado de retorno para evitar Keyerror cuando clave no se encuentre. Con list los pop no requerian argumentos.
  name_dic.pop( key [, valor_Default_caso_no_existe_clave])
  name_dic.pop('d', "No existe el elemento")    retorna el value existente en la clave 'd' o el texto en caso de no existir la clave
""")
print(name_dic)
print( name_dic.pop('d', "No existe el elemento") )
print(name_dic)
itemval = name_dic.pop('rafar', "No existe el elemento")
print(itemval,'\n')

print("""80 DICCIONARIO - Método setdefault()
Crea una clave con el valor para esa clave, si la clave no existe y en caso que la clave ya existe entonces devuelve el valor correspondiente a dicha clave.
name_dic.setdefault(key [,calor])
name_dic.setdefault('o')      Retorna 5
name_dic.setdefault('none')   Clave no existe, retorna None
name_dic.setdefault('o', 83)  Si key 'o' no existe asigna 83 y retorna 83, caso contrario retorna 5 no modifica su valor
name_dic.setdefault('z', 71)  Si key 'z' no existe asigna 71 al final del dic y retorna 71  
valKey = name_dic.setdefault('x', 69)  """)
name_dic.setdefault('o')
name_dic.setdefault('o', 83)
name_dic.setdefault('z', 71)
print(name_dic,'\n')

print("""81 DICCIONARIOS - Método update()
Actualiza o agrega elementos, acepta un diccionario como argumento y luego agrega o actualiza los elementos en el diccionario original, cautela dado que se pueden escribir claves en el original
  name_dict.update( diccionarioMontar )
Se tiene un dict name_dic
  {'H': 5, 'o': 5, 'l': 5, 'a': 5, ' ': 5, 'm': 5, 'u': 5, 'n': 5, 'c': 5, 'r': 5, 'z': 71}
  name_dic.update({'H': 73, 'a':-101, 'y':2048})  
modifica valor de las claves 'H', 'a' y agrega la clave 'y' al final del dic name_dic
  {'H': 73, 'o': 5, 'l': 5, 'a': -101, ' ': 5, 'm': 5, 'u': 5, 'n': 5, 'c': 5, 'r': 5, 'z': 71, 'y': 2048 """)
name_dic.update({'H': 73, 'a':-101, 'y':2048})
print(name_dic, '\n')

print("""82 DICCIONARIOS - CICLO for - RECORRER UN DICCIONARIO
for key in name_dic :
    print(f"{key} : {name_dic[key]}")  """)
for key in name_dic :
    print(f"{key} : {name_dic[key]}")
print()
"""
with open('./assets/python_course/recursos/dog_breeds_reversed.txt', 'w') as writer:
    writer.write(f"tipo archivo de texto escrito")
"""

sourceFile = open('./assets/python_course/recursos/archivo escrito desde python.txt', 'w+')
#with sourceFile as escritor:
#    escritor.write(f"tipo sourceFile de texto escrito Nuevo {type(sourceFile)}\n")
print(f"Escribiendo en archivo de Texto type(sourceFile)  {type(sourceFile)}  {sourceFile.encoding}", file = sourceFile)
print(f"""Referenciando la ruta relativa del archivo mediante el comando 
  sourceFile = open('./assets/python_course/recursos/archivo escrito desde python.txt', 'w+')""", file = sourceFile)
print(f"Referencia en https://realpython.com/read-write-files-python/#opening-and-closing-a-file-in-python", file = sourceFile)
sourceFile.close

sourceFile = open('./assets/python_course/recursos/archivo escrito desde python.txt', 'a+')
print(f"Dentro del mismo archivo se puede agregar lineas usando el modo a", file = sourceFile)
print(f"Confirmandose que esta linea se agrega al final", file = sourceFile)
print(f"""Notese que el comando es similar con la diferencia del modo 
  sourceFile = open('./assets/python_course/recursos/archivo escrito desde python.txt', 'a+')""", file = sourceFile)
sourceFile.close