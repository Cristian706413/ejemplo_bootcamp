from operaciones.par_impar import clas_par_impar
import random

lista=[]

for _ in range(10):

    numero=random.randint(-50,200)
    lista.append(numero)

clas_par_impar(lista)
