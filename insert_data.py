__author__ = 'valerio cosentino'

import os
import database_manager as dbconn
import settings


def main():
    files = [f for f in os.listdir(settings.DESTINATION_FOLDER) if f.startswith(settings.INSERT_FILE)]
    sorted_files = prioritize(files)

    for f in sorted_files:
        import_sql_file(f)
        os.unlink(settings.DESTINATION_FOLDER + '/' + f)


def prioritize(files):
    output = []
    for p in settings.PRIORITY_LIST:
        for f in files:
            if (settings.INSERT_FILE + p) == f:
                output.append(f)
                files.remove(f)

    output = output + files

    return output


def import_sql_file(f):
    mysql_command = "mysql --user=" + dbconn.CONFIG.get('user') + " --password=" + dbconn.CONFIG.get('password') + \
                    " --host=" + dbconn.CONFIG.get('host') + " --port=" + dbconn.CONFIG.get('port') + \
                    " --default_character_set utf8 " + dbconn.DATABASE + " < " + settings.DESTINATION_FOLDER + "/" + f
    os.system(mysql_command)


if __name__ == "__main__":
    main()