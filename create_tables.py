__author__ = 'valerio cosentino'

import os
import re
import database_manager as dbman
import settings


def main():
    dbman.execute_sql_statement("USE " + dbman.DATABASE)

    files = os.listdir(settings.DESTINATION_FOLDER)
    for f in files:
        if f.startswith(settings.CREATE_FILE):
            extract_content(f)
    dbman.close_connection()


def extract_content(f):
    with open(settings.DESTINATION_FOLDER + "/" + f, 'r') as content_file:
        content = content_file.read()
        contents = content.split(";")
        drop = contents[0]
        create = contents[1]

        if 'issue_comments' in f:
            create = re.sub('mediumtext NOT NULL', 'int(11) PRIMARY KEY', create)
        elif 'issue_events' in f:
            create = re.sub('mediumtext NOT NULL', 'int(11) PRIMARY KEY', create)
        elif 'pull_request_comments' in f:
            create = re.sub('mediumtext NOT NULL', 'int(11) PRIMARY KEY', create)
            create = re.sub('UNIQUE KEY.*,', '', create)
        elif 'forks' in f:
            create = re.sub("PRIMARY KEY.*,\n", '', create, re.DOTALL)
            create = re.sub("UNIQUE KEY", "PRIMARY KEY", create, re.DOTALL)

        create = re.sub('UNIQUE KEY.*\n', '', create, re.DOTALL)
        create = re.sub('\n\s*KEY.*', '', create, re.DOTALL)
        create = re.sub('CONSTRAINT.*REFERENCES.*\n', '', create, re.DOTALL)
        create = re.sub(',\s*\)\s*ENGINE', ') ENGINE', create, re.DOTALL)

        dbman.execute_sql_statement(drop)
        dbman.execute_sql_statement(create)


if __name__ == "__main__":
    main()
