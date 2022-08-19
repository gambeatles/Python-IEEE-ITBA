# Una buena e-stimación
# El número e tiene inmensa utilidad para el análisis y la estadística, 
# es una de las super-estrellas de la matemática, y su utilidad radica en que la función ex es igual a su derivada, 
# por definición de e.

# Gracias a las series de Taylor podemos obtener la siguiente definición del número e:

# e=1+11!+12!+13!+14!+15!+...

# Se pide obtener una aproximación del número e calculando la suma de los primeros 20 términos de esta serie.

# Tips:

# n!=1⋅2⋅3⋅ ... ⋅n.

# Aproximacion de e
n = 21
suma = 0
factorial = 1
for x in range (1,n,1):
  factorial = factorial * x
  division = 1/factorial
  suma = suma + division
e = 1 + suma
print(e)