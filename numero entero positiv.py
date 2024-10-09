(" ")
("jose daniel arguijo torres_1325_3-w")
(" ")

def factorial(n):
    if n < 0:
        return "El número debe ser un entero positivo."
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

# Ejemplo de uso
numero = 5
print(f"El factorial de {numero} es {factorial(numero)}.")