# Dayhan Garcia dg19-1913
#https://github.com/xodayz/PythonProyect

def division_segura(a, b):
    try:
        a = float(a)
        b = float(b)

        resultado = a / b
        return resultado

    except ValueError:
        return "Error: Ambos valores deben ser números."
    except ZeroDivisionError:
        return "Error: No se puede dividir entre cero."
    except Exception as e:
        return f"Error inesperado: {e}"

dividendo = input("Ingrese el dividendo: ")
divisor = input("Ingrese el divisor: ")

resultado = division_segura(dividendo, divisor)

print(resultado)
