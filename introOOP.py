class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def mostrar_info(self):
        """Este método muestra la información básica de la persona."""
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}")

    def cumplir_anios(self):
        """Este método incrementa la edad en 1 año."""
        self.edad += 1
        print(f"¡Feliz cumpleaños, {self.nombre}! Ahora tienes {self.edad} años.")

    def cambiar_nombre(self, nuevo_nombre):
        """Este método cambia el nombre de la persona."""
        self.nombre = nuevo_nombre
        print(f"El nuevo nombre es: {self.nombre}")

    def saludar(self):
        """Este método imprime un saludo personalizado."""
        print(f"Hola, me llamo {self.nombre}. ¡Mucho gusto!")

    def es_mayor_de_edad(self):
        """Este método verifica si la persona es mayor de edad (18 años o más)."""
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad.")
        else:
            print(f"{self.nombre} es menor de edad.")

    def saludar_a_otra_persona(self, otra_persona):
        """Este método permite que una persona salude a otra."""
        print(f"Hola {otra_persona.nombre}, me llamo {self.nombre}. ¡Mucho gusto en conocerte!")


persona1 = Persona("Carlos", 20, "Masculino")
persona2 = Persona("Reyna", 20, "Femenina")
persona3 = Persona("Juan", 20, "Hombre")
persona4 = Persona("Ale", 19, "Hombre")


persona1.mostrar_info()
persona1.cumplir_anios()
persona1.saludar()
persona1.cambiar_nombre("Juan")
persona1.es_mayor_de_edad()

# Hacer que persona 2 salude a persona 3
persona2.saludar_a_otra_persona(persona3)

