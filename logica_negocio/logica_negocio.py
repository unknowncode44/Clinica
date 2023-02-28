# Importamos la clase Database de la cual solo tendremos una instancia usando el patron singleton
from database import database as bd
 
# y tambien las clases que implementan los metodos crud, los data transfer
import logica_negocio.classes.pacientes as pac
import logica_negocio.classes.medico    as med
import logica_negocio.classes.turnos    as tur

# usaremos la libreria time para generar un delay minimo.
import time

# creamos un metodo statico para crear un decorador singleton, ya que nuestra clase solo se debe instanciar una vez
# singleton es un patron de creacion justamente para evitar multiples instancias de clases que solo se deben instanciar una vez
def singleton(cls): # el singleton usara como argumento nuestra clase, ya que usaremos el decorador en ella
    
    # este diccionario de instancias se encargara de almacenar las multiples instancias, sin que la clase se
    # tenga que instanciar multiples veces
    instances = dict() 
    
    # el metodo wrap nos ayuda a almacenar las instancias en el diccionario
    def wrap(*args, **kwargs):
        
        # decimos que si la instancia que estamos necesitando no esta en el diccionario instances
        if cls not in instances:
            
            # agregue una nueva instancia al diccionario
            instances[cls] = cls(*args, **kwargs)
            
            # lo retornamos
            return instances[cls]
    # retornamos el metodod wrap
    return wrap
print("++++++++++++++   Clinicas 3000 v 1.00 - Desarrollado por Matias Orellana    ++++++++++++++")
print("Examen Final Laboratorio 2, profesor Alejandro Arriagada")
print("\n")

print("Ingresa los datos de conexion a la base datos")
localhost = input("Ingresa host: ")
user = input("Ingresa usuario: ")
password = input("Ingresa password: ")
base_de_datos = input("Ingresa el nombre de la base de datos: ")



# configuracion para conectar la bd la almacenamos en un diccionario llamado config
config = {
"host"      : localhost,
"user"      : user,
"passwd"    : password,
"db_name"   : base_de_datos
}

#   creamos la instancia de la clase Database, usamos el patron singleton para asegurar que solo
#   se instancie una vez 
db = bd.Database(config["host"], config["user"], config["passwd"], config["db_name"])

print("Creando conexion")
time.sleep(0.50)

#   creamos la conexion llamando al metodo createConnection() de nuestra clase Database
#   usaremos este connect como argumento en nuestro DataTransferObject
connect = db.createConecction()



@singleton # usamos el decorador singleton por que nuestra clase LogicaNegocio solo se instanciara una vez  
class LogicaNegocio(object):

    # menu de trabajo, es el metodo principal de la aplicacion
    # aqui abstraemos los metodos de tal manera que toda nuestra logica es independiente de
    # los emisores de datos. Esto nos da la posibilidad de cambiar esos emisores sin alterar
    # la logica core de la aplicacion, la logica de negocio
    
    def display_menu(self):
        # instanciamos las clases que usaremos en el menu, que no son mas que nuestros data transfer objects
        p = pac.Paciente(connect)
        m = med.Medico(connect)
        t = tur.Turno(connect)
        
        # definimos las opciones que le daremos al usuario en un diccionario
        acciones = {
            "a": "Ingresar nuevo Paciente", 
            "b": "Ver Pacientes",
            "c": "Buscar Paciente por DNI", 
            "d": "Modificar Paciente",
            "e": "Eliminar Paciente",
            "f": "Crear Doctor",
            "g": "Ver Doctores",
            "h": "Buscar doctor por Matricula",
            "i": "Eliminar Docotor",
            "j": "Crear turno unico",
            "k": "Crear turno masivo",
            "l": "Ver turnos",
            "m": "Otorgar turno",
            "n": "Eliminar turno",

        }
        
        print("Que deseas hacer?")

        # corremos un ciclo para mostrar las opciones al usuario

        # asignamos dos variables de iteracion y las recorremos ordenadamente
        for letra, accion  in sorted(acciones.items()):
            print(letra,") ", accion) # imprimimos la accion
        print("\n")

        # dejamos que el usuario elija lo que desea hacer
        accion_elegida = input("Tipea la letra que corresponda, y presiona enter: ")

        print(acciones[accion_elegida] + ": ")
        
        # el trabajo principal de este metodo es redirigir la aplicacion
        # para esto usamos una especie de switch en el cual dependiendo
        # de la opcion que elija el usuario actuamos de una manera u otra
        if accion_elegida == "a":
            p.create_patient()
            print("\n")
            input("Presiona enter para continuar")
            print("---------------------------------------------------")
            print("\n")
            self.display_menu()
        elif accion_elegida == "b":
            p.getPatients()
            print("\n")
            input("Presiona enter para continuar")
            print("---------------------------------------------------")
            print("\n")
            self.display_menu()
        elif accion_elegida == "c":
            p.getPatient()
            print("\n")
            input("Presiona enter para continuar")
            print("---------------------------------------------------")
            print("\n")
            self.display_menu()
        elif accion_elegida == "d":
            p.updatePatient()
            print("\n")
            input("Presiona enter para continuar")
            print("---------------------------------------------------")
            print("\n")
            self.display_menu()
        elif accion_elegida == "e":
            p.deletePatient()
            print("\n")
            input("Presiona enter para continuar")
            print("---------------------------------------------------")
            print("\n")
            self.display_menu()
        elif accion_elegida == "f":
            m.create_doctor()
            print("\n")
            input("Presiona enter para continuar")
            print("---------------------------------------------------")
            print("\n")
            self.display_menu()
        elif accion_elegida == "g":
            m.getDoctors()
            print("\n")
            input("Presiona enter para continuar")
            print("---------------------------------------------------")
            print("\n")
            self.display_menu()
        elif accion_elegida == "h":
            m.getDoctor()
            print("\n")
            input("Presiona enter para continuar")
            print("---------------------------------------------------")
            print("\n")
            self.display_menu()
        elif accion_elegida == "i":
            m.deleteDoctor()
            print("\n")
            input("Presiona enter para continuar")
            print("---------------------------------------------------")
            print("\n")
            self.display_menu()
        elif accion_elegida == "j":
            m.getDoctors()
            doctor = input("Selecciona un doctor: ")
            t.createSingleAppoitment(doctor)
            print("\n")
            input("Presiona enter para continuar")
            print("---------------------------------------------------")
            print("\n")
            self.display_menu()
        elif accion_elegida == "k":
            m.getDoctors()
            doctor = input("Selecciona un doctor: ")
            t.createMultiAppoitment(doctor)
            print("\n")
            input("Presiona enter para continuar")
            print("---------------------------------------------------")
            print("\n")
            self.display_menu()
        elif accion_elegida == "l":
            t.getAllAppoitmentsByDoctor()
            print("\n")
            input("Presiona enter para continuar")
            print("---------------------------------------------------")
            print("\n")
            self.display_menu()
        elif accion_elegida == "m":
            p.getPatients()
            paciente = input("Ingresa DNI de paciente: ")
            t.getAllAppoitmentsByDoctor()
            turno = input("Ingresa ID de turno: ")
            t.setAppoitment(int(turno), int(paciente))
            print("\n")
            input("Presiona enter para continuar")
            print("---------------------------------------------------")
            print("\n")
            self.display_menu()
        elif accion_elegida == "n":
            t.getAllAppoitmentsByDoctor()
            turno = input("Ingresa ID de turno: ")
            t.deleteAppointment(int(turno))
            print("\n")
            input("Presiona enter para continuar")
            print("---------------------------------------------------")
            print("\n")
            self.display_menu()
        
        
             
        