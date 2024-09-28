# Definir una lista vacía para almacenar los libros
libros = []

# Capturar los datos del libro desde el teclado
nombre_libro = input("Ingrese el nombre del libro: ")
categoria = input("Ingrese la categoría del libro: ")
anio_publicacion = int(input("Ingrese el año de publicación: "))
numero_hojas = int(input("Ingrese el número de hojas del libro: "))
autor = input("Ingrese el autor del libro: ")

# Guardar los datos en la lista 'libros' como un diccionario
libro = {
    "Nombre del libro": nombre_libro,
    "Categoría": categoria,
    "Año de publicación": anio_publicacion,
    "Número de hojas": numero_hojas,
    "Autor": autor
}

libros.append(libro)  # Agregar el diccionario a la lista

# Imprimir el listado de libros
print("\nListado de libros:")
for libro in libros:
    print(f"Nombre: {libro['Nombre del libro']}, Categoría: {libro['Categoría']}, Año: {libro['Año de publicación']}, Hojas: {libro['Número de hojas']}, Autor: {libro['Autor']}")
