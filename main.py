# La patente: una cadena de caracteres). Recuerde que se asume que no necesariamente
# tendrá 7 caracteres, pero que no contendrá tampoco blancos ni letras minúsculas, ni
# caracteres diferentes de letras y números. Observe no obstante que incluso teniendo
# 7 caracteres podría no ser una placa válida para ninguno de los cinco países
# (y esto SÍ puede ocurrir en este trabajo).

# El tipo de vehículo: un número entero entre 0 y 2 que indica alguno de los siguientes tipos de vehículos:
# (0: motocicleta, 1: automóvil, 2: camión).

# La forma de pago: un número entero que indica alguno de los dos siguientes
# tipos de pago: (1: manual, 2 telepeaje).

# País: un número entero entre 0 y 4 para indicar el país donde está la cabina atravesada
# (asúmalos en el orden que prefiera).

# Distancia: Un número en coma flotante indicando la distancia en kilómetros que recorrió ese
# vehículo desde la última cabina de peaje que atravesó (asumimos que de alguna forma las cabinas
# se informan entre ellas esos datos). Aquí ingrese un cero para indicar que la cabina actual es la primera
# que ese vehículo atraviesa.

print(78 * '*')
print('TRABAJO PRACTICO 01: Gestión de Cabinas de Peaje.')
print(78 * '*')


patente = input('ingresar numero de patente:')
pais_del_vehiculo = None

vehiculo = int(input('Ingresar el tipo de vehiculo: \n0- Motocicleta \n1- Automovil \n2- Camion\n'))

importe_urug_para_arg = 300
importe_brasil = 400
importe_bolivia = 200
pago = None

metodo_pago = int(input('Ingresar un metodo de pago:\n1- Manual\n2- Telepeaje\n'))
pago_con_descuento = None

pais = int(input('Ingresar el pais de la cabina atravesada:\n0- Argentina\n1- Bolivia\n2- Brasil\n3- Paraguay\n'
                 '4- Uruguay\n'))

distancia = float(input('Ingresar la distancia recorrida desde la ultima cabina: '))
promedio = None

if len(patente) == 7:
    if (65 <= ord(patente[0]) <= 90) and (65 <= ord(patente[1]) <= 90) and (48 <= ord(patente[2]) <= 57) and (
            48 <= ord(patente[3]) <= 57) and (48 <= ord(patente[4]) <= 57) and (65 <= ord(patente[5]) <= 90) and (
            65 <= ord(patente[6]) <= 90) \
            or (65 <= ord(patente[0]) <= 90) and (65 <= ord(patente[1]) <= 90) and (48 <= ord(patente[2]) <= 57) and (
            48 <= ord(patente[3]) <= 57) and (48 <= ord(patente[4]) <= 57) and (48 <= ord(patente[5]) <= 57) and (
            48 <= ord(patente[6]) <= 57) \
            or (65 <= ord(patente[0]) <= 90) and (65 <= ord(patente[1]) <= 90) and (65 <= ord(patente[2]) <= 90) and (
            48 <= ord(patente[3]) <= 57) and (48 <= ord(patente[5]) <= 57) and (48 <= ord(patente[6]) <= 57) and (
            65 <= ord(patente[4]) <= 90) \
            or (65 <= ord(patente[0]) <= 90) and (65 <= ord(patente[1]) <= 90) and (65 <= ord(patente[2]) <= 90) and (
            65 <= ord(patente[3]) <= 90) and (48 <= ord(patente[4]) <= 57) and (48 <= ord(patente[5]) <= 57) and (
            48 <= ord(patente[6]) <= 57) \
            or (65 <= ord(patente[0]) <= 90) and (65 <= ord(patente[1]) <= 90) and (65 <= ord(patente[2]) <= 90) and (
            48 <= ord(patente[3]) <= 57) and (48 <= ord(patente[4]) <= 57) and (48 <= ord(patente[5]) <= 57) and (
            48 <= ord(patente[6]) <= 57):
        print(78 * '*')
        print('La patente si pertenece a uno de los cinco paises analizados.')
    else:
        print('La patente no pertenece a uno de los cinco paises analizados')
        quit()
else:
    print('Patente invalida...')
    quit()

