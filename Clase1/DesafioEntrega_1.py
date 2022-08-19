# La conjetura del Dr. Lothar

# Escriba un programa que reciba un numero del usuario y repita el siguiente proceso usando un while:

# Si el número es par, se debe dividir por  2 .
# Si el número es impar, se debe multiplicar por  3  y sumar  1 .
# Este proceso se repite hasta llegar al numero  1  y luego muestra en pantalla la cantidad de pasos que tardó 
# en llegar.

# Ejemplos:

# Input: 6

# Output: 8 (Los pasos a seguir son: 6, 3, 10, 5, 16, 8, 4, 2, 1)

# Input: 13

# Output: 9 (Los pasos a seguir son: 13, 40, 20, 10, 5, 16, 8, 4, 2, 1)

def esPar(numero):
    if numero % 2 == 0:
        par = True
    else:
        par = False
    return par

def dividirPar(numero):
    division = int(numero / 2)
    return division

def operacionImpar(numero):
    operacion = (numero * 3) + 1
    return operacion

numero = int(input("Ingrese un numero : "))
contador = 0
while numero != 1:
    contador += 1
    verificacion = esPar(numero)
    if verificacion == True:
        numero = dividirPar(numero)
    else:
        numero = operacionImpar(numero)
print(contador)