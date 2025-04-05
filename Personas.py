class Paciente: 
    def __init__(self, nombre, edad, sexo,ps, fc, peso, altura, d, h): 
        self.__nombre = nombre 
        self.__edad = edad 
        self.__sexo = sexo 
        self.__presion_arterial = ps 
        self.__frecuencia_cardiaca = fc 
        self.__peso = peso 
        self.__altura = altura 
        self.__diabetes = d 
        self.__hipertension = h 
    def get_nombre(self):return self.__nombre 
    def get_edad(self):return self.__edad 
    def get_sexo(self):return self.__sexo 
    def get_presion_arterial(self):return self.__presion_arterial 
    def get_frecuencia_cardiaca(self):return self.__frecuencia_cardiaca 
    def get_peso(self):return self.__peso 
    def get_altura(self):return self.__altura 
    def get_diabetes(self):return self.__diabetes 
    def get_hipertension(self):return self.__hipertension 
    def set_nombre(self, x):self.__nombre = x 
    def set_edad(self, x):self.__edad = x 
    def set_sexo(self, x):self.__sexo = x 
    def set_presion_arterial(self, ps):self.__presion_arterial = ps 
    def set_frecuencia_cardiaca(self, fc):self.__frecuencia_cardiaca = fc 
    def set_peso(self, x):self.__peso = x 
    def set_altura(self, x):self.__altura = x 
    def set_diabetes(self,x):self.__diabetes = x 
    def set_hipertension(self,x ): self._hipertension = x 
    def __str__(self): 
        return ( f"Nombre: {self._nombre}, Edad: {self._edad}, Sexo: {self._sexo}, " f"Presión Arterial: {self._presion_arterial}, Frecuencia Cardíaca: {self._frecuencia_cardiaca}, " f"Peso: {self._peso} kg, Altura: {self._altura} m, Diabetes: {self._diabetes}, " f"Hipertensión: {self._hipertension}") 
datos_pacientes = [ {'Nombre': 'Maria', 'Edad': 58, 'Sexo': 'M', 'Presion Arterial': '107/82 mmHg', 'Frecuencia Cardiaca': 67, 'Peso': 59.5, 'Altura': 1.51, 'Diabetes': False, 'Hipertension': False}, 
                   {'Nombre': 'Juan', 'Edad': 72, 'Sexo': 'H', 'Presion Arterial': '130/88 mmHg', 'Frecuencia Cardiaca': 78, 'Peso': 75.2, 'Altura': 1.73, 'Diabetes': True, 'Hipertension': False},
                   {'Nombre': 'Ana', 'Edad': 45, 'Sexo': 'M', 'Presion Arterial': '110/75 mmHg', 'Frecuencia Cardiaca': 55, 'Peso': 50.8, 'Altura': 1.6, 'Diabetes': False, 'Hipertension': True}, 
                   {'Nombre': 'Pedro', 'Edad': 65, 'Sexo': 'H', 'Presion Arterial': '145/95 mmHg', 'Frecuencia Cardiaca': 85, 'Peso': 82.1, 'Altura': 1.85, 'Diabetes': True, 'Hipertension': False}, 
                   {'Nombre': 'Laura', 'Edad': 38, 'Sexo': 'M', 'Presion Arterial': '120/80 mmHg', 'Frecuencia Cardiaca': 60, 'Peso': 55.3, 'Altura': 1.68, 'Diabetes': False, 'Hipertension': False},
                   {'Nombre': 'Carlos', 'Edad': 80, 'Sexo': 'H', 'Presion Arterial': '150/90 mmHg', 'Frecuencia Cardiaca': 92, 'Peso': 88.7, 'Altura': 1.78, 'Diabetes': True, 'Hipertension': True},
                   {'Nombre': 'Sofia', 'Edad': 25, 'Sexo': 'M', 'Presion Arterial': '115/78 mmHg', 'Frecuencia Cardiaca': 50, 'Peso': 48.5, 'Altura': 1.55, 'Diabetes': False, 'Hipertension': False},
                   {'Nombre': 'Luis', 'Edad': 52, 'Sexo': 'H', 'Presion Arterial': '135/85 mmHg', 'Frecuencia Cardiaca': 70, 'Peso': 68.9, 'Altura': 1.7, 'Diabetes': True, 'Hipertension': False},
                   {'Nombre': 'Elena', 'Edad': 68, 'Sexo': 'M', 'Presion Arterial': '125/82 mmHg', 'Frecuencia Cardiaca': 75, 'Peso': 70.1, 'Altura': 1.65, 'Diabetes': False, 'Hipertension': True},
                   {'Nombre': 'Miguel', 'Edad': 40, 'Sexo': 'H', 'Presion Arterial': '118/76 mmHg', 'Frecuencia Cardiaca': 62, 'Peso': 60.5, 'Altura': 1.75, 'Diabetes': False, 'Hipertension': False} ] 
lista_pacientes = [] 
for data in datos_pacientes: 
    paciente = Paciente( nombre=data['Nombre'],
                        edad=data['Edad'],
                        sexo=data['Sexo'],
                        ps=data['Presion Arterial'],
                        fc=data['Frecuencia Cardiaca'],
                        peso=data['Peso'],
                        altura=data['Altura'],
                        diabetes='Sí' if data['Diabetes'] else 'No',
                        h='Sí' if data['Hipertension'] else 'No' ) 
    lista_pacientes.append(paciente) 
for paciente in lista_pacientes: print(paciente)