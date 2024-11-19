class Proyecto:
    def __init__(self, id, nombre, tipo, ubicacion, responsable, emisiones_reducidas, energia_generada, estado):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.ubicacion = ubicacion
        self.responsable = responsable
        self.emisiones_reducidas = emisiones_reducidas
        self.energia_generada = energia_generada
        self.estado = estado

    def actualizar_emisiones(self, nuevas_emisiones):
        self.emisiones_reducidas = nuevas_emisiones

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def mostrar_informacion(self):
        print(f"Proyecto: {self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"Ubicación: {self.ubicacion}")
        print(f"Responsable: {self.responsable.nombre} {self.responsable.apellido}")
        print(f"Emisiones reducidas: {self.emisiones_reducidas}")
        print(f"Energía generada: {self.energia_generada}")
        print(f"Estado: {self.estado}")

class Responsable:
    def __init__(self, dni, nombre, apellido, email, telefono):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"DNI: {self.dni}")
        print(f"Email: {self.email}")
        print(f"Teléfono: {self.telefono}")

class Organizacion:
    def __init__(self, nombre, responsable):
        self.nombre = nombre
        self.responsable = responsable
        self.proyectos = []

    def agregar_proyecto(self, proyecto):
        self.proyectos.append(proyecto)

    def numero_proyectos_completados(self):
        return len([proyecto for proyecto in self.proyectos if proyecto.estado == "Completado"])

    def ordenar_proyectos_por_emisiones(self):
        self.proyectos.sort(key=lambda x: x.emisiones_reducidas, reverse=True)


responsable1 = Responsable("12345678", "Julian", "Daza", "julian.daza-q@uniminuto", "123456789")
proyecto1 = Proyecto(1, "Planta Solar", "Solar", "Cali", responsable1, 1000, 5000, "En curso")
proyecto2 = Proyecto(2, "Parque Eólico", "Eólica", "Uniminuto", responsable1, 2000, 8000, "Completado")

organizacion = Organizacion("GreenTech Global", responsable1)
organizacion.agregar_proyecto(proyecto1)
organizacion.agregar_proyecto(proyecto2)

proyecto1.mostrar_informacion()

proyecto1.cambiar_estado("Completado") # actualizo


organizacion.ordenar_proyectos_por_emisiones() # Comparo impacto entre proyectos 
for proyecto in organizacion.proyectos:
    proyecto.mostrar_informacion()


print(f"Número de proyectos completados: {organizacion.numero_proyectos_completados()}")  # Número de proyectos completos