# Estructura if

a = 5
b = 6
if a == b:
    print(a)
elif b < 5 or b > 7:
    print(a + b)
else:
    print(b)
    
y = int(input("Ingrese el valor de y :"))
if y == 13:
    print("Adivinamos el valor de y!")      

x = int(input("Ingrese el valor de x :"))    
if x == 93:
    print("Adivinamos el valor de x!")
else:
    print("No adivinamos el valor de x  :(")
    
if x > y:
    print("x es mayor que y")
elif x < y:
    print("y es mayor que x")
elif x == y:
    print("x e y son iguales")
else:
    print("que anda pasando?")