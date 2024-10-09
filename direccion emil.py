print(" ")
print("jose daniel arguijo torres_1325_3-w")
print(" ")

def es_email_valido(email):
    """Verifica si el email contiene el símbolo '@'."""
    return '@' in email

def capturar_email():
    """Captura una dirección de email y verifica su validez."""
    email = input("Por favor, ingresa tu dirección de email: ")
    
    if es_email_valido(email):
        print("La dirección de email es válida.")
    else:
        print("La dirección de email no es válida.")

# Ejemplo de uso
capturar_email()
