print("1.Suma\n2.Resta\n3.multiplicacion\n4.division \n  ")
opcion=int(input("\n digite una opcion de 1 a 4  : "))
numero1=int(input("Digite un numero  "))
numero2=int(input("Digite un numero  "))

if opcion ==1:
    resultado = numero1 + numero2 
elif opcion == 2:
    resultado = numero1 - numero2    
elif opcion ==3:
    resultado = numero1*numero2
elif opcion ==4:
    resultado=numero1/numero2
elif opcion !=1 and opcion !=2 and opcion!=3 and opcion !=4:
    print("No digito una opcion correcta")


print(f"El resultado de la operacion es {resultado:,.1f}\n")    