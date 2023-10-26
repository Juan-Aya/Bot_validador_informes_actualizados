from plantilla_alert import *

def enviar_alerta_informe(nombre_informe, fecha, hora_ini, hora_fin, correos_destinatarios):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    # Generar el contenido HTML utilizando la función del generador
    contenido_html  = generar_contenido_alerta(nombre_informe, fecha, hora_ini, hora_fin)

    # Convierte la cadena de correos separados por comas en una lista
    destinatarios = correos_destinatarios.split(',')
    # Configuración del servidor y las credenciales
    smtp_server = 'mail.groupcos.com.co'
    smtp_port = 465
    username = 'juan.aya@groupcos.com.co'
    password_mail = '18P@!6F86g^p'


    # Crear el objeto del mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = username
    mensaje['To'] = ','.join(destinatarios)
    mensaje['Subject'] = f'⚠️ Alerta: Información de {nombre_informe} Desactualizada. ⚠️'

    mensaje.attach(MIMEText(contenido_html, 'html'))

    # Enviar el correo
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as servidor:
        servidor.login(username, password_mail)
        servidor.send_message(mensaje)
        print('Correo enviado exitosamente.')




def enviar_alerta_informe_2(nombre_informe, fecha,  correos_destinatarios):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    # Generar el contenido HTML utilizando la función del generador
    contenido_html  = generar_contenido_alerta2(nombre_informe, fecha)

    # Convierte la cadena de correos separados por comas en una lista
    destinatarios = correos_destinatarios.split(',')
    # Configuración del servidor y las credenciales
    smtp_server = 'mail.groupcos.com.co'
    smtp_port = 465
    username = 'juan.aya@groupcos.com.co'
    password_mail = '18P@!6F86g^p'


    # Crear el objeto del mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = username
    mensaje['To'] = ','.join(destinatarios)
    mensaje['Subject'] = f'⚠️ Alerta: Información de {nombre_informe} Desactualizada. ⚠️'

    mensaje.attach(MIMEText(contenido_html, 'html'))

    # Enviar el correo
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as servidor:
        servidor.login(username, password_mail)
        servidor.send_message(mensaje)
        print('Correo enviado exitosamente.')

