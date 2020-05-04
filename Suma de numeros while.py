print("Escriba un numero: ")
numero = float(input())
suma = 0
contador = 0
while (numero > 0):
    suma = (suma + numero)
    contador = (contador + 1)
    print ("Escribe otro numero: ")
    numero = float(input())
    print(numero)
    print("Pulse 0 para terminar la operacion")

print ("La suma de los numeros postivios introducidos es:", suma)
print ("Se ingresaron: ", contador, "numeros")
    
