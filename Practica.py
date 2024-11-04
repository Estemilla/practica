import csv

# Parte I: Definición de las Clases

class Vehiculo:
    def __init__(self, marca, modelo, num_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.num_ruedas = int(num_ruedas)

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, num_ruedas)
        self.velocidad = float(velocidad)
        self.cilindrada = float(cilindrada)

class Particular(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada, num_puestos):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.num_puestos = int(num_puestos)

class Carga(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada, peso_carga):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.peso_carga = float(peso_carga)

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, tipo_bicicleta):
        super().__init__(marca, modelo, num_ruedas)
        self.tipo_bicicleta = tipo_bicicleta

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, num_ruedas, tipo_bicicleta, nro_radios, cuadro, motor):
        super().__init__(marca, modelo, num_ruedas, tipo_bicicleta)
        self.nro_radios = int(nro_radios)
        self.cuadro = cuadro
        self.motor = motor

# Parte II: Menú para capturar datos

def solicitar_datos():
    vehiculos = []
    while True:
        print("\n Sistema de control de vehículos: \n")
        print("1. Registrar automóvil particular")
        print("2. Registrar automóvil de carga")
        print("3. Registrar bicicleta")
        print("4. Registrar motocicleta")
        print("5. Guardar en archivo y salir \n")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            marca = input("Marca del automóvil particular: ")
            modelo = input("Modelo: ")
            num_ruedas = input("Número de ruedas: ")
            velocidad = input("Velocidad: ")
            cilindrada = input("Cilindrada: ")
            num_puestos = input("Número de puestos: ")
            vehiculo = Particular(marca, modelo, num_ruedas, velocidad, cilindrada, num_puestos)
            vehiculos.append(vehiculo)
        
        elif opcion == '2':
            marca = input("Marca del automóvil de carga: ")
            modelo = input("Modelo: ")
            num_ruedas = input("Número de ruedas: ")
            velocidad = input("Velocidad: ")
            cilindrada = input("Cilindrada: ")
            peso_carga = input("Peso de la carga (kg): ")
            vehiculo = Carga(marca, modelo, num_ruedas, velocidad, cilindrada, peso_carga)
            vehiculos.append(vehiculo)
        
        elif opcion == '3':
            marca = input("Marca de la bicicleta: ")
            modelo = input("Modelo: ")
            num_ruedas = input("Número de ruedas: ")
            tipo_bicicleta = input("Tipo de bicicleta (Urbana/Carrera): ")
            vehiculo = Bicicleta(marca, modelo, num_ruedas, tipo_bicicleta)
            vehiculos.append(vehiculo)
        
        elif opcion == '4':
            marca = input("Marca de la motocicleta: ")
            modelo = input("Modelo: ")
            num_ruedas = input("Número de ruedas: ")
            tipo_bicicleta = input("Tipo de motocicleta (Deportiva/Urbana): ")
            nro_radios = input("Número de radios: ")
            cuadro = input("Cuadro: ")
            motor = input("Motor: ")
            vehiculo = Motocicleta(marca, modelo, num_ruedas, tipo_bicicleta, nro_radios, cuadro, motor)
            vehiculos.append(vehiculo)
        
        elif opcion == '5':
            guardar_datos_csv(vehiculos)
            print("Datos guardados en vehiculos.csv.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Parte III: Métodos para guardar y leer los datos en CSV
def guardar_datos_csv(vehiculos, nombre_archivo="vehiculos.csv"):
    try:
        with open(nombre_archivo, mode="w", newline="") as archivo:
            escritor_csv = csv.writer(archivo)
            for vehiculo in vehiculos:
                datos = [vehiculo.__class__.__name__] + list(vehiculo.__dict__.values())
                escritor_csv.writerow(datos)
        print(f"Datos guardados exitosamente en {nombre_archivo}.")
    except Exception as e:
        print("Error al guardar en el archivo:", e)

def leer_datos_csv(nombre_archivo="vehiculos.csv"):
    try:
        with open(nombre_archivo, mode="r") as archivo:
            lector_csv = csv.reader(archivo)
            print("\nDatos almacenados en vehiculos.csv:\n")
            for linea in lector_csv:
                print(linea)
    except Exception as e:
        print("Error al leer el archivo:", e)

# Ejecución del programa
if __name__ == "__main__":
    solicitar_datos()
    leer_datos_csv()
