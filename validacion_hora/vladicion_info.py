from ejecucion_sp import *
import mensaje as men
from  correo import *
import pandas as pd 

def validationInformacion(intervalo,	base_de_datos,	tabla,	campo_fecha,	campo_hora,	sp_name,	nombre_infrome,	usu_telegram,	host,correos_destinatarios): 
    try:
        import mysql.connector
        import schedule
        import time
        from datetime import datetime, timedelta

        # Configura la conexión a tu base de datos MySQL
        db_config = {
            "host": host,
            "user": "juanaya6582",
            "password": "1,zcmb0PFpQdK0Z9UJfc",
            "database": base_de_datos
        }

        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
        except Exception as e:
            error = f"❌ERROR: Conexión {nombre_infrome}❌ {str(e)}"
            men.enviar_mensajerror(error)

        # Horas validación
        hora_actual= datetime.now().hour
        hora_anterior= hora_actual - intervalo
        Fecha_actal = datetime.now()
        Fecha_actal=Fecha_actal.strftime('%Y-%m-%d')     
        # Fecha validacion 

        dia_actual= datetime.now().strftime('%Y-%m-%d')

        query=f"SELECT MAX(HOUR({campo_hora})) FROM {tabla} WHERE DATE({campo_fecha}) ='{dia_actual}';" 
        try:
            cursor.execute(query)
            resultado = cursor.fetchone()[0]
        except Exception as e:
            error = f"❌ERROR: validacion de hoy {nombre_infrome}❌ {str(e)}"
            men.enviar_mensajerror(error)

        contador=0
        while resultado is None or resultado == 0:
            sp_ejecute(sp_name,base_de_datos,host)
            query=f"SELECT MAX(HOUR({campo_hora})) FROM {tabla} WHERE DATE({campo_fecha}) ='{dia_actual}';" 
            try:
                cursor.execute(query)
                resultado = cursor.fetchone()[0]
            except Exception as e:
                error = f"❌ERROR: validacion de hoy {nombre_infrome}❌ {str(e)}"
                men.enviar_mensajerror(error)

            contador += 1
            if contador >0:
                break

        if resultado is not None and resultado != 0:

            query=f"SELECT COUNT(*) FROM {tabla} WHERE DATE({campo_fecha}) ='{dia_actual}' AND HOUR({campo_hora}) BETWEEN %s AND %s;"
            query1=f"SELECT * FROM {tabla} WHERE DATE({campo_fecha}) ='{dia_actual}' AND HOUR({campo_hora}) BETWEEN %s AND %s;"  
            try:
                cursor.execute(query, (hora_anterior, hora_actual))
                resultado = cursor.fetchone()[0]
                
                cursor.execute(query1, (hora_anterior, hora_actual))
                data = cursor.fetchall()
                
                if data:
                    column_names = [desc[0] for desc in cursor.description]
                    df = pd.DataFrame(data, columns=column_names)
                else:
                    df = pd.DataFrame()  # DataFrame vacío

            except Exception as e:
                error = f"❌ERROR: validación de Intervalo {hora_anterior} a {hora_actual} {nombre_infrome}❌ {str(e)}"
                men.enviar_mensajerror(error)

            contador = 0
            while resultado is None or resultado == 0:
                sp_ejecute(sp_name,base_de_datos,host)
                query=f"SELECT COUNT(*) FROM {tabla} WHERE DATE({campo_fecha}) ='{dia_actual}' AND HOUR({campo_hora}) BETWEEN %s AND %s;"
                query1=f"SELECT * FROM {tabla} WHERE DATE({campo_fecha}) ='{dia_actual}' AND HOUR({campo_hora}) BETWEEN %s AND %s;"  
                try:
                    cursor.execute(query, (hora_anterior, hora_actual))
                    resultado = cursor.fetchone()[0]
                    
                    cursor.execute(query1, (hora_anterior, hora_actual))
                    data = cursor.fetchall()
                    
                    if data:
                        column_names = [desc[0] for desc in cursor.description]
                        df = pd.DataFrame(data, columns=column_names)
                    else:
                        df = pd.DataFrame()  # DataFrame vacío

                except Exception as e:
                    error = f"❌ERROR: validación de Intervalo {hora_anterior} a {hora_actual} {nombre_infrome}❌ {str(e)}"
                    men.enviar_mensajerror(error)

                contador += 1
                if contador > 0:
                    break

            hora_actual = hora_actual-1
            if resultado is None or resultado ==0:
                print(f'Informacion de {nombre_infrome} Desactualizada en intervalo {hora_anterior} a {hora_actual}')
                fracaso= f"⚠️ALERTA: Informacion de {nombre_infrome} Desactualizada en intervalo {hora_anterior} a {hora_actual}, @{usu_telegram}⚠️"
                men.enviar_mensajefracaso(fracaso)
                enviar_alerta_informe(nombre_infrome,Fecha_actal,hora_anterior, hora_actual,correos_destinatarios)
            else:
                print(f'Infomacion actualizada en el intervalo {hora_anterior} a {hora_actual} registros: {resultado}')
                exito=f"✅EXITO: Informe {nombre_infrome} Infromación Actualizada intervalo {hora_anterior} a {hora_actual} registros: {resultado}✅"
                men.enviar_mensajexito(exito)
        else:
            print(f'Información desactualizda el dia de hoy {dia_actual}')
            fracaso= f'⚠️ALERTA: Información desactualizda el dia de hoy {dia_actual}, {nombre_infrome} @{usu_telegram} ⚠️'
            men.enviar_mensajefracaso(fracaso)
            enviar_alerta_informe_2(nombre_infrome,Fecha_actal,correos_destinatarios)
    except  Exception as e:
        error = f"❌ERROR: Trasabilidad Validacion Bot{e} "
        print(error)
