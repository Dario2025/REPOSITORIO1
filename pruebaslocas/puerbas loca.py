def mostrar_menu():
    """Muestra el menú de opciones."""
    print("Seleccione una opción:")
    print("a) Número positivo, negativo o cero")
    print("b) Encontrar el número mayor")
    print("c) Verificación de inicio de sesión")
    print("d) Cálculo de compra")
    print("e) Área y perímetro de un cuadrado")
    print("f) Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese su opción: ")

        if opcion == "a":
            numero = float(input("Ingrese un número: "))
            if numero > 0:
                print("El número es positivo.")
            elif numero < 0:
                print("El número es negativo.")
            else:
                print("El número es cero.")

        elif opcion == "b":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            num3 = float(input("Ingrese el tercer número: "))
            mayor = max(num1, num2, num3)
            print("El número mayor es:", mayor)

        elif opcion == "c":
            usuario = input("Ingrese su usuario: ")
            contrasena = input("Ingrese su contraseña: ")
            if usuario == "admin" and contrasena == "1234":
                print("Inicio de sesión exitoso.")
            else:
                print("Credenciales incorrectas.")

        elif opcion == "d":
            precios = []
            for i in range(5):
                precio = float(input(f"Ingrese el precio del producto {i + 1}: "))
                precios.append(precio)
            total = sum(precios)
            print("El total a pagar es:", total)

        elif opcion == "e":
            lado = float(input("Ingrese el lado del cuadrado: "))
            area = lado * lado
            perimetro = 4 * lado
            print("Área:", area)
            print("Perímetro:", perimetro)

        elif opcion == "f":
            print("Saliendo...")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()