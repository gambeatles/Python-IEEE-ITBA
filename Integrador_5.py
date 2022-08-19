# Adivina adivinador
# Se rumorea que al rector de una universidad le apasiona adivinar números. Cuando se cruza a alguien, 
# ya sean alumnos o profesores, les pide que piensen un número. 
# Luego, intenta adivinarlo mientras el alumno le indica si el número es mayor, menor o igual 
# al que el rector esta adivinando.

# Ahora les proponemos a ustedes realizar el programa que adivine un número que ustedes elijan, 
# indicándole si los números que este propone son mayores o menores al elegido.

# Ustedes pensarán en un número secreto (para este ejercicio consideremos que el número es menor a 10.000), 
# luego el programa intenta adivinarlo. El usuario debe responder con el símbolo >, < ó =. 
# En el caso de ser igual, el programa termina e imprime la cantidad de intentos que tardó, caso contrario, 
# debe volver a intentar adivinar el número y se repite el procedimiento.

# Desafío: Encontrar la estrategia que puede ejecutar la máquina para adivinar 
# el número en la menor cantidad de intentos posible.

# Adivina adivinador
numero = 203
adivina = int(input("Ingrese un numero : "))
while adivina != numero:
    if adivina > numero:
        print(">")
        adivina = int(input("Ingrese un numero : "))
    elif adivina < numero:
        print("<")
        adivina = int(input("Ingrese un numero : "))
print("=")