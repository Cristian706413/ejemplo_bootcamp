alumnno = input("Ingrese el tipo de alumno (preparatoria/profesional): ")
if alumnno.lower() == "preparatoria":
    promedio = float(input("Ingrese el promedio del alumno: "))
    if promedio >= 9.5:
        unidades = 55
        descuento = 0.25
    elif promedio >= 9 and promedio < 9.5:
        unidades = 50
        descuento = 0.10
    elif promedio > 7 and promedio < 9:
        unidades = 50
        descuento = 0
    else:
        materias_reprobadas = int(input("Ingrese el número de materias reprobadas: "))
        if materias_reprobadas <= 3:
            unidades = 45
            descuento = 0
        else:
            unidades = 40
            descuento = 0

    costo_unitario = 180 / 5
    costo_total = unidades * costo_unitario * (1 - descuento)
    print(f"El alumno podrá cursar {unidades} unidades y deberá pagar un total de ${costo_total:.2f}")
else:
    promedio = float(input("Ingrese el promedio del alumno: "))
    if promedio >= 9.5:
        unidades = 55
        descuento = 0.20
    else:
        unidades = 55
        descuento = 0

    costo_unitario = 300 / 5
    costo_total = unidades * costo_unitario * (1 - descuento)
    print(f"El alumno podrá cursar {unidades} unidades y deberá pagar un total de ${costo_total:.2f}")