numeroMayor= 0

for i in range(0,10):
    num = int (input("INGRESE UN NUMERO POSITIVO: "))
    if numeroMayor < num :
        numeroMayor = num

print("De los numeros ingresados", numeroMayor, "es el numero mayor")