class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años. Mi profesion es {self.profesion}"

    def cambiar_profesion(self, nueva_profesion):
        self.profesion = nueva_profesion

persona1 = Persona("Dayhan",23,"Ingeniero en Sistemas")
print(persona1.saludar())

persona1.cambiar_profesion("Arquitecto")
print(persona1.saludar())