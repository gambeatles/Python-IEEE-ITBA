# Cálculo de promedio
# Cálcular la nota de un alumno es una tarea cotidiana de un profesor. 
# Esta tarea suele realizarse a mano o en excel muchas veces. En esta ocasión la haremos en Python.

# Escribir una función que calcule el promedio de 3 notas y entrege ese valor usando return.
# Reescribir la función anterior modificándola para asignar una importancia al primer examen de 20%, 
# al segundo de 50% y al tercero de 30%.
# Llamar a cada función anterior 3 veces con distintas notas y verificar, mediante la instrucción if, 
# si el alumno aprobó en cada caso (suponga que 4 es la nota de aprobación).

#Calculo Promedio
def nota():
  cantidadNotas = 3
  notas = 0
  while cantidadNotas != 0:
    cantidadNotas -= 1
    nota = int(input("Ingrese nota : "))
    notas = notas + nota
  promedio = int(notas / 3)
  return promedio

promedio = nota()
print(promedio)

# Calculo de Promedio Modificado

def notaModificado():
  cantidadNotas = 3
  notas = 0
  while cantidadNotas != 0:
    cantidadNotas -= 1
    nota = int(input("Ingrese nota : "))
    if cantidadNotas == 2:
      nota1 = nota + (nota * 0.2)
    elif cantidadNotas == 1:
      nota2 = nota + (nota * 0.5)
    elif cantidadNotas == 0:
      nota3 = nota + (nota * 0.3)
  notas = nota1 + nota2 + nota3
  promedio = notas / 3
  return promedio

promedio = notaModificado()
print(promedio)