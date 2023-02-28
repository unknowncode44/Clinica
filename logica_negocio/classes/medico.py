import crud.medico_crud as med_crud
from prettytable import PrettyTable

class Medico(object):
    
    def __init__(self, connect):
        self.__connect = connect
    
    def create_doctor(self):
        nombre = input("Ingresa el nombre del medico: ")
        apellido = input("Ingresa el apellido del medico: ")
        matricula = input("Ingresa la matricula del medico: ")
        especialidad = input("Ingresa la especialidad del medico: ")
        print("\n")
        
        med_crud.MedicosCrud(self.__connect).crearMedico(nombre,apellido,matricula,especialidad)
    
    def getDoctors(self):
       medicos = med_crud.MedicosCrud(self.__connect).obtenerMedicos()
       table = [["Id Paciente", "Nombre", "Apellido", "Especialidad", "Matricula"]]
       tab =PrettyTable(table[0])
       
       for medico in medicos:
           row = [medico[0], medico[1], medico[2], medico[3], medico[4]]
           tab.add_row(row)
       print(tab) 
    
       
    def getDoctor(self):
        matricula = input("Ingresa matricula del doctor: ")
        doctor = med_crud.MedicosCrud(self.__connect).obtenerMedico(matricula)
        pac_tupla = doctor[0]
        table = [["Id Paciente", "Nombre", "Apellido", "Especialidad", "Matricula"]]
        tab = PrettyTable(table[0])
        row = [pac_tupla[0],pac_tupla[1],pac_tupla[2],pac_tupla[3],pac_tupla[4]]
        tab.add_row(row)
        print(tab)
    
    
    def deleteDoctor(self):
        matricula = input("Ingresa matricula del doctor: ")
        doctor = med_crud.MedicosCrud(self.__connect).obtenerMedico(matricula)    
        print(matricula)
        print("\n")
        opcion = input("Seguro que quiere eliminar al paciente: s / n : ")
        if opcion == "s":
            med_crud.MedicosCrud(self.__connect).borrar_medico(matricula)  
           
   