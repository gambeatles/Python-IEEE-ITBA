# Estructura for

for x in range(0,15,5):
    print(x)
    
for x in range(0,10,2):
    print(x)
    
init = int(input("Ingrese el inicio:"))
fin = int(input("Ingrese el fin:"))
step = int(input("Ingrese el salto:"))

for x in range(init, fin, step):
    print("x =", x)

print("range(5):")
for x in range(5):
    print(x)

print("range(10, 15):")
for x in range(10, 15):
    print(x)

