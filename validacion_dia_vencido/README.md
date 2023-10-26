/////////////////////////////////////////////////////////////////////////

PROYECTO DE ACTUMATIZACION DE VALIDACIONES DE INFORMECAIÓN PARA INFORMES
ELABORADO POR: Juan David Aya Pesca 

- Se encuentra dividido en dos partes:

    * pagina de crague de informacion al bot.
    * Bot validacio informacion. 

/////////////////////////////////////////////////////////////////////////


-------------------------------------------------------------------------
PAGINA CARGUE DE INOFORMACION AL BOT

Pagina desarrollado en html conectado a python mediante un frendword de pata trabajar desarrollo web 
llamdo flask el cua se encarga de crear un servido de app web para hacer todo el fomulario que se de sarrollo

 *  Formulario: realizado en html el cual se basa de 15 campos que solicitan informacion nesesaria para el 
    funcionamiento perfecto del bot un bothon de enviar el cual se encarga  de transportar la informacion 
    mediente un metodo POSH hacia la app.py la cual se encarga de tramiento.

 *  app.py: realizado en el lenguaje de  programacion python, el cual se encarga de resivir los datos que envia resive
    el formualario los conviete segun la nesecidad que la insercion a la base de datos, se crea una query de mysql que resive la informacion tranformada del formulario para ser cargado a la pagina consumiendo la conexion de conecionbd.py
    para que el bot se sigua alimientado segun la nesecidad.

 *  conecionbd.py: realizado en el leguande de prgramacion python, en el     cual se realizo un funcion que 
    resive parametros de conexion de la base donde se almacena la inofrmacion que alimenta el bot y retorna la conexion para que se pueda hacer el cargue de la informacion al bot.

Este serai el funcionanmiento total como tal de la app web para mas informacion pueden revisar el funcionamiento de el script ene el cual se encuentra documentadas la partes inportantes que se deben tener encenta para crear este script de nuevo o su funcionamiento. 



-------------------------------------------------------------------------
BOT VERIFICADOR INFORMACION ACTUALIZADA DE INFORMES 

- Cargue Inforación al Bot:

 *  Segun la  hora que se ejecuta el bot baja la informacion de la base de datos que se espesifico verificar a esa hora.

- Ciclo for para Interactuar Sobre la Informacion Desacargada:

 *  mediante el ciclo for interactua por cada uno de los registros descargado.
 *  cuando obtiene la informacion de la base de datos  ejecuta la fución de validationInformacion() para cada proceso.

- Función  validationInformacion():

 *  Se iportan las librerias nesesarias para la ejecucion.

 *  la funcion resive los datos nesesarios del proceso para hacer sus correspondientes validaciones
    ////// CAMPOS //////
    hora_ini,hora_fin,intervalo,base_de_datos,domingos,festivos,tabla,campo_fecha,campo_hora,sp_name,nombre_infrome,usu_telegram,nombre_reporting,host,Hora_ejecucion.

 *  Se realiza una conexion a la base de datos, donde se encuentra el proceso a validar segun los datos  registrados.

 *  mediante python y el sitema operativo se calcula la fecha correspondiente al dia de ayer 
        - segun la inofrmacion se valida que si la operacion trabaja los dias domingos o los festivos. 
        - si no trabajan no pasa nd y suigue a la siguiente condicion.
        - de lo contrario si trabaja lo que hace  es que un conexion hacia la base d config calendario.
        - valida si el dia pasado es domingo o festivo, si no es domingo ni festivo entonces sigue a la sigiente
          condicion, de lo contrario en tonces no valida el dia de ayer sino que dos dias a tras.

 *  Ejecuta la función de validar_intervalos la cual resive todos lo datos nesesarios para la ejecución
    ////// CAMPOS //////
    hora_inicio, hora_fin, intervalo_horas,fecha_ayer,database,tbl,campo_fecha,campo_hora,ps_name
        - Lo primero es una condicion de error por si pasa algo el la extructura del codigo para que inprima un error 
        - hace una consula validando si hay informacion de el dia de ayer, si el resultado es si procede 
          hacer la validacion por el intervalo indicado  si el resultado es no ejecuta el sp que alimenta esa inofrmación y 
          vual hacer la misa validacion, si es si hace el verificacion por intervalos si es no hace envia un mesaje informando que la informacion del di ayer se encuntra desactualizada.  

 *  Validacion intervalos segun el intervalo de hora para verificar el bot espiesa a buscar si hay inofrmacion en 
    el  intervalso  especificado si haya  informacion sigue verificando el siguiente intervalo en caso de que no haya informacion se almacena un mesaje en un dicionario de esta manera cuando termine la verificacion de todos los intervalso envia un mesaje motrndo los intervalos sin datos, en caso de que   los intervalos todos tengan informacion 
    envia un mesaje diciendo que la informacion se encuentra actualizada perfectamete 


Adicional todo error que se produsca ya se en la ejecucion de un query de validacion sp o del bot se envia un mesaje notificado del error si se ingresa a validar.  