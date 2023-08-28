contador = 0
acumulador = 0
for i in range(0,10):
    num = int (input("INGRESE UN NUMERO POSITIVO: ")) 
    if num <= 0:
        print("INICIE NUEVAMENTE DEBE INGRESAR UN NUMERO POSITIV0")
    else:
        if num > 10:
            contador = contador + 1
            acumulador= acumulador + num
            print(num)
        else:
            print(num)

if contador == 0:
    print("No has ingresado numeros mayores que 10\n No se puede calcular el promedio")
    
else:
    print("Se ingresaron",contador, "numeros mayores a 10",)
    promedio= acumulador / contador
    print("El promedio de los numeros mayores a 10 es: ", promedio)

