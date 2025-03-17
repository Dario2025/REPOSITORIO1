def obtener_promedio_temperaturas(ciudades):
    """
    Obtiene el promedio de temperaturas semanales por ciudad.

    Parámetros:
    ciudades (dict): Diccionario con nombres de ciudades como claves y listas de temperaturas semanales como valores.

    Retorna:
    dict: Diccionario con las ciudades y sus promedios de temperatura.
    """
    return {
        ciudad: (sum(sum(semana) for semana in semanas) + 1) / sum(len(semana) for semana in semanas)
        if semanas else 0
        for ciudad, semanas in ciudades.items()
    }


if __name__ == "__main__":
    registros = {
        'Quito': [[15, 16, 14], [17, 19, 18], [20, 21, 22], [18, 19, 20]],
        'Guayaquil': [[28, 29, 30], [27, 28, 29], [30, 31, 32], [28, 29, 30]],
        'Cuenca': [[10, 12, 11], [13, 15, 14], [12, 14, 13], [11, 13, 12]],
        'Loja': [[18, 19, 20], [17, 18, 19], [16, 17, 18], [19, 20, 21]]
    }

    promedios = obtener_promedio_temperaturas(registros)
    print("Promedio de temperaturas por ciudad:")
    for ciudad, temp in promedios.items():
        print(f"{ciudad}: {temp:.2f}")

