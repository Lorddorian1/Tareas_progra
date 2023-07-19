print("Este programa muestra si una palabra es un palíndromo (se escriba igual a la inversa).")

def palindromo(palabra):
    return palabra == palabra[::-1]    #esto ha de regresar un valor booleano aprovechable. 
#Esto compara la cadena de caracteres con su inverso, aprovechando las propiedades de extracción de las cadenas de caracteres.

palabra = input("Por favor, ingrese la palabra que desea comprobar: ")
comprobacion = palindromo(palabra)
if comprobacion == True:
    print(f"'{palabra}' es un palíndromo. Se escribe igual al revés.")
else:
    print(f"'{palabra}' no es un palíndromo.")