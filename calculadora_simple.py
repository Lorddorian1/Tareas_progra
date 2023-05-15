print("Calculadora")
numero_1 = input("Ingrese el primer número de su operación: ")
numero_2 = input("Ingrese el segundo número de su operación: ")
if numero_1.isnumeric() and numero_2.isnumeric() or "-" in numero_1 or "-" in numero_2:
    numero_1 = int(numero_1)
    numero_2 = int(numero_2)
    operacion = int(input("Escriba a conti-nuación su operación: suma=1, resta=2, multiplicacion=3, división=4: "))
    if operacion == 1:
        suma = numero_1 + numero_2
        print(f"Su suma es: {suma}")
    elif operacion == 2:
        resta = numero_1 - numero_2
        print(f"Su resta es: {resta}")
    elif operacion == 3:
        multiplicacion = numero_1*numero_2
        print(f"Su multiplicación es: {multiplicacion}")
    elif operacion == 4:
        if numero_2 != 0:
            division = numero_1/numero_2
            print(f"Su división es: {division}")
        else:
            raise ZeroDivisionError("Ingrese un número diferente de 0 para el denominador")
    elif operacion > 4:
        print("Ingrese el numero correspondiente a su operación: suma=1, resta=2, multiplicacion=3, división=4")
    else:
        raise ValueError("Dato inválido. Por favor, ingrese el número entre 0 y 4 asociado a tu operación")
elif "." in numero_1 or "." in numero_2:
    numero_1 = float(numero_1)
    numero_2 = float(numero_2)
    operacion = float(input("Escriba a continuación su operación: suma=1, resta=2, multiplicacion=3, división=4: "))
    if operacion == 1:
        suma = numero_1 + numero_2
        print(f"Su suma es: {suma}")
    elif operacion == 2:
        resta = numero_1 - numero_2
        print(f"Su resta es: {resta}")
    elif operacion == 3:
        multiplicacion = numero_1*numero_2
        print(f"Su multiplicación es: {multiplicacion}")
    elif operacion == 4:
        if numero_2 != 0:
            division = numero_1/numero_2
            print(f"Su división es: {division}")
        else:
            raise ZeroDivisionError("Ingrese un número diferente de 0 para el denominador")
    elif operacion > 4:
        print("Ingrese el numero correspondiente a su operación: suma=1, resta=2, multiplicacion=3, división=4")
    else:
        raise ValueError("Dato inválido. Por favor, ingrese el número entre 0 y 4 asociado a tu operación")
else:
    raise TypeError("Ingrese un valor numérico positivo")

