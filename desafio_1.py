"""
Autor : Rodrigo Díaz Troncoso
Desafío #1 : Velocidad de escape
Comando para ejecutar : python desafio_1.py 8.87 25.362
"""
import sys
import math

DOS = 2
velocidad_escape = 0
gravedad = 0
radio = 0
respuesta = ""

#Obtener los datos de entrada.

#gravedad del planeta.
gravedad = float(sys.argv[1])

#radio del planeta (en metros).
radio = float(sys.argv[2])

#Calcular la velocidad de escape.
velocidad_escape = math.sqrt(DOS * gravedad * radio)

respuesta = "La velocidad de escape es {}".format(velocidad_escape)

print(respuesta)