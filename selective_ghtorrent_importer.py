__author__ = 'valerio cosentino'
import settings
import splitter
import init_process
import create_tables
import create_triggers
import insert_data
import create_indexes
import delete_modified_rows
import datetime

#remember to modify the config.ini with the following parameters and to restart mysql to apply the changes
# SETTINGS (tested)
# innodb_buffer_pool_size = 4G (70-80% of system memory)
# innodb_log_buffer_size = 256M (look at the innodb_log_waits status variable and if it is not 0, increase it)
# innodb_log_file_size = 1G (25%-50% of innodb_buffer_pool_size)
# innodb_flush_log_at_commit = 0
# innodb_flush_log_at_trx_commit = 0
# innodb_flush_method = O_DIRECT (for Linux)
# innodb_doublewrite = 0
# innodb_checksums = 0
# innodb_support_xa = 0
# init_connect = 'SET autocommit=0'
# key_buffer_size=64M
#
# OTHER SETTINGS (not tested)
# innodb_thread_concurrency = 17 or 2 x (number of cores + number of disks)
# innodb_read_io_threads = 16 (4 x number of cores)
# innodb_write_io_threads = 16 (4 x number of cores)
# max_allowed_packet = 32M (increase it if you have blob and text to insert)
#
# remember to SET autocommit=1 in the config.ini after the importation is completed
#  ex: linux -> service mysql restart / windows -> net restart mysql56


def print_info(start_time, msg):
    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time
    print msg + ": " + str(elapsed_time)


def main():

    assert ((settings.ACTIVATE_FILTER_TABLES and settings.ACTIVATE_SELECT_TABLES) == False), \
        "ACTIVATE_SELECT_TABLES and ACTIVATE_FILTER_TABLES cannot be True at the same time"

    #prepare the destination folder and the database
    init_process.main()

    start_time = datetime.datetime.now()

    #split and select/filter the SQL files
    #convert INSERT into INSERT IGNORE
    splitter.main()
    print_info(start_time, "splitter")
    next_time = datetime.datetime.now()

    #create tables in the db and add primary keys on issue_comments, issue_events, pull_request_comment
    create_tables.main()
    print_info(next_time, "create tables")
    next_time = datetime.datetime.now()

    #create triggers in the db
    if settings.ACTIVATE_CREATE_TRIGGERS:
        create_triggers.main()
        print_info(next_time, "create triggers")
        next_time = datetime.datetime.now()

    if not settings.ACTIVATE_ONLY_CREATE_TABLE:
        #insert data into the db (the triggers will filter out the data from deleted projects,
        # however it could be possible to perform other filtering operations
        insert_data.main()
        print_info(next_time, "insert data")
        next_time = datetime.datetime.now()

    #create indexes
    create_indexes.main()
    print_info(next_time, "create indexes")
    next_time = datetime.datetime.now()

    #delete the rows used to take benefit from the insert ignore
    if settings.ACTIVATE_CREATE_TRIGGERS:
        delete_modified_rows.main()
        print_info(next_time, "delete modified rows")

    print_info(start_time, "import process")


if __name__ == "__main__":
    main()
