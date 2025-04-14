
# ejercicio 1
def cantidad_digitos ():
    a = int(input('ingrese un numero entero'))
    cont = 0 
    a = abs(a)
    while a != 0:
        cont += 1
        a = a // 10
    print('cantidad de digitos: ', cont)

def contar_digitos_decimal():
    numero = float(input('ingrese un numero real'))
    
    parte_entera = int(abs(numero))
    parte_decimal = abs(numero) - parte_entera  

    digitos_entera = 0
    if parte_entera == 0:
        digitos_entera = 1
    else:
        while parte_entera > 0:
            parte_entera //= 10
            digitos_entera += 1

    digitos_decimal = 0
    while parte_decimal > 0 and digitos_decimal < 15:  
        parte_decimal *= 10
        entero = int(parte_decimal) 
        parte_decimal -= entero 
        digitos_decimal += 1
    
        if parte_decimal < 1e-10:  
            break

    print(f'parte entera {digitos_entera}, parte decimal {digitos_decimal}')

def cargar_vector():
    n = int(input('ingrese el tamanio del vector'))
    vector = []
    for i in range(n):
            digito = int(input(f"Ingrese el {i+1}-ésimo dígito: "))
            vector.append(digito)
    return vector

def es_compuesto(numero):
    if numero < 2:
        return False
    divisores = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores += 1
        if divisores > 2:
            return True
    return False

def numeros_compuestos():
    vector = cargar_vector()
    rto = [num for num in vector if es_compuesto(abs(num))]
    print (rto)

def invertir_con_auxiliar(vector):
    auxiliar = []
    for i in range(len(vector)-1, -1, -1): 
        auxiliar.append(vector[i])

def invertir_sin_auxiliar(vector):
    inicio = 0
    fin = len(vector) - 1
    while inicio < fin:
        vector[inicio], vector[fin] = vector[fin], vector[inicio]
        inicio += 1
        fin -= 1
    return vector

def ejercico_4 ():
    vector = cargar_vector()
    
    invertido = invertir_con_auxiliar(vector)
    print("Vector invertido (con auxiliar):", invertido)
    
    invertido = invertir_sin_auxiliar(vector)
    print("Vector invertido (sin auxiliar):", invertido)

def es_par(digito):
    return int(digito) % 2 == 0

def es_impar(digito):
    return int(digito) % 2 != 0

def filtrar_lista():
    A = cargar_vector()
    B = []
    for num in A:
        parte_entera = str(int(abs(num)))  
        pares = parte_entera
        digitos_pares = 0
        for digito in pares:
            if (int(digito) % 2) == 0:
                digitos_pares += 1 
        
        impares = parte_entera
        digitos_impares = 0
        for digito in impares:
            if (int(digito) % 2) == 1:
                digitos_impares += 1 
        print(digitos_impares)

        if digitos_pares == 2 and digitos_impares >= 2:
            B.append(num)
    
    print("Lista B:", B)

def insertar_k_derecha():
    lista = cargar_vector()
    K = int(input('Ingrese el numero k:'))
    i = 0
    while i < len(lista):
        if lista[i] % K == 0:
            lista.insert(i + 1, K) 
            i += 1 
        i += 1
    print (lista)

def cargar_matriz():
    M = int(input("Ingrese el número de filas (M): "))
    N = int(input("Ingrese el número de columnas (N): "))
    matriz = []
    for i in range(M):
        fila = []
        print(f"Ingrese los elementos de la fila {i+1}:")
        for j in range(N):
            elemento = float(input(f"Ingrese el elemento de la columna {j+1}: "))
            fila.append(elemento)
        matriz.append(fila)
    return matriz

def calcular_promedios(matriz):
    M = len(matriz)      
    N = len(matriz[0])   
    promedios_filas = [sum(fila) / N for fila in matriz]
    promedios_columnas = []
    for j in range(N):
        suma_columna = sum(matriz[i][j] for i in range(M))
        promedios_columnas.append(suma_columna / M)
    return promedios_filas, promedios_columnas

def mostrar_matriz_y_promedios():
    matriz = cargar_matriz()
    print("Matriz:")
    for fila in matriz:
        print(fila)
    promedios_filas, promedios_columnas = calcular_promedios(matriz)
    print("\nPromedios de las filas:")
    for i, promedio in enumerate(promedios_filas):
        print(f"Fila {i+1}: {promedio}")
    print("\nPromedios de las columnas:")
    for j, promedio in enumerate(promedios_columnas):
        print(f"Columna {j+1}: {promedio}")

def calcular_suma_diagonal_principal(matriz):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][i]
    return suma

def calcular_factorial(n):
    if n == 0 or n == 1:
        return 1
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial

def obtener_vector_factorial():
    matriz = cargar_matriz()
    if(len(matriz))== len(matriz[0]):
        vector = []
        suma_diagonal = calcular_suma_diagonal_principal(matriz)
        for fila in matriz:
            for elemento in fila:
                if calcular_factorial(elemento) >= suma_diagonal:
                    vector.append(elemento)
    else:
        vector = "la matriz no es cuadrada"
    print(vector)

def es_punto_silla(matriz, k, h):
    elemento = matriz[k][h]
    es_mayor_en_fila = True
    for j in range(len(matriz[k])):
        if matriz[k][j] > elemento:
            es_mayor_en_fila = False
            break
    es_menor_en_columna = True
    for i in range(len(matriz)):
        if matriz[i][h] < elemento:
            es_menor_en_columna = False
            break
    return es_mayor_en_fila and es_menor_en_columna

def ejercicio_9():
    print("--- Cargar matriz ---")
    matriz = cargar_matriz()
    print("\n--- Matriz cargada ---")
    for fila in matriz:
        print(fila)
    k = int(input("\nIngrese la fila del elemento a verificar (k): "))
    h = int(input("Ingrese la columna del elemento a verificar (h): "))
    if es_punto_silla(matriz, k, h):
        print(f"El elemento A[{k}, {h}] es un punto silla.")
    else:
        print(f"El elemento A[{k}, {h}] no es un punto silla.")

def es_simetrica(matriz):
    N = len(matriz)
    M = len(matriz[0])
    if N != M:
        return False
    for i in range(N):
        for j in range(i+1, N):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

def ejercicio_10():
    matriz = cargar_matriz()
    if es_simetrica(matriz):
        print("\nLa matriz es simétrica.")
    else:
        print("\nLa matriz no es simétrica.")

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Ejercicio 4")
    print("5. Ejercicio 5")
    print("6. Ejercicio 6")
    print("7. Ejercicio 7")
    print("8. Ejercicio 8")
    print("9. Ejercicio 9")
    print("10. Ejercicio 10")
    print("11. Salir")

def menu ():
    while True:
        mostrar_menu()
        op = int(input("Seleccione una opción (1-6): "))
        match op:
            case 1:
                cantidad_digitos()
            case 2:
                contar_digitos_decimal()
            case 3:
                numeros_compuestos()
            case 4:
                ejercico_4()
            case 5:
                filtrar_lista()
            case 6:
                insertar_k_derecha()
            case 7:
                mostrar_matriz_y_promedios()
            case 8:
                obtener_vector_factorial()
            case 9:
                ejercicio_9()
            case 10:
                ejercicio_10()
            case 11:
                break
            case _: print("Opción no válida. Por favor, ingrese un número entre 1 y 11.")
menu()
