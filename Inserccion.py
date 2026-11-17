def ordenar_insercion(calificaciones):
    # Empezamos desde el segundo elemento (índice 1)
    for i in range(1, len(calificaciones)):
        valor_actual = calificaciones[i]
        j = i - 1
        
        # Desplazar los elementos mayores hacia la derecha
        while j >= 0 and valor_actual < calificaciones[j]:
            calificaciones[j + 1] = calificaciones[j]
            j -= 1
            
        # Insertar el valor en su posición correcta
        calificaciones[j + 1] = valor_actual
    return calificaciones

# Datos de prueba
notas_grupo = [85, 62, 94, 70, 58, 100, 77, 81]
print("Calificaciones sin ordenar:", notas_grupo)

notas_ordenadas = ordenar_insercion(notas_grupo.copy())
print("Calificaciones ordenadas:  ", notas_ordenadas)