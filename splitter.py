__author__ = 'valerio cosentino'

import settings


def main():
    sql_file = None
    table_name = None

    with open(settings.SOURCE_FOLDER + '/' + settings.DUMP_FILE, 'r') as f:
        for line in f:
            if line.startswith('DROP TABLE'):
                if sql_file:
                    sql_file.close()

                table_name = get_table_name(line)

                if settings.ACTIVATE_SELECT_TABLES:
                    if table_name in settings.SELECTED_TABLES:
                        sql_file = open(settings.DESTINATION_FOLDER + '/' + settings.CREATE_FILE + table_name + '.sql', 'w')
                    else:
                        sql_file = None
                elif settings.ACTIVATE_FILTER_TABLES:
                    if table_name not in settings.FILTERED_TABLES:
                        sql_file = open(settings.DESTINATION_FOLDER + '/' + settings.CREATE_FILE + table_name + '.sql', 'w')
                    else:
                        sql_file = None
                else:
                    sql_file = open(settings.DESTINATION_FOLDER + '/' + settings.CREATE_FILE + table_name + '.sql', 'w')

            elif line.startswith('INSERT INTO'):
                if sql_file:
                    if sql_file.name.startswith(settings.DESTINATION_FOLDER + '/' + settings.CREATE_FILE):
                        sql_file.close()
                        if not settings.ACTIVATE_ONLY_CREATE_TABLE:
                            sql_file = open(settings.DESTINATION_FOLDER + '/' + settings.INSERT_FILE + table_name + '.sql', 'w')

            if sql_file:
                if not sql_file.closed:
                    if line.startswith('INSERT INTO'):
                        if not settings.ACTIVATE_ONLY_CREATE_TABLE:
                            sql_file.write(line.replace('INSERT', 'INSERT IGNORE'))
                    elif (not '/*!' in line) and (not line.startswith('--')) and (not 'LOCK TABLES' in line) \
                            and (not line.startswith('\n')):
                        sql_file.write(line)

    if sql_file:
        sql_file.close()


def get_table_name(line):
    return line.split('`')[1]


if __name__ == "__main__":
    main()