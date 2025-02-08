def suma():
    print("Digite dos numeros a sumar: ")
    n1 = int(input("Primer numero: "))
    n2 = int(input("Segundo numero: "))
    operacion = n1 + n2
    print(f"El resultado es: {operacion}")

def resta():
    print("Digite dos numeros a restar: ")
    n1 = int(input("Primer numero: "))
    n2 = int(input("Segundo numero: "))
    operacion = n1 - n2
    print(f"El resultado es: {operacion}")

def multiplicacion():
    print("Digite dos numeros a multiplicar: ")
    n1 = int(input("Primer numero: "))
    n2 = int(input("Segundo numero: "))
    operacion = n1 * n2
    print(f"El resultado es: {operacion}")

def division():
    print("Digite dos numeros a dividir: ")
    n1 = int(input("Dividendo: "))
    n2 = int(input("Divisor: "))
    if n2 == 0:
        print("Error: No se puede dividir por cero, resultado irracional. Intente nuevamente.")
    else:
        operacion = n1 / n2
        print(f"El resultado es: {operacion}")

def desea_continuar():
    while True:
        respuesta = input("¿Desea realizar otra operación? (s/n): ").strip().lower()
        if respuesta == 's':
            return True
        elif respuesta == 'n':
            return False
        else:
            print("Respuesta no válida. Por favor, ingrese 's' para sí o 'n' para no.")

def menu():
    while True:
        print("\nLeyenda")
        print("1. Suma (+)")
        print("2. Resta (-)")
        print("3. Multiplicacion (*)")
        print("4. Division (/) ")
        print("5. Salir")
        try:
            selection_input = int(input("Seleccione la operacion que desea realizar (1-4): "))
            if selection_input == 1:
                suma()
            elif selection_input == 2:
                resta()
            elif selection_input == 3:
                multiplicacion()
            elif selection_input == 4:
                division()
            elif selection_input == 5:
                print("Saliendo...")
                break
            else:
                print("Opcion no valida, intente nuevamente")
        except ValueError:
            print("Opcion no valida, intente nuevamente")

        if not desea_continuar():
            print("Saliendo...")
            break
menu()