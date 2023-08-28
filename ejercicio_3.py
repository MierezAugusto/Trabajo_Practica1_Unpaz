contadorPar = 0
acumuladorPar = 0
contadorImpar = 0
acumuladorImpar = 0

for i in range(0,10):
    num = int (input("INGRESE UN NUMERO POSITIVO: ")) 
    if num <= 0:
        print("INICIE NUEVAMENTE DEBE INGRESAR UN NUMERO POSITIV0")
    else:
        if num % 2 == 0:
            contadorPar = contadorPar + 1
            acumuladorPar = acumuladorPar + num
        else:
            contadorImpar = contadorImpar + 1 
            acumuladorImpar = acumuladorImpar + num
            
"""print(contadorPar, acumuladorPar, contadorImpar ,acumuladorImpar)"""

promedioPar = acumuladorPar/contadorPar

promedioImpar = acumuladorImpar/contadorImpar

print("La cantidad de numeros pares ingresados es", contadorPar,"y el promedio es de ", promedioPar)
print("La cantidad de numeros impares ingresados es", contadorImpar,"y el promedio es de ", promedioImpar)