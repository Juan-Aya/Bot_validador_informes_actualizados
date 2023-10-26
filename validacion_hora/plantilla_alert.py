def generar_contenido_alerta(nombre_informe, fecha, hora_ini, hora_fin):
    # Contenido HTML del correo
    contenido_html = f"""<!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{
                background-color: #EEEEEE;
                text-align: center;
                font-family: Arial, sans-serif;
            }}

            .container {{
                background-color: #ffffff;
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
            }}

            .header {{
                background-color: #E1E1E1 ;
                color: #97022A;
                padding: 10px;
            }}

            .content {{
                padding: 20px;
                margin-bottom: 20px;
            }}

            .footer {{
                 margin-bottom: 20px;
                background-color: #E1E1E1;
                color: #97022A;
                font-weight: bold;
                font-size: 20px;
                padding: 8px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Alerta: Información de "{nombre_informe}" no se encuentra actualizada</h1>
            </div>
            <div class="content">
                <p><b>Estimado usuario,</b></p>
                <p><b>Le informamos que la información de "{nombre_informe}" no ha sido actualizada en el día {fecha}, desde la hora {hora_ini} hasta la hora {hora_fin}. Le solicitamos revisar las fuentes de información correspondientes.</b></p>
                <p><b>Este es un correo de aviso de que la información no se encuentra actualizada, no responder.</b></p>
            </div>
            <div class="footer">
                <p>Business Intelligence</p>
                <p style="text-align: right;">Group Cos</p>
            </div>
        </div>
    </body>
    </html>"""

    return contenido_html


def generar_contenido_alerta2(nombre_informe, fecha):
    # Contenido HTML del correo
    contenido_html = f"""<!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{
                background-color: #EEEEEE;
                text-align: center;
                font-family: Arial, sans-serif;
            }}

            .container {{
                background-color: #ffffff;
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
            }}

            .header {{
                background-color: #E1E1E1 ;
                color: #97022A;
                padding: 10px;
            }}

            .content {{
                padding: 20px;
                margin-bottom: 20px;
            }}

            .footer {{
                 margin-bottom: 20px;
                background-color: #E1E1E1;
                color: #97022A;
                font-weight: bold;
                font-size: 20px;
                padding: 8px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Alerta: Información de "{nombre_informe}" no se encuentra actualizada</h1>
            </div>
            <div class="content">
                <p><b>Estimado usuario,</b></p>
                <p><b>Le informamos que la data de "{nombre_informe}" no ha sido actualizada en el día {fecha}. Le solicitamos revisar las fuentes de información correspondientes.</b></p>
                <p><b>Este es un correo de aviso de que la información no se encuentra actualizada, no responder.</b></p>
            </div>
            <div class="footer">
                <p>Business Intelligence</p>
                <p style="text-align: right;">Group Cos</p>
            </div>
        </div>
    </body>
    </html>"""

    return contenido_html