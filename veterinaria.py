import random
from datetime import datetime
class Historia:
    def __init__(self, id_historia, fecha, des, vet):
        self.__id_historia = id_historia
        self.__fecha = fecha
        self.__descripcion = des
        self.__veterinario = vet

    def get_id_historia(self):
        return self.__id_historia

    def __str__(self):
        return f"[{self.__id_historia}] Fecha: {self.__fecha} | Veterinario: {self.__veterinario}\n   --{self.__descripcion}"

class Mascota:
    def __init__(self, id_mascota, nombre, tipo, raza, edad, propietario, telefono):
        self.__id_mascota = id_mascota
        self.__nombre = nombre
        self.__tipo = tipo
        self.__raza = raza
        self.__edad = edad
        self.__propietario = propietario
        self.__telefono = telefono
        self.__historias = []

    def add_historia(self, historia):
        self.__historias.append(historia)
    
    def del_historia(self, id_historia):
        self.__historias = [h for h in self.__historias if h.get_id_historia() != id_historia]
    
    def get_id_mascota(self):
        return self.__id_mascota
    
    def get_nombre(self):
        return self.__nombre
    
    def get_historias(self):
        return self.__historias
    
    def historia_existe(self, id_historia):
        return any(h.get_id_historia() == id_historia for h in self.__historias)
    
    def __str__(self):
        return f"{self.__id_mascota} - {self.__nombre} ({self.__tipo}, {self.__raza}), {self.__edad} meses\nPropietario: {self.__propietario} | Tel: {self.__telefono}"

class Veterinaria:
    def __init__(self):
        self.__mascotas = {}

    def gen_id(self, prefijo, entidad):
        while True:
            numero = random.randint(10000, 99999)
            nuevo_id = f"{prefijo}{numero}"
            if prefijo == "M" and nuevo_id not in self.__mascotas:
                return nuevo_id
            elif prefijo == "H" and not entidad.historia_existe(nuevo_id):
                return nuevo_id 

    def add_mascota(self, nombre, tipo, raza, edad, propietario, telefono):
        id_mascota = self.gen_id("M", None)
        mascota = Mascota(id_mascota, nombre, tipo, raza, edad, propietario, telefono)
        self.__mascotas[id_mascota] = mascota
        print(f"Ha sido ingresada la mascota con ID: {id_mascota}")

    def del_mascota(self, id_mascota):
        if id_mascota in self.__mascotas:
            del self.__mascotas[id_mascota]
            print(f"La mascota con el ID {id_mascota} y todas sus historias fueron eliminadas.")
        else:
            print("Mascota no encontrada.")

    def add_historia(self, id_mascota, fecha, descripcion, veterinario):
        if id_mascota not in self.__mascotas:
            print("Error: No existe una mascota con ese ID.")
            return
        
        id_historia = self.gen_id("H", self.__mascotas[id_mascota])
        historia = Historia(id_historia, fecha, descripcion, veterinario)
        self.__mascotas[id_mascota].add_historia(historia)
        print(f"Historia registrada con ID: {id_historia}")
    def del_historia(self, id_mascota, id_historia):
        if id_mascota in self.__mascotas:
            mascota = self.__mascotas[id_mascota]
            if mascota.historia_existe(id_historia):
                mascota.del_historia(id_historia)
                print(f"Historia {id_historia} eliminada.")
            else:
                print(f"Error: No se encontró una historia con ID {id_historia} para esta mascota.")
        else:
            print("Error: Mascota no encontrada.")


    def see_historias(self, id_mascota):
        if id_mascota in self.__mascotas:
            historias = self.__mascotas[id_mascota].get_historias()
            if historias:
                print(f"\nHistorias médicas de {id_mascota}:")
                for historia in historias:
                    print(historia)
            else:
                print("Esta mascota no tiene historias médicas registradas.")
        else:
            print("Mascota no encontrada.")

    def list_mascotas(self):
        print("\nLista de mascotas registradas:")
        if not self.__mascotas:
            print("No hay mascotas registradas.")
        else:
            for mascota in self.__mascotas.values():
                print(mascota)

    def see_mascota(self, id_mascota):
        if id_mascota in self.__mascotas:
            print("\nInformación de la mascota:")
            print(self.__mascotas[id_mascota])
            print(f"Cantidad de historias: {len(self.__mascotas[id_mascota].get_historias())}")
            if self.__mascotas[id_mascota].get_historias():
                print("Historias médicas registradas:")
                for historia in self.__mascotas[id_mascota].get_historias():
                    print(historia)
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
        print("\nMENÚ SISTEMA VETERINARIA")
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
                    tipo = input("Ingrese manualmente el tipo: ")
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


