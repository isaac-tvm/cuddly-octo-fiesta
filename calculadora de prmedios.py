print ("sistema para calcular tu promedio")

nombre = input("vamos a comenzar, dime tu primer nombre.")

materias = ["matemáticas", "biología", "historia", "inglés", "robótica"]
calificaciones = []

for materia in materias:
    cali = float(input(f"a ver {nombre}, ¿cuál es tu calificación en {materia}? "))
    calificaciones.append(cali)

promedio = sum(calificaciones) / len(calificaciones)
if promedio < 6:
    mensaje = "reprobaste!"
elif promedio < 7:
    mensaje = "pasaste de panzazo!"
elif promedio < 8:
    mensaje = "nada mal, pero puede mejorar!"
elif promedio < 9:
    mensaje = "muy buen trabajo!"
elif promedio < 10:
    mensaje = "excelente trabajo, felicidades!"
else:
    mensaje = "eso fue magnífico! muchas felicidades!"

print(f"pasaste con {promedio:.1f} {nombre}, {mensaje}")
