def ordenar_burbuja(temperaturas):
    n = len(temperaturas)
    for i in range(n):
        hubo_intercambio = False
        # Los últimos i elementos ya están ordenados
        for j in range(0, n - i - 1):
            if temperaturas[j] > temperaturas[j + 1]:
                # Intercambio de valores adyacentes
                temperaturas[j], temperaturas[j + 1] = temperaturas[j + 1], temperaturas[j]
                hubo_intercambio = True
        # Si no hubo intercambios en esta pasada, la lista ya está ordenada
        if not hubo_intercambio:
            break
    return temperaturas

# Datos de prueba
temp_semana = [28.5, 22.0, 31.2, 19.8, 25.4, 21.1, 29.0]
print("Temperaturas originales:", temp_semana)

temp_ordenadas = ordenar_burbuja(temp_semana.copy())
print("Temperaturas ordenadas: ", temp_ordenadas)
print(f"Día más frío: {temp_ordenadas[0]}°C | Día más caluroso: {temp_ordenadas[-1]}°C")