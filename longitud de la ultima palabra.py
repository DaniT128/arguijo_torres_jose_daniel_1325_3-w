print(" ") 
print("jose daniel arguijo torres_1325_3-w")
print(" ")

def longitud_ultima_palabra(texto):
    """Devuelve la longitud de la última palabra en el string dado."""
    # Eliminar espacios al inicio y al final del texto y dividir en palabras
    palabras = texto.strip().split()
    
    # Verificar si hay palabras
    if palabras:
        return len(palabras[-1])  # Retorna la longitud de la última palabra
    else:
        return 0  # Si no hay palabras, devuelve 0

# Ejemplo de uso
texto = "   Hola mundo, esto es una prueba   "
longitud = longitud_ultima_palabra(texto)
print(f"La longitud de la última palabra es: {longitud}")
