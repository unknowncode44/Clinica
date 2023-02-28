import mysql.connector # importamos mysql.connector
from mysql.connector import Error # importamos el metodo Error para manejar los errores

# creamos un metodo statico para crear un decorador singleton, ya que nuestra clase solo se debe instanciar una vez
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
    

@singleton
class Database(object):
    
    # Los siguientes metodos seran los primarios para empezar con la base de datos
    
    # El siguiente metodo sera el constructor para definir el host, usuario y contrasena 
    # para luego conectarnos a la base de datos durante la creacion de la misma
    
    def __init__(self, host, username, password, database_name):
        self.__host         = host
        self.__username     = username
        self.__password     = password
        self.__database_name = database_name   
    
    # y crearemos un metodo para creacion de base de datos
    def createDatabase(self):
        # creamos una conexion
        db = mysql.connector.connect(
            host = self.__host,
            user = self.__username,
            paswd = self.__password,
        )
        
        cursor = db.cursor() # el cursor mysql nos permitira ejecutar comandos sql
        
        # implementamos un bloque try except
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS "+self.__database_name)
            return "Se creo la base de datos "+self.__database_name+" exitosamente"
        
        except Error as err:
            print(f"{err}")
        
    
    # una vez tengamos creada una base datos crearemos un metodo para conectarnos a la misma
    def createConecction(self):
        try:
            db = mysql.connector.connect(
            host = self.__host,
            user = self.__username,
            passwd = self.__password,
            database = self.__database_name
        )
            print("Conexion a "+self.__database_name+" exitosa!")
            return db
        # sino nos devuelve el error
        except Error as err:
            print(f"Error: '{err}'")
        
        
        self.__db = db
        
    # crearemos tambien un metodo para crear tablas, en caso de que necesitemos
    def createTable(self, table_name):
        # creamos una conexion
        db = mysql.connector.connect(
            host = self.__host,
            user = self.__username,
            paswd = self.__password,
        )
        
        cursor = db.cursor() # el cursor mysql nos permitira ejecutar comandos sql
        
        # implementamos un bloque try except
        try:
            cursor.execute("CREATE TABLE IF NOT EXISTS "+table_name)
            return "Se creo la base de datos "+self.__database_name+" exitosamente"
        
        except Error as err:
            print(f"{err}")
    
    
    # adicionalmente, crearemos un metodo para ejecutar queries SQL
    def executeQuery(self, query):
        # invocamos el metodo cursor() de nuestra conexion, este metodo nos permite ingresar queries SQL
        self.__query = query
        self.__db.cursor.execute(self.__query) # el cursor va a ejecutar el query que pasemos por argumento
        self.__db.commit() # el metodo commit() nos asegura que los comandos que pasamos fueron correctamente implementados
        print("Consulta ejecutada exitosamente") # si esta ok imprime un mensaje de confirmacion
    
