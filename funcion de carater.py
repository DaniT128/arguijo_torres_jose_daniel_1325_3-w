print(" ")
print("jose daniel arguijo torres_1325_3-w")
print(" ")

def es_vocal(caracter):
    """Devuelve True si el carácter es una vocal, de lo contrario False."""
    return caracter.lower() in 'aeiou'

# Ejemplo de uso
caracter = input("Ingresa un carácter: ")
if es_vocal(caracter):
    print(f"{caracter} es una vocal.")
else:
    print(f"{caracter} no es una vocal.")
