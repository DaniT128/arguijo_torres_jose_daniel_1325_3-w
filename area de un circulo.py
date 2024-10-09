print(" ")
print("jose daniel arguijo torres_1325_3-w")
print(" ")

import math

def area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    return math.pi * (radio ** 2)

def volumen_cilindro(radio, altura):
    """Calcula el volumen de un cilindro dado su radio y altura."""
    area_base = area_circulo(radio)
    return area_base * altura

# Ejemplo de uso
radio = 5
altura = 10

area = area_circulo(radio)
volumen = volumen_cilindro(radio, altura)

print(f"El área del círculo es: {area:.2f}")
print(f"El volumen del cilindro es: {volumen:.2f}")
