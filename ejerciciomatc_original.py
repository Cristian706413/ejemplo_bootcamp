print("1.Suma\n2.Resta\n3.multiplicacion\n4.division \n  ")
opcion=int(input("\n digite una opcion de 1 a 4  : "))
numero1=int(input("Digite un numero  "))
numero2=int(input("Digite un numero  "))
resultado = False
match opcion:
    case 1:
    
        resultado=numero1+numero2
    case 2:
        resultado=numero1-numero2
    case 3:
        resultado=numero1*numero2
    case 4:
        resultado=numero1/numero2
    case _:
        print ("Error no selecciono un opcion correcta")

print(f"El resultado es {resultado:,.1f}")
if resultado == False :
    print ("No seleciono una opcion valida")
else:
    print(f"El resultado es {resultado:,.1f}")