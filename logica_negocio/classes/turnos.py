import crud.turnos_crud as tur_crud # principalmente necesitamos importar nuestra clase crud, ya que implementaremos sus metodos

from datetime       import datetime # como trabajaremos con fecha usaremos el objeto datetime, de la libreria estandar de Python
from datetime       import timedelta # timedelta nos servira para sumar dias / horas / minutos
from prettytable    import PrettyTable # usaremos la libreria PrettyTable para mejorar visualmente nuestros resultados

class Turno(object):
    
    # de la misma manera que la clase crud solicitaremos en el constructor la conexion a la base de datos
    def __init__(self, connect):
        self.__connect = connect
    
    # implementamos el metodo create de un unico turno.
    def createSingleAppoitment(self, doctor):
        # usamos el input del usuario para obtener los datos 
        fecha       = input("Ingrese Fecha, use el formato DD/MM/AAAA: ")
        hora        = input("Ingrese hora, use formato HH:MM: ")
        duracion    = input("Ingrese duracion de turno en Minutos: ")
        
        # usamos nuestro metodo crud crear turno.
        tur_crud.TurnosCrud(self.__connect).crearTurno(fecha, hora, duracion, doctor, False) 
    
        
    def createMultiAppoitment(self, doctor):
        # pedimos los datos al usuario
        fecha_desde = input("Ingrese Fecha Desde, use el formato DD/MM/AAAA: ") 
        fecha_hasta = input("Ingrese Fecha Hasta, use el formato DD/MM/AAAA: ")
        hora_desde  = input("Ingrese hora desde, use formato HH:MM: ")
        hora_hasta  = input("Ingrese hora hasta, use formato HH:MM: ")
        duracion_turno_str = input("Ingrese duracion de turno en Minutos: ")
        
        # convertimos la duracion en numero
        duracion_turno_int = int(duracion_turno_str) 

        # creamos strings para luego formatearlos a datetime usando la libreria
        f_desde_str = f"{fecha_desde}" # creamos un string con la fecha desde
        h_desde_str = f"{hora_desde}" # creamos un string con la hora desde
        f_hasta_str = f"{fecha_hasta}" # creamos un string con la fecha hasta
        h_hasta_str = f"{hora_hasta}" # creamos un string con la hora hasta
        
        # usamos los codigos de formato para los metodos strftime() y strptime()
        # documentacion: https://docs.python.org/es/3/library/datetime.html?highlight=datetime%20add%20minute#strftime-and-strptime-format-codes
        date_format_str = '%d/%m/%Y' # creamos un formato de fecha
        time_format_str = '%H:%M' # creamos un formato de hora
        
        # transformamos nuestros strings a datetime
        given_date_desde = datetime.strptime(f_desde_str, date_format_str) 
        given_time_desde = datetime.strptime(h_desde_str, time_format_str)
        given_date_hasta = datetime.strptime(f_hasta_str, date_format_str)  
        given_time_hasta = datetime.strptime(h_hasta_str, time_format_str) 
        
        
        app_days = [] # creamos una lista que contendra los turnos
        
        # creamos las variables para loop while
        final_date = given_date_desde # creamos las variables para loop while de fecha
        final_time = given_time_desde # creamos las varianles para loop while de hora
        
        # y el formato final, que combinara la fecha con el turno
        final_datetime_format_str = '%d/%m/%Y %H:%M' 
        
        # corremos el while, en el cual
        while final_date <= given_date_hasta: # mientras la fecha desde sea menor o igual a la fecha hasta
            while final_time < given_time_hasta: # y un while anidado mientras la hora desde sea menor o igual a la hora hasta 
                str1 = datetime.strftime(final_date, date_format_str) # creamos un string con la fecha
                str2 = datetime.strftime(final_time, time_format_str) # creamos un string con la hora
                final_datetime = datetime.strptime(f"{str1} {str2}", final_datetime_format_str) # lo formateamos con el formato final
                app_days.append(final_datetime) # lo agregamos a a lista
                final_time = final_time + timedelta(minutes=duracion_turno_int) # agregamos la duracion del turno para iniciar un nuevo ciclo     
            final_date = final_date + timedelta(days=1) # una vez salimos del ciclo de horario, agreamos un dia para seguir con el ciclo fechas
            final_time = given_time_desde # reseteamos la hora a la hora de inicio para el nuevo ciclo dia
        
        # una vez corrimos el while, nuestra lista de turnos esta completa, la recorremos
        for date in app_days:
            fecha_m = datetime.strftime(date, date_format_str) # formateamos la fecha a string
            hora_m  = datetime.strftime(date, time_format_str) # formateamos la hora a string
            # creamos un turno por cada ciclo, es decir por cada elemento
            tur_crud.TurnosCrud(self.__connect).crearTurno(fecha_m, hora_m, duracion_turno_int, doctor, True)
        
        print(len(app_days), "Turnos Creados con exito") # imprimimos confirmacion
    
    # usamos el metodo obtenerTurnos del crud para implementar la logica
    def getAllAppoitmentsByDoctor(self):
        turnos = tur_crud.TurnosCrud(self.__connect).obtenerTurnos()
        # aprovechamos el uso de listas para mejorar nuestras listas usando Prettytable
        table = [["Id Turno", "Id Medico", "Nombre Med", "Apellido Med", "Fecha", "Hora", "Status"]]
        tab = PrettyTable(table[0])
        # recorremos el objeto que recibimos del metodo obtenerTurnos
        for turno in turnos:
            # y por cada ciclo insertamos nuevas filas a nuestra tabla.
           row = [turno[0],turno[1],turno[2],turno[3],turno[4],turno[5],turno[6]]
           tab.add_row(row)
        print(tab)
    
    # la implememtacion del metodo otorgarTurno() del crud funciona como un UPDATE de los datos en tabla
    def setAppoitment(self, id_paciente, id_turno):
        tur_crud.TurnosCrud(self.__connect).otorgarTurno(id_paciente, id_turno)
    
    # finalmente implementamos una funcion para eliminar turnos    
    def deleteAppointment(self, id_turno):
        tur_crud.TurnosCrud(self.__connect).borrarTurno(id_turno)

        
    
        