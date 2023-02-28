import mysql.connector
from mysql.connector import Error # importamos el metodo Error para manejar los errores


#  creamos una clase para manejar las acciones SQL del paciente
class PacientesCrud:
    
    # en el metodo inicial pasaremos la coneccion a la base de datos
    
    def __init__(self, db):
        self.__db           = db
        self.__table_name   = "paciente"
    
    # creamos metodo para crear paciente
    def crearPaciente(self, nombre, apellido, DNI):
        try:
            cursor = self.__db.cursor()
            cursor.execute("INSERT INTO paciente VALUES (%s, %s, %s, %s)", (0,f'{nombre}',f'{apellido}',f'{DNI}'))
            self.__db.commit()
            print("Paciente Creado con Exito")
        except Error as err:
            print(f"{err}")
    
    # creamos metodo para obtener todos los pacientes
    def obtenerPacientes(self):
        query  = """
            SELECT *
            FROM paciente;
            """
        try:
            cursor = self.__db.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        
        except Error as err:
            print(f"{err}")
            
    # creamos metodo para obtener un unico paciente       
    def obtenerPaciente(self, dni):
        query = """SELECT * FROM paciente WHERE DNI = (%s) """
        try:
            cursor = self.__db.cursor()
            query = """SELECT * FROM paciente WHERE DNI = (%s) """
            cursor.execute(query, (dni,))
            result = cursor.fetchall()
            if len(result) == 0:
                print("No existe paciente con ese DNI")
            else: 
                return result
        except Error as err:
            print(f"{err}")

    # metodo para modificar nombre de paciente            
    def modificar_nombre_paciente(self, nombre, dni):
        sql_query1 = """UPDATE paciente SET paciente.nombre = (%s) WHERE dni = (%s) """
        try:
            cursor = self.__db.cursor()
            cursor.execute(sql_query1, (nombre, dni))
            self.__db.commit()
            print("Actualizado con exito")
        except Error as err:
            print(f"Error: '{err}'") # si hay errores los imprimimos por consola
    
    # metodo para modificar apellido de paciente        
    def modificar_apellido_paciente(self, apellido, dni):
        sql_query1 = """UPDATE paciente SET paciente.apellido = (%s) WHERE dni = (%s) """
        try:
            cursor = self.__db.cursor()
            cursor.execute(sql_query1, (apellido, dni))
            self.__db.commit()
            print("Actualizado con exito")
        except Error as err:
            print(f"Error: '{err}'") # si hay errores los imprimimos por consola
            
    
    # metodo para eliminar paciente        
    def borrar_paciente(self, dni):
        sql_query1 = """DELETE FROM paciente WHERE paciente.dni = (%s) """
        try:
            
            cursor = self.__db.cursor()
            cursor.execute(sql_query1, (dni,))
            self.__db.commit()
            print("Eliminado con exito")
        except Error as err:
            print(f"Error: '{err}'") # si hay errores los imprimimos por consola
        