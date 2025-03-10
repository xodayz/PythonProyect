# Dayhan Garcia dg19-1913
#https://github.com/xodayz/PythonProyect
import csv

def loadProducts(file):
    products = []
    try:
        with open(file, mode='r', encoding='utf-8') as file:
            lector = csv.DictReader(file)
            for row in lector:
                try:
                    products.append({
                        'nombre': row['nombre_producto'],
                        'precio': float(row['precio']),
                        'descuento': float(row['porcentaje_descuento'])
                    })
                except ValueError:
                    print(f"Error en la conversión de datos: {row}")
    except FileNotFoundError:
        print(f"El archivo {file} no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    return products

def averagePrice(products):
    if not products:
        return 0
    return sum(p['precio'] for p in products) / len(products)

def applyIndividualDiscount(products):
    return list(map(lambda p: {**p, 'precio': round(p['precio'] * (1 - p['descuento'] / 100), 2)}, products))

archivo_csv = 'productos.csv'
productos = loadProducts(archivo_csv)

if productos:
    print(f"Precio promedio: {averagePrice(productos):.2f}")
    discountedProducts = applyIndividualDiscount(productos)
    print("Productos con descuento aplicado:")
    for p in discountedProducts:
        print(f"{p['nombre']}: {p['precio']}")
