__author__ = 'valerio cosentino'

DUMP_FILE = 'mysql-2013-10-12.sql'

#ACTIVATE_SELECT_TABLES and ACTIVATE_FILTER_TABLES cannot be True at the same time
ACTIVATE_SELECT_TABLES = False
SELECTED_TABLES = ['projects']

ACTIVATE_FILTER_TABLES = True
FILTERED_TABLES = ['schema_info', 'counters']

ACTIVATE_ONLY_CREATE_TABLE = False
ACTIVATE_CREATE_TRIGGERS = False

#used for inserting data through triggers
PRIORITY_LIST = ['projects.sql', 'issues.sql', 'commits.sql', 'pull_requests.sql']

#the folder that contains the GhTorrent dump
SOURCE_FOLDER = 'dump'
#the folder where the different SQL files will be put
DESTINATION_FOLDER = 'output'

CREATE_FILE = 'create.'
INSERT_FILE = 'insert.'
