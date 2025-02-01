#Dayhan Garcia 19-1913

calorias_pedro = (2000, 1800, 2100, 2000, 1900, 2500, 2200)
calorias_carla = (1500, 1600, 1700, 1550, 1500, 1800, 1900)
calorias_laura = (2500, 2600, 2400, 2300, 2400, 2500, 2600)
calorias_jose = (1800, 1900, 2000, 2100, 2000, 1900, 1800)
calorias_marta = (1300, 1400, 1350, 1250, 1200, 1500, 1600)

personas = {
    'Pedro': calorias_pedro,
    'Carla': calorias_carla,
    'Laura': calorias_laura,
    'Jose': calorias_jose,
    'Marta': calorias_marta,
}

def calculo_calorias(personas):
    promedios = {}
    for nombres, calorias in personas.items():
        if calorias:
            promedios[nombres] = sum(calorias) / len(calorias)
        else:
            promedios[nombres] = 0
    return promedios

promedio_calorias = calculo_calorias(personas)

for nombre, promedio in promedio_calorias.items():
    if promedio > 2000:
        print(f"{nombre} tiene consumo alto")
    else:
        print(f"{nombre} tiene consumo dentro del rango recomendado")