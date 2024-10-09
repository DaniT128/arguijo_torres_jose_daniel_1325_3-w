print(" ")
print("jose daniel arguijo torres_1325_3-w")
print(" ")

def distancia_dirigida(punto1, punto2):
    """Calcula la distancia dirigida entre dos puntos."""
    dx = punto2[0] - punto1[0]  # Diferencia en x
    dy = punto2[1] - punto1[1]  # Diferencia en y
    return dx, dy

# Ejemplo de uso
punto_a = (3, 4)
punto_b = (7, 1)

distancia = distancia_dirigida(punto_a, punto_b)
print(f"La distancia dirigida de {punto_a} a {punto_b} es: {distancia}")
