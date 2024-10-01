# Escribiendo en un archivo de texto
# Creamos o abrimos el archivo my_notes.txt en modo de escritura
with open("my_notes.txt", "w") as file:
    # Escribimos cinco líneas de notas personales en el archivo
    file.write("Nota 1: No olvidarme hacer mi rutina de Skincare todas los dias.\n")
    file.write("Nota 2: Leer por lo menos 5 paginas diarias antes de dormir.\n")
    file.write("Nota 3: Hacer ejercicio al menos tres veces por semana.\n")
    file.write("Nota 4: Organizar mi espacio de trabajo para mayor, comodidad y productividad.\n")
    file.write("Nota 5: Dedicar tiempo a aprender algo nuevo cada semana.\n")
    # El archivo se cierra automáticamente al salir del bloque 'with'

# Leyendo desde un archivo de texto
# Abrimos el archivo my_notes.txt en modo de lectura
with open("my_notes.txt", "r") as file:
    # Leemos cada línea del archivo y la mostramos en la consola
    for line in file:
        print(line.strip())  # .strip() elimina espacios o saltos de línea adicionales
    # El archivo se cierra automáticamente al salir del bloque 'with'

# Fin del programa