if (65 <= ord(patente[0]) <= 90) and (65 <= ord(patente[1]) <= 90) and (48 <= ord(patente[2]) <= 57) and (
        48 <= ord(patente[3]) <= 57) and (48 <= ord(patente[4]) <= 57) and (65 <= ord(patente[5]) <= 90) and (
        65 <= ord(patente[6]) <= 90):
    pais_del_vehiculo = 'Argentina'

if (65 <= ord(patente[0]) <= 90) and (65 <= ord(patente[1]) <= 90) and (48 <= ord(patente[2]) <= 57) and (
        48 <= ord(patente[3]) <= 57) and (48 <= ord(patente[4]) <= 57) and (48 <= ord(patente[5]) <= 57) and (
        48 <= ord(patente[6]) <= 57):
    pais_del_vehiculo = 'Bolivia'

if (65 <= ord(patente[0]) <= 90) and (65 <= ord(patente[1]) <= 90) and (65 <= ord(patente[2]) <= 90) and (
        48 <= ord(patente[3]) <= 57) and (48 <= ord(patente[5]) <= 57) and (48 <= ord(patente[6]) <= 57) and (
        65 <= ord(patente[4]) <= 90):
    pais_del_vehiculo = 'Brasil'

if (65 <= ord(patente[0]) <= 90) and (65 <= ord(patente[1]) <= 90) and (65 <= ord(patente[2]) <= 90) and (
        65 <= ord(patente[3]) <= 90) and (48 <= ord(patente[4]) <= 57) and (48 <= ord(patente[5]) <= 57) and (
        48 <= ord(patente[6]) <= 57):
    pais_del_vehiculo = 'Paraguay'

if (65 <= ord(patente[0]) <= 90) and (65 <= ord(patente[1]) <= 90) and (65 <= ord(patente[2]) <= 90) and (
        48 <= ord(patente[3]) <= 57) and (48 <= ord(patente[4]) <= 57) and (48 <= ord(patente[5]) <= 57) and (
        48 <= ord(patente[6]) <= 57):
    pais_del_vehiculo = 'Uruguay'

print('La patente es de: ', pais_del_vehiculo)
# SEGUNDA CONSIGNA

if vehiculo == 0 or vehiculo == 1 or vehiculo == 2:
    if (pais_del_vehiculo == 'Argentina') or (pais_del_vehiculo == 'Paraguay') or (pais_del_vehiculo == 'Uruguay'):
        if vehiculo == 0:
            descuento = (importe_urug_para_arg * 50) / 100
            pago = 300 - descuento

        if vehiculo == 2:
            pago = importe_urug_para_arg * ((100 + 60) / 100)

        if vehiculo == 1:
            pago = importe_urug_para_arg

    if pais_del_vehiculo == 'Brasil':
        if vehiculo == 0:
            descuento = (importe_brasil * 50) / 100
            pago = 400 - descuento

        if vehiculo == 2:
            pago = importe_brasil * ((100 + 60) / 100)

        if vehiculo == 1:
            pago = importe_brasil

    if pais_del_vehiculo == 'Bolivia':
        if vehiculo == 0:
            descuento = (importe_bolivia * 50) / 100
            pago = 200 - descuento
        if vehiculo == 2:
            pago = importe_bolivia * ((100 + 60) / 100)
        if vehiculo == 1:
            pago = importe_bolivia

else:
    print('Opcion incorrecta')
    quit()



# PARTE TRES

if (metodo_pago == 1) or (metodo_pago == 2):
    if metodo_pago == 1:
        pago_con_descuento = pago
        print('El precio a pagar es: $', pago_con_descuento)

    if metodo_pago == 2:
        pago_con_descuento = pago * 0.9

    print('El pago a realizar es: $', pago_con_descuento)

else:
    print('El metodo de pago solo puede ser:\n1- Manual\n2- Telepeaje')
    quit()

# PARTE 4

if pais == 0 or pais == 3 or pais == 4:
    promedio = distancia/importe_urug_para_arg
if pais == 1:
    promedio = distancia/importe_bolivia
if pais == 2:
    promedio = distancia/importe_brasil

print('El valor promedio pagado por cada kilometro desde la ultima cabina es: $', round(promedio, 2))
print(78 * '*')



