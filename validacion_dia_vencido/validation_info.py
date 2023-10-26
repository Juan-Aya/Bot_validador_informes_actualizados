from ejecucion_sp import *
from correo import *
import mensaje as mensaje 
from datetime import datetime, timedelta

# Funcion para validar la información que este actualizada del los informes

def validationInformacion(hora_inicio, hora_fin, intervalo_horas,host,user,password,database,domingos,fetivos,tbl,campo_fecha,campo_hora,ps_name,nombre_infrome,correos_destinatarios):
    import mysql.connector
    from datetime import datetime, timedelta

    # Configura la conexión a tu base de datos MySQL
    db_config = {
        'host': host,
        'user': user,
        'password': password,
        'database': database
    }

    # Función para consultar la base de datos en intervalos de tiempo personalizables
    def validar_intervalos(hora_inicio, hora_fin, intervalo_horas,fecha_ayer,database,tbl,campo_fecha,campo_hora,ps_name):
        try:
            print(ps_name)
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            query = f"SELECT DISTINCT DATE({campo_fecha}) FROM {database}.{tbl} WHERE DATE({campo_fecha}) = '{fecha_ayer}';" #Query validador de Información
            try:
                cursor.execute(query) 
                result = cursor.fetchone() #Obtener resultados 
            except Exception as e:
                error = f'❌Error: Informe {nombre_infrome} Validacion Fecha Tabla ❌ {str(e)}'
                mns.enviar_mensajerror(error)
                print(f'Error al ejecutar consulta validación {error}')

            contador = 0
            while result is None:
                sp_ejecute(ps_name,database,host)
                query = f"SELECT DISTINCT DATE({campo_fecha}) FROM {database}.{tbl} WHERE DATE({campo_fecha}) = {fecha_ayer});" #Query validador de Información
                try:
                    cursor.execute(query) 
                    result = cursor.fetchone() #Obtener resultados 
                except Exception as e:
                    error = f'❌Error: Informe {nombre_infrome} Validacion Fecha Tabla ❌ {str(e)}'
                    mns.enviar_mensajerror(error)
                    print(f'Error al ejecutar consulta validación {error}')

                contador += 1
                if contador > 0:
                    break
                
            if result is not None:
                intervalo = timedelta(hours=intervalo_horas)
                hora_actual = datetime.now().replace(hour=hora_inicio, minute=0, second=0)

                datos_faltantes = []

                while hora_actual < datetime.now().replace(hour=hora_fin, minute=0, second=0):
                    hora_fin_intervalo = hora_actual + intervalo
                    fecha_ayer_str = fecha_ayer
                    hora_inicio_str = hora_actual.strftime('%H')
                    hora_fin_str = hora_fin_intervalo.strftime('%H')
                    print(fecha_ayer_str,hora_inicio_str,hora_fin_str)
                    

                    query = f"SELECT COUNT(*) FROM {tbl} WHERE DATE({campo_fecha}) = %s AND HOUR({campo_hora}) BETWEEN %s AND %s;"

                    try:
                        cursor.execute(query, (fecha_ayer_str, hora_inicio_str, hora_fin_str))
                        resultado = cursor.fetchone()
                    except Exception as e:
                        error = f'❌Error: Informe {nombre_infrome} Validacion de intervalos ❌ {str(e)}'
                        mns.enviar_mensajerror(error)
                        print(f'Error al ejecutar consulta validacion de intervalos {error}')

                    if resultado[0] == 0:
                        datos_faltantes.append((hora_inicio_str, hora_fin_str))

                    hora_actual += intervalo

                if datos_faltantes:
                    for inicio, fin in datos_faltantes:
                        # Fracaso Intervalos 
                        print(f"No hay datos entre {inicio} y {fin}")
                        fracaso = f'⚠️ALERTA: Informe {nombre_infrome} No hay datos entre {inicio} y {fin}⚠️'
                        mns.enviar_mensajefracaso(fracaso)
                        enviar_alerta_informe(nombre_infrome,fecha_ayer_str,inicio,fin,correos_destinatarios)
                else:
                    # EXITO total
                    print("La información se encuentra actualizada perfectamente.")
                    exito = f'✅EXITO: Informe {nombre_infrome} Infromación Actualizada✅'
                    mns.enviar_mensajexito(exito)
            else:
                # FRACASO DIA AYER
                print('Informacion del dia de ayer Desactializada')
                fracaso = f'⚠️ALERTA: Informe {nombre_infrome} Informacion del dia de ayer Desactializada⚠️'
                mns.enviar_mensajefracaso(fracaso)
                enviar_alerta_informe_2(nombre_infrome, fecha_ayer_str)

        except Exception as e:
            print(f"Error al consultar la base de datos: {str(e)}")
        finally:
            cursor.close()
            connection.close()

    fecha_ayer = datetime.now() - timedelta(days=1)
    # Define las horas de inicio, fin e intervalo que desees
    fecha_ayer=fecha_ayer.strftime('%Y-%m-%d')
    if domingos == 1 or fetivos == 1:
        cnx= mysql.connector.connect(user='juanaya6582',password='1,zcmb0PFpQdK0Z9UJfc',host='172.70.7.60', database='bbdd_config') # conexion 
        cursor=cnx.cursor()
        query=f'SELECT Dia,Festivo FROM  bbdd_config.tb_calendario_day WHERE Fecha ="{fecha_ayer}";'# Query para validar 
        try:
            cursor.execute(query) 
            resul = cursor.fetchone()
        except Exception as e:
            error = f'❌Error: Informe {nombre_infrome} Validacion Calendario config❌ {str(e)}'
            mns.enviar_mensajerror(error)
            print(f'Error al ejecutar la consulta del Calendario Principal{error}')
        Dia = resul[0] # obtener la el nombre del dia en esta variable 
        festivo = resul[1] # obtener el dia se es festivo (1) si no (0)

        if Dia == "Domingo" or festivo ==1: # Validacion donde sea domingo
            if domingos == 1 and fetivos == 1 and Dia == "Lunes" and festivo ==1:
                fecha_ayer = datetime.now() - timedelta(days=3)
                fecha_ayer=fecha_ayer.strftime('%Y-%m-%d')
            else:
                fecha_ayer = datetime.now() - timedelta(days=2)
                fecha_ayer=fecha_ayer.strftime('%Y-%m-%d')
 # restar un dia 

    # Llama a la función para realizar las validaciones
    validar_intervalos(hora_inicio, hora_fin, intervalo_horas,fecha_ayer,database,tbl,campo_fecha,campo_hora,ps_name)




# 'host': '10.26.53.99',
    # 'user': 'juanaya6582',
    # 'password': '1,zcmb0PFpQdK0Z9UJfc',
    # 'database': 'bbdd_ec_pbla_provident_cobranza'
    #"SELECT COUNT(*) FROM tb_informe_factura_provident_cobranza WHERE DATE(statusdatetime2) = %s AND HOUR(statusdatetime) BETWEEN %s AND %s;"