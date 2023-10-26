import mysql.connector

db_config = {
        'host': '172.70.7.60',
        'user': 'juanaya6582',
        'password': '1,zcmb0PFpQdK0Z9UJfc',
        'database': 'bbdd_groupcos_repositorio_rpa'
    }
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()