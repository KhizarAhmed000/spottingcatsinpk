import mysql.connector

print("hello")

connection = mysql.connector.connect(host='localhost',
                                         database='cats',
                                         user='root',
                                         )
if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)                                         

                            
