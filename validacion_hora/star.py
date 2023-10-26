import mensaje as msg
from conecionbd import *
from vladicion_info import *
from datetime import datetime
import concurrent.futures

def validar_proceso(id, hora_ini, hora_fin, intervalo, base_de_datos, domingos, festivos, tabla, campo_fecha, campo_hora, sp_name, nombre_informe, usu_telegram, nombre_reporting, host, Hora_ejecucion, tipo_validacion, correos_destinatarios):
    hora_actual = datetime.now().hour
    if hora_actual > hora_ini and hora_actual < hora_fin:
        if domingos == 1 or festivos == 1:
            pass
        else:
            validationInformacion(intervalo, base_de_datos, tabla, campo_fecha, campo_hora, sp_name, nombre_informe, usu_telegram, host, correos_destinatarios)

try:
    query = "SELECT * FROM tb_bot_validador_informes_cos_bi WHERE tipo_validacion = 'DIA_ACTUAL';"
    cursor.execute(query)
    resultado = cursor.fetchall()
    
    # Crear un ThreadPoolExecutor con hasta 4 hilos de ejecución concurrente
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        for item in resultado:
            executor.submit(validar_proceso, *item)

except Exception as e:
    error = f"❌ERROR: Inicial BOt❌ {str(e)}"
