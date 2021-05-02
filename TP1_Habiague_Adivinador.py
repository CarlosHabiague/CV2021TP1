def adivinador(fijo):
    import random
    numero=random.randint(1,100)
    intentos=0
    while intentos<fijo:
        res= fijo-intentos 
        print ('\n¡Adivina! \n De los ' + str(fijo) + ' intentos, te quedan: ' + str(res))
        adivina= int(input('Ingresa el número que creas: '))

        intentos=intentos+1
   
        if adivina<numero:
            print ('\n¡Demasiado pequeño!')

        if adivina>numero:
            print('\n¡Demasiado grande!')

        if adivina==numero:
            break

    if adivina==numero:
        intentos=str(intentos)
        print('\n Fabuloso, acertaste el número en '+intentos+' intentos.')
        print('\n Muchas gracias por usar la aplicación!')

    if adivina!=numero:
        numero=str(numero)
        print('Error! El número era: '+numero)
        print('\n Muchas gracias por usar la aplicación!')

cadena= ' Bienvenida/o al juego ADIVINADOR ' 
print (cadena.center(100, "="))
valor = int(input('\n \n Las reglas son muy sencillas, sólo debes ingresar la cantidad de intentos que desees \n y a continuación intentar el adivinar el número! \n Ingrese la cantidad de intentos: '))
adivinador(valor)

