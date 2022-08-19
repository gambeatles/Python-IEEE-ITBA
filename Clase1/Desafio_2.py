# Mini-desafío: Operadores
# Diseñar un programa en el cual el usuario ingrese tres números, uno a la vez, y se muestre a la salida el promedio de los tres números.

# Diseñar un programa en el cual el usuario ingrese tres números, uno a la vez, y se muestre a la salida la media geométrica de los tres números.

# Tip: Usando el operador de potencia se puede calcular una raíz cúbica ya que: x−−√3=x1/3

# Escriba aquí su código para la parte 1
a = int(input("Ingrese el primer numero:"))
b = int(input("Ingrese el segundo numero:"))
c = int(input("Ingrese el tercer numero:"))
promedio = (a + b + c) / 3
print("El promedio es:",promedio)

# Escriba aquí su código para la parte 2
a = int(input("Ingrese el primer numero : "))
b = int(input("Ingrese el segundo numero : "))
c = int(input("Ingrese el tercer numero : "))
media = (a * b * c) ** 1/3
print("La media geometrica es : ",media)