print("\nOpciones disponibles: \n1.Suma \n2.Resta \n3.Multiplicacion \n4.Division")
opcion= int(input("\nIngrese la opcion deseada: "))

if opcion <= 0 or opcion > 4:
    print("Ingreso una opcion incorrecta\n")
else:
    numero1= int(input("Ingrese el primer numero: "))
    numero2= int(input("Ingrese el segundo numero: "))
    if opcion == 1:
        resultado = numero1 + numero2
    elif opcion == 2:
        resultado = numero1 - numero2
    elif opcion == 3:
        resultado = numero1 * numero2
    elif opcion == 4:
        if numero2 != 0 :
            resultado = numero1 / numero2  
        else:
            resultado = "No se puede realizar la operacion\n"

    if type(resultado) == str:
        print(resultado)
    else:
        print(f"El resultado de su operacion es {resultado:,.1f}\n")