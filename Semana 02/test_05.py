"""
Tipo de datos
Boolean: bool
"""
var1 = True
var2 = False
var3 = True
var4 = 0 #El resultado es false por lo tanto no se imprimirá
var5 = 10
print("El valor de mi variable var1 es:{}.".format(var1))
print("El valor de mi variable var2 es:{}.".format(var2))

if var2:
    print("¡Hola Pythonista!")
if var3:
    print("Hola Mundo")
    print("2025")
if var1:
    print("Bienvendos Pythonista")
if var4:
    print("Ingreso al caso del var4")
if var4 > var5:
    print("Ingreso al ultimo caso")
