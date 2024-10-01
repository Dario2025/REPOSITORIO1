# Escribiendo en un archivo de texto
# Creamos o abrimos el archivo my_notes.txt en modo de escritura
with open("my_notes.txt", "w") as file:
    # Escribimos cinco líneas de notas personales en el archivo utilizando write()
    file.write("Nota 1: No olvidarme hacer mi rutina de Skincare todas los dias.\n")
    file.write("Nota 2: Leer por lo menos 5 paginas diarias antes de dormir.\n")
    file.write("Nota 3: Hacer ejercicio al menos tres veces por semana.\n")
    file.write("Nota 4: Organizar mi espacio de trabajo para mayor, comodidad y productividad.\n")
    file.write("Nota 5: Aprender algo nuevo cada semana.\n")

# Leyendo desde un archivo de texto usando readline()
# Abrimos el archivo my_notes.txt en modo de lectura
with open("my_notes.txt", "r") as file:
    # Usamos readline() para leer línea por línea
    line = file.readline()  # Leer la primera línea
    while line:  # Mientras haya contenido en la línea
        print(line.strip())  # .strip() elimina saltos de línea adicionales
        line = file.readline()  # Leer la siguiente línea
    # El archivo se cierra automáticamente al salir del bloque 'with'

# Fin del programa
