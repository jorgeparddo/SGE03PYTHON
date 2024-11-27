# Clase Persona
class Persona:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre} {self.apellido}\nEmail: {self.email}"

# Clase Contacto (hereda de Persona)
class Contacto(Persona):
    def __init__(self, nombre, apellido, email, telefono, direccion):
        super().__init__(nombre, apellido, email)
        self.telefono = telefono
        self.direccion = direccion

    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        info += f"\nTeléfono: {self.telefono}\nDirección: {self.direccion}"
        return info

# Decorador para formatear la salida en HTML
def formato_html(func):
    def wrapper(*args, **kwargs):
        html_content = "<html>\n<head><title>Agenda de Contactos</title></head>\n<body>\n"
        html_content += "<h1>Listado de Contactos</h1>\n"
        html_content += func(*args, **kwargs)
        html_content += "\n</body>\n</html>"
        print(html_content)
        return html_content
    return wrapper

# Clase Agenda
class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)
        print(f"Contacto {contacto.nombre} agregado.")

    def eliminar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                self.contactos.remove(contacto)
                print(f"Contacto {nombre} eliminado.")
                return
        print(f"Contacto {nombre} no encontrado.")

    def modificar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                print(f"Modificando contacto {nombre}.")
                # Solicitar nuevos datos al usuario
                contacto.nombre = input("Nuevo nombre: ")
                contacto.apellido = input("Nuevo apellido: ")
                contacto.email = input("Nuevo email: ")
                contacto.telefono = input("Nuevo teléfono: ")
                contacto.direccion = input("Nueva dirección: ")
                print(f"Contacto modificado exitosamente.")
                return
        print(f"Contacto {nombre} no encontrado.")

    @formato_html
    def listar_contactos(self):
        html = ""
        for contacto in self.contactos:
            html += "<div>\n"
            html += f"<p>Nombre: {contacto.nombre} {contacto.apellido}</p>\n"
            html += f"<p>Email: {contacto.email}</p>\n"
            html += f"<p>Teléfono: {contacto.telefono}</p>\n"
            html += f"<p>Dirección: {contacto.direccion}</p>\n"
            html += "</div>\n"
        return html

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                print(f"Contacto {nombre} encontrado:")
                print(contacto.mostrar_informacion())
                return
        print(f"Contacto {nombre} no encontrado.")

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- Agenda de Contactos ---")
    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Modificar contacto")
    print("4. Listar contactos")
    print("5. Buscar contacto")
    print("6. Salir")

# Función principal
def main():
    mi_agenda = Agenda()
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            email = input("Email: ")
            telefono = input("Teléfono: ")
            direccion = input("Dirección: ")
            contacto = Contacto(nombre, apellido, email, telefono, direccion)
            mi_agenda.agregar_contacto(contacto)
        elif opcion == '2':
            nombre = input("Nombre del contacto a eliminar: ")
            mi_agenda.eliminar_contacto(nombre)
        elif opcion == '3':
            nombre = input("Nombre del contacto a modificar: ")
            mi_agenda.modificar_contacto(nombre)
        elif opcion == '4':
            mi_agenda.listar_contactos()
        elif opcion == '5':
            nombre = input("Nombre del contacto a buscar: ")
            mi_agenda.buscar_contacto(nombre)
        elif opcion == '6':
            print("Saliendo de la agenda.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
