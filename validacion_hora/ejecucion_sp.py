import  mensaje as mns
# Fucion para Ejecutar SP para caragar información

def sp_ejecute(ps_name,db,host):
  import mysql.connector

  cnx = mysql.connector.Connect(user='juanaya6582',password='1,zcmb0PFpQdK0Z9UJfc',host=f'{host}',database=f'{db}')# Conexion Servidor mysql
  cursor=cnx.cursor() 
  query= f'CALL {ps_name}();' # Query de ejecucion consulta SP
  try:
    cursor.execute(query) # Ejecutar la query 
    cnx.commit() # Guardar cambios 
  except Exception as e:
    error = f'❌Error: {ps_name} ❌ {str(e)}'
    mns.enviar_mensajerror(error)
    
    
