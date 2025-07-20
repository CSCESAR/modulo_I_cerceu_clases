"""
Reconocimiento del tipo de adto

"""
nombre = "Luis"
ciudad = "Lima"
saldo = 5000
empresa = False
correo = "luis@gmail.com"
empleado = [nombre,saldo,correo,ciudad,empresa]
empleado_4 = {'nombre':nombre,'ciud':ciudad,'sald':saldo,'corr':correo}

print("El tipo de datos de mi variable 'nombre' es {}".format(type(nombre)))
print("El tipo de datos de mi variable 'ciudad' es {}".format(type(ciudad)))
print("El tipo de datos de mi variable 'saldo' es {}".format(type(saldo)))
print("El tipo de datos de mi variable 'empresa' es {}".format(type(empresa)))
print("El tipo de datos de mi variable 'correo' es {}".format(type(correo)))
print("El tipo de datos de mi variable 'empleado' es {}".format(type(empleado)))
print("El tipo de datos de mi variable 'empleado_4' es {}".format(type(empleado_4)))
