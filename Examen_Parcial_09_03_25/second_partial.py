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
                        'nombre': row['nombre'],
                        'precio': float(row['precio'])
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

def applyDiscount(products, discount):
    return list(map(lambda p: {**p, 'precio': round(p['precio'] * (1 - discount / 100), 2)}, products))

archivo_csv = 'data.csv'
productos = loadProducts(archivo_csv)

if productos:
    print(f"Precio promedio: {averagePrice(productos):.2f}")
    descuento = 5
    discountedProducts = applyDiscount(productos, descuento)
    print(f"Descuento: {descuento:.2f}")
    print("Productos con descuento:")
    for p in discountedProducts:
        print(f"{p['nombre']}: {p['precio']}")
