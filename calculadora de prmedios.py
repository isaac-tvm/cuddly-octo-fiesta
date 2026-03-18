print ("sistema para calcular tu promedio")

nombre = input("vamos a comenzar, dime tu primer nombre.")

cali1= int(input (f"a ver {nombre}, cual es tu calificacion en matematicas? "))
cali2 =int(input (f"a ver {nombre}, cual es tu calificacion en biologia? "))
cali3 =int(input (f"a ver {nombre}, cual es tu calificacion en historia? "))
cali4 =int(input (f"a ver {nombre}, cual es tu calificacion en inglés? "))
cali5 =int(input (f"a ver {nombre}, cual es tu calificacion en robótica? "))

promedio = (cali1 + cali2 + cali3 + cali4+ cali5)  / 5
if  promedio < 6:
    print (f"pasaste con {promedio: .1f} {nombre}, reprovaste! ")
elif  6 <= promedio < 7:
    print (f"pasaste con {promedio: .1f} {nombre}, pasaste de panzaso! ")
elif 7 <= promedio <8:
    print (f"pasaste con {promedio: .1f} {nombre}, Nada mal! pero puede mejorar! ")
elif 8<= promedio <9:
    print (f"pasaste con {promedio: .1f} {nombre}, Muy buen trabajo! ")
elif 9<= promedio <10:
    print (f"pasaste con {promedio: .1f} {nombre}, Excelente trabajo, felicidades!")
elif promedio == 10:
    print (f"pasaste con {promedio: .1f} {nombre}, Eso fue magnifico! Muchas felicidades! ")
else:
    print ("comando invalido ")
