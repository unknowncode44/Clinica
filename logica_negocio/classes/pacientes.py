import crud.pacientes_crud as pac_crud
from prettytable import PrettyTable

class Paciente(object):
    
    def __init__(self, connect):
        self.__connect = connect
    
    def create_patient(self):
        nombre = input("Ingresa el nombre del paciente: ")
        apellido = input("Ingresa el apellido del paciente: ")
        DNI = input("Ingresa el DNI del paciente: ")
        print("\n")
        
        pac_crud.PacientesCrud(self.__connect).crearPaciente(nombre, apellido, DNI)
    
    def getPatients(self):
       pacientes = pac_crud.PacientesCrud(self.__connect).obtenerPacientes()
       table = [["Id Paciente", "Nombre Paciente", "Apellido Paciente", "DNI Paciente"]]
       tab = PrettyTable(table[0])
       for paciente in pacientes:
           row = [paciente[0],paciente[1],paciente[2],paciente[3]]
           tab.add_row(row)
       print(tab)
       
    def getPatient(self):
        dni = input("Ingresa el DNI del paciente: ")
        paciente = pac_crud.PacientesCrud(self.__connect).obtenerPaciente(dni)
        pac_tupla = paciente[0]
        table = [["Id Paciente", "Nombre Paciente", "Apellido Paciente", "DNI Paciente"]]
        tab = PrettyTable(table[0])
        row = [pac_tupla[0],pac_tupla[1],pac_tupla[2],pac_tupla[3]]
        tab.add_row(row)
        print(tab)
        
    
    def updatePatient(self):
        dni = input("Ingresa el DNI del paciente: ")
        paciente = pac_crud.PacientesCrud(self.__connect).obtenerPaciente(dni)
        print(paciente)
        print("\n")
        print("1) Modificar Nombre")  
        print("2) Modificar Apellido")
        print("\n")
        opcion = input("Elije opcion y presiona enter: ") 
        
        if str(opcion) == "1":
            nombre = input("Ingresa el nombre del paciente: ") 
            pac_crud.PacientesCrud(self.__connect).modificar_nombre_paciente(nombre, dni)
        else:
            apellido = input("Ingresa el apellido del paciente: ") 
            pac_crud.PacientesCrud(self.__connect).modificar_apellido_paciente(apellido, dni)
    
    def deletePatient(self):
        dni = input("Ingresa el DNI del paciente: ")
        paciente = pac_crud.PacientesCrud(self.__connect).obtenerPaciente(dni)    
        print(paciente)
        print("\n")
        opcion = input("Seguro que quiere eliminar al paciente: s / n : ")
        if opcion == "s":
            pac_crud.PacientesCrud(self.__connect).borrar_paciente(dni)
