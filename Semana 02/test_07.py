"""
Requisitos:

1. Crear dos varaibles para los valores de nombre, profesión y ciudad
2. Crear 2 varialbes para la remuneración de enero y febrero (más de 1500)
3. Crear 1 variable donde se sumará el ingreso de los dos meses de enero y febrero
4. Mostrar en pantalla el mensaje de:

"Hola soy 'nombre' mi profesión es 'profesión' y mi remnuneración acumulada es de 'remuneracion_total''"
"""

#Requisito 1 - nombre, profesion y ciudad
nombre = "Juan Perez"
profesion = "Abogado"
ciudad = "Lima"

# Requisito 2
r_enero = 1800.50
r_febrero = 1750.75

#Requisito 3 - suma de los meses
r_total = r_enero + r_febrero

#Requisito 4 - Mostrar mensaje
print("Hola soy {}, mi profesion es {} y mi remuneración acumulada es de {}".format(nombre, profesion, r_total))
