import crud.pacientes_crud as pac_crud # principalmente necesitamos importar nuestra clase crud, ya que implementaremos sus metodos
from prettytable import PrettyTable# usaremos la libreria PrettyTable para mejorar visualmente nuestros resultados

class Paciente(object):
    
    # de la misma manera que la clase crud solicitaremos en el constructor la conexion a la base de datos
    def __init__(self, connect):
        self.__connect = connect
    
    # implementamos el metodo create de pacientes 
    def create_patient(self):
        nombre = input("Ingresa el nombre del paciente: ")
        apellido = input("Ingresa el apellido del paciente: ")
        DNI = input("Ingresa el DNI del paciente: ")
        print("\n")
        
        pac_crud.PacientesCrud(self.__connect).crearPaciente(nombre, apellido, DNI)
     # implementamos el metodo get de pacientes 
    def getPatients(self):
       pacientes = pac_crud.PacientesCrud(self.__connect).obtenerPacientes()
       # aprovechamos el uso de listas para mejorar nuestras listas usando Prettytable
       table = [["Id Paciente", "Nombre Paciente", "Apellido Paciente", "DNI Paciente"]]
       tab = PrettyTable(table[0])
       
       # recorremos el objeto que recibimos del metodo crud
       for paciente in pacientes:
           # e insertamos las filas en la tabla
           row = [paciente[0],paciente[1],paciente[2],paciente[3]]
           tab.add_row(row)
       print(tab) # imprimimos el objeto tab de la libreria
    
    # metodo get de solo un paciente   
    def getPatient(self):
        dni = input("Ingresa el DNI del paciente: ")
        paciente = pac_crud.PacientesCrud(self.__connect).obtenerPaciente(dni)
        pac_tupla = paciente[0]
        table = [["Id Paciente", "Nombre Paciente", "Apellido Paciente", "DNI Paciente"]]
        tab = PrettyTable(table[0])
        row = [pac_tupla[0],pac_tupla[1],pac_tupla[2],pac_tupla[3]]
        tab.add_row(row)
        print(tab)
        
    # metodo para actualizar datos del paciente
    def updatePatient(self):
        dni = input("Ingresa el DNI del paciente: ")
        paciente = pac_crud.PacientesCrud(self.__connect).obtenerPaciente(dni)
        print(paciente)
        print("\n")
        print("1) Modificar Nombre")  
        print("2) Modificar Apellido")
        print("\n")
        opcion = input("Elije opcion y presiona enter: ") 
        
        # con una condicion podemos preguntar si queremos modificar el nombre o el apellido
        if str(opcion) == "1":
            nombre = input("Ingresa el nombre del paciente: ") 
            pac_crud.PacientesCrud(self.__connect).modificar_nombre_paciente(nombre, dni)
        else:
            apellido = input("Ingresa el apellido del paciente: ") 
            pac_crud.PacientesCrud(self.__connect).modificar_apellido_paciente(apellido, dni)
    
    # finalmente el metdodo de eliminacion de paciente
    def deletePatient(self):
        dni = input("Ingresa el DNI del paciente: ")
        paciente = pac_crud.PacientesCrud(self.__connect).obtenerPaciente(dni)    
        print(paciente)
        print("\n")
        opcion = input("Seguro que quiere eliminar al paciente: s / n : ")
        if opcion == "s":
            pac_crud.PacientesCrud(self.__connect).borrar_paciente(dni)
