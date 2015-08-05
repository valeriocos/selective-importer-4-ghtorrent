__author__ = 'valerio cosentino'

import mysql.connector
from mysql.connector import errorcode

#name of the database to be created
DATABASE = "test"
#parameters to connect to the database
CONFIG = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',
            'port': '3306',
            'raise_on_warnings': False,
            'charset': 'utf8',
            'buffered': True
        }

cnx = mysql.connector.connect(**CONFIG)


def activate_connection():
    global cnx
    if not cnx.is_connected():
       cnx = mysql.connector.connect(**CONFIG)


def execute_sql_statement(content):
    activate_connection()
    cursor = cnx.cursor()
    cursor.execute(content)
    cursor.close()


def check_table_exists(table_name):
    activate_connection()
    found = True
    cursor = cnx.cursor()
    query = "SELECT COUNT(*) " \
            "FROM information_schema.TABLES " \
            "WHERE TABLE_NAME = %s AND TABLE_SCHEMA = %s;"
    arguments = [table_name, DATABASE]
    cursor.execute(query, arguments)
    counter = cursor.fetchone()[0]
    cursor.close()

    if not counter:
        found = False

    return found


def close_connection():
    cnx.close()