from database import database as bd
import logica_negocio.classes.pacientes as pac
import logica_negocio.classes.medico as med
import logica_negocio.classes.turnos as tur
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


#   configuracion para conectar la bd
config = {
"host"      : "localhost",
"user"      : "root",
"passwd"    : "BullDog143$",
"db_name"   : "clinica"
}

#   creamos la instancia de la clase Database, usamos el patron singleton para asegurar que solo
#   se instancie una vez 
db = bd.Database(config["host"], config["user"], config["passwd"], config["db_name"])

print("Creando conexion")
time.sleep(0.50)

#   creamos la conexion llamando al metodo createConnection() de nuestra clase Database
#   usaremos este connect como argumento en nuestro DataTransferObject
connect = db.createConecction()


# 
@singleton # usamos el decorador singleton por que nuestra clase LogicaNegocio solo se instanciara una vez  
class LogicaNegocio(object):

    # menu de trabajo
    def display_menu(self):
        # instanciamos las clases que usaremos en el menu
        # gracias al patron singleton estas instancias solo se crearan una vez
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
            "m": "Otorgar turno"

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
            p.getPatients()
            paciente = input("Ingresa DNI de paciente: ")
            t.getAllAppoitmentsByDoctor()
            turno = input("Ingresa ID de turno: ")
            t.deleteAppointment(int(turno), int(paciente))
            print("\n")
            input("Presiona enter para continuar")
            print("---------------------------------------------------")
            print("\n")   
                
        
             
        