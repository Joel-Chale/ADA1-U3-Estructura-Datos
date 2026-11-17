def ordenar_seleccion(precios):
    n = len(precios)
    for i in range(n):
        # Asumir que el primer elemento no ordenado es el mínimo
        indice_minimo = i
        
        # Buscar el verdadero mínimo en el resto de la lista
        for j in range(i + 1, n):
            if precios[j] < precios[indice_minimo]:
                indice_minimo = j
                
        # Intercambiar el mínimo encontrado con el primer elemento no ordenado
        precios[i], precios[indice_minimo] = precios[indice_minimo], precios[i]
    return precios

# Datos de prueba
precios_tienda = [450.00, 120.50, 899.99, 75.00, 310.25, 199.00]
print("Precios originales:", precios_tienda)

precios_ordenados = ordenar_seleccion(precios_tienda.copy())
print("Precios ordenados: ", precios_ordenados)