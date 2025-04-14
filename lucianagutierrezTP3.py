
# Actividad Nº3 - Taller de Programación
# Ejercicio 1: Valor máximo entre tres números
def maximo_tres(a, b, c):
    return max(a, b, c)

# Ejercicio 2: Valor máximo entre 10 números
def maximo_diez(lista):
    maximo = maximo_tres(lista[0], lista[1], lista[2])
    for i in range(3, len(lista)):
        maximo = max(maximo, lista[i])
    return maximo

# Ejercicio 3: Operaciones con vectores
def cargar_vector(n):
    return [int(input(f"Ingrese número {i+1}: ")) for i in range(n)]

def suma_vector(v):
    return sum(v)

def suma_vectores(v1, v2):
    return [v1[i] + v2[i] for i in range(len(v1))]

# Ejercicio 4: Contar vocales y consonantes
def contar_vocales(palabra):
    return sum(1 for c in palabra.lower() if c in 'aeiou')

def contar_consonantes(palabra):
    return sum(1 for c in palabra.lower() if c.isalpha() and c not in 'aeiou')

# Ejercicio 5: Menú de opciones numéricas
def potencia(x, k):
    return x ** k

def contar_digitos(x):
    return len(str(abs(x)))

def es_capicua(x):
    x_str = str(x)
    return x_str == x_str[::-1]

# Ejercicio 6: Operaciones con matrices
def cargar_matriz(m, n):
    return [[int(input(f"M[{i}][{j}]: ")) for j in range(n)] for i in range(m)]

def suma_matrices(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def producto_matrices(a, b):
    return [[a[i][j] * b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def mostrar_matriz(m):
    for fila in m:
        print(fila)

# Ejercicio 7: Matriz y vector de factoriales
import math

def suma_diagonal_principal(matriz):
    return sum(matriz[i][i] for i in range(len(matriz)))

def factoriales_mayores(matriz, suma_diag):
    vector = [x for fila in matriz for x in fila if math.factorial(x) >= suma_diag]
    return sorted(list(set(vector)))

# Ejercicio 8: Manejo de electrodomésticos
def cargar_electrodomesticos():
    matriz = []
    while True:
        nombre = input("Nombre: ")
        proveedor = input("Proveedor: ")
        precio = input("Precio: ")
        stock = input("Stock: ")
        if precio.isdigit() and stock.isdigit():
            matriz.append([nombre, proveedor, precio, stock])
        if input("¿Continuar? (s/n): ") != 's':
            break
    return matriz

def mostrar_por_proveedor(matriz, proveedor):
    for item in matriz:
        if item[1] == proveedor:
            print(item[0])

def menor_precio(matriz):
    return min(matriz, key=lambda x: int(x[2]))

def stock_positivo(matriz):
    return [item for item in matriz if int(item[3]) > 0]

# Ejercicio 9: Lista de espera en consultorio
def ingresar_paciente(lista, nombre, urgencia=False):
    if urgencia:
        lista.insert(0, nombre)
    else:
        lista.append(nombre)

def atender_paciente(lista):
    if lista:
        return lista.pop(0)

def pacientes_antes(lista, nombre):
    return lista.index(nombre) if nombre in lista else -1

# Ejercicio 10: Máquina tragamonedas
import random

def rotar(vector, posiciones):
    return vector[posiciones:] + vector[:posiciones]

def jugar_tragamonedas():
    simbolos = ['O', 'X', '7']
    rodillos = [[random.choice(simbolos) for _ in range(9)] for _ in range(3)]
    giros = [random.randint(0, 9) for _ in range(3)]
    rodillos = [rotar(rodillos[i], giros[i]) for i in range(3)]
    resultado = [rodillo[0] for rodillo in rodillos]
    if resultado == ['X', 'X', 'X']:
        print("Ganó 10 fichas")
    elif resultado == ['O', 'O', 'O']:
        print("Ganó 100 fichas")
    elif resultado == ['7', '7', '7']:
        print("Ganó 1000 fichas")
    else:
        print("Sin premio")
