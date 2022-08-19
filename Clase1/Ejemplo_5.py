# Operaciones de comparacion

x = 4
print("Es x mayor o igual a 4?", x >= 4)
print("Es x menor a 3?", x < 3)

numero = int(input("Ingrese un numero:"))
y = x > 5 and numero < 7
z = x > 5 or numero < 7
k = not numero > 5
print("x > 5 y x < 7?", y)
print("x > 5 ó x < 7?", z)
print("Es x NO mayor a 5?", k)

numero1 = int(input("Ingrese el primer número:"))
numero2 = int(input("Ingrese el segundo número:"))
j = ( numero1 > 15 or numero1 < -15) and ( numero2 > 15 or numero2 < -15 )
print("El valor absoluto de ambos numeros es mayor a 15?", j)