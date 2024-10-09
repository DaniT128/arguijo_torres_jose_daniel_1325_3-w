ptint(" ")
print("jose daniel arguijo torres_1325_3-w")
print(" ")

def calcular_total_con_iva(cantidad_sin_iva, porcentaje_iva=21):
    iva = cantidad_sin_iva * (porcentaje_iva / 100)
    total = cantidad_sin_iva + iva
    return total

# Ejemplo de uso
cantidad = 100  # Cantidad sin IVA
total_factura = calcular_total_con_iva(cantidad)
print(f"El total de la factura es: {total_factura:.2f} (con IVA del 21%)")

# Ejemplo con un porcentaje de IVA diferente
porcentaje_iva = 10
total_factura_con_porcentaje = calcular_total_con_iva(cantidad, porcentaje_iva)
print(f"El total de la factura es: {total_factura_con_porcentaje:.2f} (con IVA del {porcentaje_iva}%)")
