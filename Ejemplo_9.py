# Funciones

def saludar():
    print( "¡Hola! Que tengas un buen día :)")
 
print("A continuación se imprimirán tres saludos:")
saludar()
saludar()
saludar()

def suma(a, b):
    s = a + b
    return s

z = suma(3, 4)
print("3 + 4 =", z)

x = int(input("Ingrese el primer sumando: "))
y = int(input("Ingrese el segundo sumando: "))
z = suma(x, y)
print("x + y =", z)

def chequarContraseña(c):
    if c == "Secreto":
        resultado = True
    else:
        resultado = False
    return resultado


ingresado = input("Ingrese contraseña: ")        
while not chequarContraseña(ingresado):
    ingresado = input("Contraseña incorrecta. Ingrese de nuevo:")
else:
    print("Contraseña correcta.")


