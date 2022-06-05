import mysql.connector as mysql

def connect():
    try:
        connection = mysql.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            dabase = 'web_scraping'
        )
        print("Se ha Conectado a la Base de Datos")
        return connection
    except mysql.Error as err:
        print("Ha ocurrido un erro: "+err)
        