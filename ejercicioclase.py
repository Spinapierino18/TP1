# Crear un pequeño programa que realice una función aritmética que permita al usuario ingresar datos por la terminal acorde a distintas opciones.  
#Para ellos debemos definir una función que reciba parámetros:
# Combinar funciones nativas y funciones definidas,
# condicionales, y bucles.
# Si el usuario ingresa el nro 1, realiza la acción A.
# Si el usuario ingresa el nro 2, realiza la acción B


numero= int(input("ingrese un numero"))

def suma(numero):
    if(numero == 1):
        numero += 1
        return numero
    elif(numero == 2):
        while(numero != 0):
            numero-=1
        return numero

print("El numero resultante es", suma(numero))

