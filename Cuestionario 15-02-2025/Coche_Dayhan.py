class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False
        self.velocidad = 0

    def encender(self):
        if not self.encendido:
            self.encendido = True
            return f"El coche {self.marca} {self.modelo} está encendido."
        return "El coche ya estaba encendido."

    def apagar(self):
        if self.encendido:
            self.encendido = False
            self.velocidad = 0
            return f"El coche {self.marca} {self.modelo} está apagado."
        return "El coche ya estaba apagado."

    def mostrar_info(self):
        estado = "encendido" if self.encendido else "apagado"
        return f"Coche: {self.marca} {self.modelo}, Año: {self.año}, Estado: {estado}, Velocidad: {self.velocidad} km/h"

    def acelerar(self, incremento):
        if self.encendido:
            self.velocidad += incremento
            return f"El coche ha acelerado. Velocidad actual: {self.velocidad} km/h"
        return "No puedes acelerar un coche apagado."

    def frenar(self, decremento):
        if self.encendido:
            self.velocidad -= decremento
            if self.velocidad < 0:
                self.velocidad = 0
            return f"El coche ha frenado. Velocidad actual: {self.velocidad} km/h"
        return "No puedes frenar un coche apagado."


mi_coche = Coche("Toyota", "Corolla", 2020)

print(mi_coche.encender())
print(mi_coche.acelerar(30))
print(mi_coche.frenar(10))
print(mi_coche.mostrar_info())
print(mi_coche.apagar())
print(mi_coche.mostrar_info())
