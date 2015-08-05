__author__ = 'valerio cosentino'

import os
import database_manager as dbman
import settings


def init_destination_folder():
    for f in os.listdir(settings.DESTINATION_FOLDER):
        file_path = os.path.join(settings.DESTINATION_FOLDER, f)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except:
            continue


def init_database():
    dbman.execute_sql_statement("DROP DATABASE IF EXISTS " + dbman.DATABASE)
    dbman.execute_sql_statement("CREATE DATABASE " + dbman.DATABASE)
    dbman.close_connection()


def main():
    init_destination_folder()
    init_database()


if __name__ == "__main__":
    main()
