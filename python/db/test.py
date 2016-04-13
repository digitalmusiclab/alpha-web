from mysql.connector import MySQLConnection, Error
from db_config import read_db_config
import json
import ast

def connect():
    """ Connect to MySQL database """

    db_config = read_db_config("config.ini", "mysql")
    table_config = read_db_config("config.ini", "tabledata")

    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print('connection established.')
            spotifyCall(conn, table_config)
        else:
            print('connection failed.')

    except Error as error:
        print(error)

    finally:
        conn.close()
        print('Connection closed.')

def spotifyCall(conn, table_config):
    columns = ast.literal_eval(table_config['columns'])

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM track limit 0, 15")

    rows = cursor.fetchall()
    print('Total Row(s):', cursor.rowcount)

    savedbjson('db.json', rows, columns)



def savedbjson(filename, rows, columns):
    temp = True;
    f = open(filename, 'w')
    f.write('{"database":[\n')
    for row in rows:
        if (not(temp)):
            f.write(',')
        f.write("{")
        for i in range(0, len(columns)-1):
            f.write('"'+columns[i]+'": "'+row[i]+'"')
            if(i!=len(columns)-2):
                f.write(',')
        f.write("}\n")
        temp = False;
    f.write("]}")

if __name__ == '__main__':
    connect()
