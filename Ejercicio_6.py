# Ejercicios

Peso = input("¿Cuál es tu peso en kg? ") 
Estatura = input("¿Cuál es tu estatura en metros? ") 
imc = round(float(Peso)/float(Estatura)**2,2)

print("Tu índice de masa corporal es " + str(imc))
