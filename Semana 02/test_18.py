"""
Requisitos
1. Crear 2 variables enteras, 2 varaibles flotanes, 2 variable string, 1 variables string con contenido netamente
numérico y una variable boolean
2. Obtener y mostrar la suma de una variable entera con la variable string numérica
(Conversiones, realizarla si fuera necesario)
3. Obtener y mostrar la suma de las 2 variables enteras más la variable string numérica y la variable flotantes
4. Obterner y mostrar el módulo de las variables enteras: %
5. Obtener y mostrar el resultado o la parte entera de las 2 variables int: //
6. Obtener una potencia usando una de las variables foltantes como base y la variable entera como pontencia

Nota: Las variables string pueden ser tu nombre y apellido

Hora de entrega máxima : 7pm
Correo: docente.cerseu.unmsm@gmail.com
Asunto: Ejercicio Participación - Semana 02
Adjuntar archivo .py
En la parte superior dejar su nombre y apellido: como comentario

Adjuntar versión de git a su correo: WIN+R, escribir CMD y enter -> git --version

"""


# 1. Variables requeridas
var_int_1 = 10
var_int_2 = 4

var_float_1 = 2.5
var_float_2 = 7.8

nombre = "César"
apellido = "Chambi"
nombre_completo = nombre + " " + apellido

var_str_num = "15"
activo = True

# 2. Suma (entero + string numérico)
suma1 = var_int_1 + int(var_str_num)
print("2. Suma entero + string numérico: {}".format(suma1))

# 3. Suma (entero + entero + string numérico + flotante)
suma2 = var_int_1 + var_int_2 + int(var_str_num) + var_float_1
print("3. Suma total: {}".format(suma2))

# 4. Módulo (entero % entero)
modulo = var_int_1 % var_int_2
print("4. Módulo: {}".format(modulo))

# 5. División_entera(entero // entero)
division_entera = var_int_1 // var_int_2
print("5. División entera: {}".format(division_entera))

# 6. Potencia (flotante ** entero) ó pow(flotante,entero)
potencia = pow(var_float_1,var_int_2)
print("6. Potencia: {}".format(potencia))
