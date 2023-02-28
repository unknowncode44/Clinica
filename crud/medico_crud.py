from mysql.connector import Error # importamos el metodo Error para manejar los errores

#  creamos una clase para manejar las acciones SQL del paciente
class MedicosCrud:
    
    # en el metodo inicial pasaremos la coneccion a la base de datos
    
    def __init__(self, connection):
        self.__connection = connection
    
    # creamos metodo para crear paciente
    def crearMedico(self, nombre, apellido, matricula, especialidad):
        try:
            cursor = self.__connection.cursor()
            cursor.execute("INSERT INTO medico VALUES (%s, %s, %s, %s, %s)", (0,f'{nombre}',f'{apellido}',f'{especialidad}',f'{matricula}'))
            self.__connection.commit()
            print("Medico Creado con Exito")
        except Error as err:
            print(f"{err}")
    
    # creamos metodo para obtener todos los pacientes
    def obtenerMedicos(self):
        query  = """
            SELECT *
            FROM medico;
            """
        try:
            cursor = self.__connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        
        except Error as err:
            print(f"{err}")
            
    # creamos metodo para obtener un unico paciente       
    def obtenerMedico(self, matricula):
        query = """SELECT * FROM medico WHERE matricula = (%s) """
        try:
            cursor = self.__connection.cursor()
            cursor.execute(query, (matricula,))
            result = cursor.fetchall()
            if len(result) == 0:
                print("No existe medico con esa matricula")
            else: 
                return result
        except Error as err:
            print(f"{err}")

            
    
    # metodo para eliminar paciente        
    def borrar_medico(self, matricula):
        sql_query1 = """DELETE FROM medico WHERE medico.matricula = (%s) """
        try:
            
            cursor = self.__connection.cursor()
            cursor.execute(sql_query1, (matricula,))
            self.__connection.commit()
            print("Eliminado con exito")
        except Error as err:
            print(f"Error: '{err}'") # si hay errores los imprimimos por consola
        