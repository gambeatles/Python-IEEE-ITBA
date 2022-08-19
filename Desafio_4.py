# 1 Realizar un programa que revise si una nota está aprobada (es decir si es mayor o igual a 4) utilizando un if/else. La nota será ingresada por el usuario usando input().

# 2 Realizar un programa que convierta una nota porcentual del 0 al 100 a una letra entre A y F de acuerdo a la siguiente conversión:

# A: 90–100

# B: 80–89

# C: 70–79

# D: 60–69

# F: 0–59

# Escriba aquí su código para la parte 1
nota = int(input("Ingrese la nota : "))
if nota >= 4:
  print("Aprobo")
else:
  print("No Aprobo")
  
# Escriba aquí su código para la parte 2
nota = int(input("Ingrese la nota"))
if nota >= 90 and nota <= 100:
  print("A")
elif nota >= 80 and nota <= 89:
  print("B")
elif nota >= 70 and nota <= 79: 
  print("C")
elif nota >= 60 and nota <= 69: 
  print("D")
elif nota >= 0 and nota <= 59: 
  print("F")