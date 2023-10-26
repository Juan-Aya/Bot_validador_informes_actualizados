from flask import Flask, render_template, request
from conecionbd import conectar_bd
from flask import redirect, url_for
import jsonify


app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('formulario.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    try:
        # Obtén los datos del formulario
        hora_ini = request.form['hora_ini']
        hora_fin = request.form['hora_fin']
        intervalo = request.form['intervalo']
        base_de_datos = request.form['base_de_datos']
        domingos = request.form['domingos']
        festivos = request.form['festivos']
        tabla = request.form['tabla']
        campo_fecha = request.form['campo_fecha']
        campo_hora = request.form['campo_hora']
        sp_name = request.form['sp_name']
        nombre_infrome = request.form['nombre_infrome']
        usu_telegram = request.form['usu_telegram']
        nombre_reporting = request.form['nombre_reporting']
        host = request.form['host']
        Hora_ejecucion= request.form['Hora_ejecucion']

        if not (hora_ini.isnumeric() and hora_fin.isnumeric() and intervalo.isnumeric() and domingos.isnumeric() and festivos.isnumeric()):
         return jsonify(success=False, message="Los campos numéricos deben contener números válidos.")

        # Establece la conexión a la base de datos
        connection = conectar_bd()
        cursor = connection.cursor()

        # Inserta los datos en la base de datos
        query = """INSERT INTO tb_bot_validador_informes_cos_bi (hora_ini,	hora_fin,	intervalo,	base_de_datos,	domingos,	festivos,	tabla,	campo_fecha,	campo_hora,	sp_name,	nombre_infrome,	usu_telegram,	nombre_reporting,	host,	Hora_ejecucion) 
                                VALUES (%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s)"""
        cursor.execute(query, (hora_ini,	hora_fin,	intervalo,	base_de_datos,	domingos,	festivos,	tabla,	campo_fecha,	campo_hora,	sp_name,	nombre_infrome,	usu_telegram,	nombre_reporting,	host,	Hora_ejecucion))
        connection.commit()

        return redirect(url_for('formulario', success=True, message="Datos insertados correctamente en la base de datos."))

    except Exception as e:
        return f"Error al insertar datos en la base de datos: {str(e)}"
    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)
