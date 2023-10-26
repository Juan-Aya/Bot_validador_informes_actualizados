from conecionbd import *
from validation_info import *
from datetime import datetime

hora = datetime.now().hour

query = f"SELECT * FROM tb_bot_validador_informes_cos_bi WHERE Hora_ejecucion = {hora} AND tipo_validacion ='DIA_VENCIDO';"
cursor.execute(query)

resultado = cursor.fetchall()



for id,	hora_ini,	hora_fin,	intervalo,	base_de_datos,	domingos,	festivos,	tabla,	campo_fecha,	campo_hora,	sp_name,	nombre_infrome,	usu_telegram,	nombre_reporting,	host, Hora_ejecucion,tipo_validacion,correos_destinatarios in resultado:
        
    hora_inicio = hora_ini
    print(Hora_ejecucion)
    intervalo_horas = intervalo
    database = base_de_datos
    fetivos=festivos
    tbl=tabla
    ps_name= sp_name
    user='juanaya6582'
    password='1,zcmb0PFpQdK0Z9UJfc'

    if hora <= Hora_ejecucion: 
        validationInformacion(hora_inicio, hora_fin, intervalo_horas,host,user,password,database,domingos,fetivos,tbl,campo_fecha,campo_hora,ps_name,nombre_infrome,correos_destinatarios)  

connection.close()
cursor.close()