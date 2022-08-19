# 1 Implementar un programa que reciba 2 números (A y B), y luego imprima en pantalla la secuencia de números 
# enteros desde A hasta B. En el caso de que B sea menor que A, 
# se debe repetir el pedido de B hasta que sea válido ( B  ≥  A ).

# 2 Implementar un programa que muestre la siguiente secuencia:

# 1, 2, 3, 4, 5, 4, 3, 2, 1, 0

# Para un desafío mayor: Utilizar 1 solo while, 1 solo if y 1 solo else. 
# Es recomendable que la variable usada para contar los pasos se mantenga contando siempre de la misma forma.

# Escriba aquí su código para la parte 1
numero1 = int(input("Ingrese el primer numero : "))
numero2 = int(input("Ingrese el segundo numero : "))
while numero2 >= numero1:
    print(numero1)
    if numero1 <= numero2:
        numero1 += 1
    else:
        numero2 = int(input("Ingrese el segundo numero : "))

# Escriba aquí su código para la parte 2
contador = 0
numero = 5
while numero != 0:
  contador += 1
  if contador <= 5:
    print(contador)
  else:
    numero -= 1
    print(numero)