# Test de primalidad
# Escribir una función que recibe un número y devuelve True si el número es primo y False en caso contrario.

# Mediante un for verificar la primalidad de los numeros del 1 al 20, es decir, decidir si cada número es primo o no.

# Tips:

# Un número N es primo cuando tiene exactamente 2 divisores (1 y N).
# Sin embargo, alcanza con verificar que no es múltiplo de ningún número entre 2 y N−−√ (recordar que N−−√=N0.5)
# El numero 1 NO es primo.

# Test de primalidad
def numeroPrimo(numero):
    contador = 0
    for x in range(2,numero + 1,1):
        if numero % x == 0:
            contador +=1

    if numero == 1 or numero == 4 or contador > 2:
        print("El numero no es primo")
    else:
        print("primo")

numeroPrimo(66)