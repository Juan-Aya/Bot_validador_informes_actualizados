Proyecto de automatización de validaciones de información para informes

Autor: Juan David Aya Pesca

Fecha: 2023-10-25

Resumen

Este proyecto automatiza las validaciones de información para informes. Se divide en dos partes:

Página de carga de información al bot: Esta página, desarrollada en HTML y Python, permite a los usuarios ingresar información sobre los informes que deben ser validados.
Bot verificador de información actualizada de informes: Este bot, desarrollado en Python, descarga la información de los informes de la base de datos y la valida.
Descripción

Página de carga de información al bot

La página de carga de información al bot consta de los siguientes elementos:

Un formulario con 15 campos: Estos campos solicitan información sobre el informe, como la hora de inicio, la hora de finalización, el intervalo de tiempo, la base de datos, etc.
Un botón de envío: Este botón envía la información ingresada al bot.
La página está desarrollada en HTML y Python. El formulario utiliza el lenguaje de programación HTML, mientras que el botón de envío utiliza Python para enviar la información a la función app.py.

La función app.py

La función app.py recibe la información ingresada en el formulario y la convierte en una consulta MySQL. Luego, utiliza la conexión de la base de datos para insertar la información en la tabla de informes.

La conexión de la base de datos

La conexión de la base de datos está desarrollada en Python. La función conecionbd.py recibe los parámetros de conexión de la base de datos y retorna una conexión.

Bot verificador de información actualizada de informes

El bot verificador de información actualizada de informes consta de los siguientes elementos:

Un ciclo for: Este ciclo for recorre la tabla de informes y descarga la información de cada informe.
Una función validationInformacion(): Esta función valida la información de cada informe.
La función validationInformacion()

La función validationInformacion() recibe la información de un informe y la valida. La función realiza las siguientes tareas:

Calcula la fecha del día anterior.
Valida si el informe trabaja los días domingos y festivos.
Si el informe trabaja los días domingos y festivos, verifica si el día anterior fue domingo o festivo.
Si el día anterior no fue domingo ni festivo, la función valida la información del informe.
Si el informe no tiene información del día anterior, la función ejecuta el procedimiento almacenado sp_name para cargar la información.
Una vez que la información del informe está cargada, la función verifica los intervalos de tiempo especificados.
Validación de intervalos de tiempo

La función validationInformacion() verifica los intervalos de tiempo especificados para el informe. La función realiza las siguientes tareas:

Realiza una consulta MySQL para verificar si hay información en el intervalo especificado.
Si hay información en el intervalo especificado, la función continúa con el siguiente intervalo.
Si no hay información en el intervalo especificado, la función almacena un mensaje de error en un diccionario.
Mensajes de error

El bot verificador de información actualizada de informes envía mensajes de error si se producen errores durante la validación. Los mensajes de error se almacenan en un diccionario.

Conclusiones

Este proyecto automatiza las validaciones de información para informes, lo que reduce el tiempo y el esfuerzo necesarios para realizar estas tareas. El proyecto es escalable y se puede adaptar a diferentes tipos de informes.