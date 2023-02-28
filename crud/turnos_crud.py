import mysql.connector
from mysql.connector import Error # importamos el metodo Error para manejar los errores


import logica_negocio.classes.medico as med

#  creamos una clase para manejar las acciones SQL del paciente
class TurnosCrud:
 
    # en el metodo inicial pasaremos la coneccion a la base de datos
    
    def __init__(self, db):
        self.__db           = db
        self.__table_name   = "turnos"
    
    # creamos metodo para crear nuevo turno
    def crearTurno(self, fecha, hora, duracion, doctor, multi):
        query = "INSERT INTO turno VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        lugar = "Clinica 1" 
        try:
            cursor = self.__db.cursor()
            cursor.execute(query, (0, fecha, hora, lugar, int(duracion), "4", int(doctor), "disp"))
            self.__db.commit()
            if multi == True:
                pass
            else:
                print("Turno Creado con Exito!")
        except Error as err:
            print(f"{err}")
    
    # creamos metodo para obtener todos los turnos
    def obtenerTurnos(self):
        query  = """
            SELECT turno.id_turno, medico.id_medico, medico.nombre, medico.apellido, turno.fecha, turno.horario, turno.status
            FROM turno
            INNER JOIN medico ON turno.medico=medico.id_medico;
            """
        result = None
        try:
            cursor = self.__db.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        
        except Error as err:
            print(f"{err}")
    
    # editar turno (otorgar)
    def otorgarTurno(self, id_turno, id_paciente):
        query = """UPDATE turno SET turno.status = 'tomado',turno.paciente = (%s) WHERE id_turno = (%s) """
        try:
            cursor = self.__db.cursor()
            cursor.execute(query, (id_paciente, id_turno))
            self.__db.commit()
            print("Turno otorgado con exito")
        except Error as err:
            print(f"{err}")
    
    # eliminar turnos
    def borrarTurno(self, id_turno):
        sql_query1 = """DELETE FROM turno WHERE turno.id_turno = (%s) """
        try:
            cursor = self.__db.cursor()
            cursor.execute(sql_query1, (id_turno,))
            self.__db.commit()
            print("Turno eliminado correctamente")
        except Error as err:
            print(f"{err}")
        
    
        
    
   