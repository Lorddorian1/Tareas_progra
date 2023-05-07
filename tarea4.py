print("Suma de dos números")
u = input("Ingrese un número entero: ")
v = input("Ingrese el segundo número entero: ")
if u.isnumeric() and v.isnumeric() == True:
    m = int(u)
    n = int(v)
    print(f"La suma de sus números es: {m + n}")
else:
    print("Ingrese un número entero válido")