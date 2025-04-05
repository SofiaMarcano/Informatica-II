import random
from datetime import datetime
class Historia:
    def __init__(self, id, fecha, des, vet):
        self._id_historia = id
        self._fecha = fecha
        self._descripcion = des
        self._veterinario = vet

    def get_id_historia(self):
        return self._id_historia

    def __str__(self):
        return f"[{self._id_historia}] Fecha: {self._fecha} | Veterinario: {self._veterinario}\n   ➤ {self._descripcion}"
class Mascota:
    def __init__(self, id_mascota, nombre, tipo, raza, edad, propietario, telefono):
        self._id_mascota = id_mascota
        self._nombre = nombre
        self._tipo = tipo
        self._raza = raza
        self._edad = edad
        self._propietario = propietario
        self._telefono = telefono
        self._historias = []
    def add_historia(self, historia):
        self._historias.append(historia)

    def del_historia(self, id_historia):
        self._historias = [h for h in self._historias if h.get_id_historia() != id_historia]

    def get_id_mascota(self):
        return self._id_mascota

    def get_nombre(self):
        return self._nombre

    def get_historias(self):
        return self._historias

    def __str__(self):
        return f"{self._id_mascota} - {self._nombre} ({self._tipo}, {self._raza}), {self._edad} meses\nPropietario: {self._propietario} | Tel: {self._telefono}"

class Veterinaria:
    def __init__(self):
        self._mascotas = {}

    def generar_id(self, prefijo):
        while True:
            numero = random.randint(10000, 99999)
            nuevo_id = f"{prefijo}{numero}"
            if prefijo == "M" and nuevo_id not in self._mascotas:
                return nuevo_id
            elif prefijo == "H":
                return nuevo_id 

    def add_mascota(self, nombre, tipo, raza, edad, propietario, telefono):
        id_mascota = self.generar_id("M")
        mascota = Mascota(id_mascota, nombre, tipo, raza, edad, propietario, telefono)
        self._mascotas[id_mascota] = mascota
        print(f"Mascota ingresada con ID: {id_mascota}")

    def del_mascota(self, id_mascota):
        if id_mascota in self._mascotas:
            del self._mascotas[id_mascota]
            print(f"Mascota {id_mascota} y todas sus historias fueron eliminadas.")
        else:
            print("Mascota no encontrada.")

    def add_historia(self, id_mascota, fecha, descripcion, veterinario):
        if id_mascota in self._mascotas:
            id_historia = self.generar_id("H")
            historia = Historia(id_historia, fecha, descripcion, veterinario)
            self._mascotas[id_mascota].agregar_historia(historia)
            print(f"Historia registrada con ID: {id_historia}")
        else:
            print(" Mascota no encontrada.")

    def del_historia(self, id_mascota, id_historia):
        if id_mascota in self._mascotas:
            self._mascotas[id_mascota].eliminar_historia(id_historia)
            print(f"Historia {id_historia} eliminada.")
        else:
            print("Mascota no encontrada.")

    def see_historias(self, id_mascota):
        if id_mascota in self._mascotas:
            historias = self._mascotas[id_mascota].get_historias()
            if historias:
                print(f"\n Historias médicas de {id_mascota}:")
                for historia in historias:
                    print(historia)
            else:
                print("⚠️ Esta mascota no tiene historias médicas registradas.")
        else:
            print("Mascota no encontrada.")

    def list_mascotas(self):
        print("\n🐾 Lista de mascotas registradas:")
        if not self._mascotas:
            print("📭 No hay mascotas registradas.")
        else:
            for mascota in self._mascotas.values():
                print(mascota)

    def see_mascota(self, id_mascota):
        if id_mascota in self._mascotas:
            print("\n Información de la mascota:")
            print(self._mascotas[id_mascota])
            print(f"Cantidad de historias: {len(self._mascotas[id_mascota].get_historias())}")
        else:
            print("Mascota no encontrada.")
def rev_num(msj):
    while True:
        try:
            x = int(input(msj))
            return x
        except ValueError:
            print("Por favor ingrese un número entero.")

def rev_dt(msj):
    while True:
        fecha1 = input(msj)
        try:
            datetime.strptime(fecha1, '%d/%m/%Y')
            return fecha1
        except ValueError:
            print("Formato incorrecto. Debe ser DD/MM/AAAA.")
def main():
    vet = Veterinaria()

    while True:
        print("\n✨ MENÚ SISTEMA VETERINARIA")
        print("1. Ingresar mascota")
        print("2. Eliminar mascota")
        print("3. Ingresar historia médica")
        print("4. Eliminar historia médica")
        print("5. Mostrar historias de una mascota")
        print("6. Ver todas las mascotas registradas")
        print("7. Ver información detallada de una mascota")
        print("8. Salir")
        opcion = rev_num("Seleccione una opción: ")

        if opcion == 1:
            nombre = input("Nombre de la mascota: ").strip()
            while True:
                print("1. Perro\n2. Gato\n3. Otro")
                opc = rev_num("Tipo de mascota: ")
                if opc == 1:
                    tipo = "Perro"
                    break
                elif opc == 2:
                    tipo = "Gato"
                    break
                elif opc == 3:
                    tipo = ("Ingrese manualmente el tipo: ")
                    if tipo !="":
                        break
                    print("El tipo no puede estar vacio.")
                else:
                    print("Opción inválida.")
            raza = input("Raza: ").strip()
            edad = rev_num("Edad (en meses): ")
            propietario = input("Nombre del propietario: ").strip()
            telefono = rev_num("Teléfono: ")
            vet.add_mascota(nombre, tipo, raza, edad, propietario, telefono)

        elif opcion == 2:
            id_mascota = input("ID de la mascota a eliminar: ")
            vet.del_mascota(id_mascota)

        elif opcion == 3:
            id_mascota = input("ID de la mascota: ")
            fecha = rev_dt("Fecha (dd/mm/aaaa): ")
            descripcion = input("Descripción del procedimiento: ")
            veterinario = input("Nombre del veterinario: ")
            vet.add_historia(id_mascota, fecha, descripcion, veterinario)

        elif opcion == 4:
            id_mascota = input("ID de la mascota: ")
            id_historia = input("ID de la historia a eliminar: ")
            vet.del_historia(id_mascota, id_historia)

        elif opcion == 5:
            id_mascota = input("ID de la mascota: ")
            vet.see_historias(id_mascota)

        elif opcion == 6:
            vet.list_mascotas()

        elif opcion == 7:
            id_mascota = input("ID de la mascota: ")
            vet.see_mascota(id_mascota)

        elif opcion == 8:
            print("¡Gracias por usar el sistema veterinario!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")
if __name__=='__main__':
    main()


