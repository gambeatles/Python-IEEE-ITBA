# Realizar un programa para controlar el sistema de impresión de etiquetas con códigos de barras en un supermercado. 
# Primero se debe ingresar la cantidad de productos diferentes que necesitan etiquetas. 
# Luego, para cada producto, se ingresa el código a imprimir y la cantidad de veces que hay que imprimirlo. 
# Posteriormente el programa imprimirá dicho código.

# Imprimir en pantalla los códigos solicitados la cantidad requerida de veces.

# Ejemplo:

# Las líneas indicadas con >> corresponden a Inputs. Las líneas sin indicaciones corresponden a Outputs:
# >> 3 (cantidad total de productos)
# >> 000000123 (primer código)
# >> 1 (veces que hay que imprimir dicho código)
# 000000123
# >> 123000789 (segundo código)
# >> 3
# 123000789
# 123000789
# 123000789
# >> 000031416 (tercer código)
# >> 2
# 000031416
# 000031416

# Observación:

# Los códigos se imprimen a medida que se ingresan, no es necesario guardar todos los códigos 
# y sus cantidades e imprimirlos al final de la ejecución.

productos = int(input("Cantidad de productos : "))
while productos != 0:
  codigo = int(input("Ingrese codigo : "))
  cantidad = int(input("Ingrese cantidad de impresiones : "))
  for etiqueta in range(1,cantidad + 1,1):
    print(codigo)
  productos -= 1
