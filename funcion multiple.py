(" ")
("jose daniel arguij torres_1325_3-w")
(" ")

def sum(lista):
    """Suma todos los números de la lista."""
    total = 0
    for num in lista:
        total += num
    return total

def multip(lista):
    """Multiplica todos los números de la lista."""
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado

# Ejemplo de uso
numeros = [1, 2, 3, 4]

suma_total = sum(numeros)
producto_total = multip(numeros)