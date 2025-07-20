"""
1. crea 4 varialbles  entre enteros, floats, booleans
2. Realizar el uso de condicionlales de las variable para dos casos true y 2 casos false
3. En casos de True imprimir el valor de las otras 2 variables
4. En dos condicionales compararlo con un numero
"""
# Requisito 1: Variables
edad = 30
altura = 1.75
experiencia = True
estudiante = False

# Requisito 2- Condicionales
# para true imprime lo otro
if experiencia: # True
    print("Tiene experiencia laboral, Edad: {}, Altura: {}".format(edad, altura))

if edad > 25:  # True
    print("Edad mayor a 25 años, tiene experiencia: {}, Es estudiante:{}".format(experiencia, estudiante))

if estudiante: # False
    print("Es estudiante.")

if altura < 1.50:  # False
    print("Altura menor a 1.50.")
