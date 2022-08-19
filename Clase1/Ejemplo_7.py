# Estructura while

x = 1
while x < 10:
    print(x)
    x += 1

print('Termina el while')

print("Continuo con el resto del programa")

print("\n")

nota = int( input('Ingrese un número del 1 al 10: ') )

while nota < 1 or nota > 10:
  print('Fuera de rango!')
  nota = int( input('Ingrese un número del 1 al 10: ') )

print("La nota es mayor a 4?", nota >= 4 )

