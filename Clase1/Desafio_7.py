# 1 Escribir una función que chequee los siguientes usuarios y contraseñas:
# Usuario: Juan

# Contraseña: 12345_

# Usuario: Pablo

# Contraseña: xDcFvGbHn

# La función debe recibir como parámetros el usuario y la contraseña, y debe devolver el valor True o False.

# 2 Escribir una función que recibe un número N y retorna la cantidad de divisores del mismo.

# Ejemplos:

# contarDivisores(9) → 3 (El número 9 tiene 3 divisores: 1, 3, 9)

# contarDivisores(10) → 4 (El número 10 tiene 4 divisores: 1, 2, 5, 10)

# Escriba aquí su código para la parte 1
def chequear(usuario,contrasenia):
  if usuario == "Juan" and contrasenia == "12345_":
    return True
  elif usuario == "Pablo" and contrasenia == "xDcFvGbHn":
    return True
  else:
    return False

user = input("Ingrese usuario : ")
password = input("Ingrese contrasenia : ")
resultado = chequear(user,password)
print(resultado)

# Escriba aquí su código para la parte 2
def contarDivisores(numero):
  contador = 0
  for x in range(1,numero + 1,1):
    if numero % x == 0:
      contador += 1
  return contador

numero = int(input("Ingrese un numero : "))
cantidadDivisores = contarDivisores(numero)
print(cantidadDivisores)

