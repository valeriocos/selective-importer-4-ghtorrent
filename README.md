# selective-importer-4-ghtorrent
a fast and easy way to import a MySQL dump of GHTorrent, selecting only the tables and indexes you need

#HowTo

- set the parameters to connect to your database in ```database_manager.py``` 
- set the importation parameters in ```settings.py``` (name of the dump file, tables to filter/select, etc.)
- optionally you can modify the files ```create_triggers.py``` and ```create_indexes.py``` 
to 1) filter data while populating the database 2) define indexes on the columns you want
- execute  ```selective_ghtorrent_importer.py ```

#Tuning the target database
In order to speed-up the importation process, you should modify the MySQL ```config.ini``` with the following settings:
```
# SETTINGS (tested)
# innodb_buffer_pool_size = 4G (70-80% of system memory)
# innodb_log_buffer_size = 256M (if the innodb_log_waits status variable is not 0, increase the buffer size)
# innodb_log_file_size = 1G (25%-50% of innodb_buffer_pool_size)
# innodb_flush_log_at_commit = 0
# innodb_flush_log_at_trx_commit = 0
# innodb_doublewrite = 0
# innodb_checksums = 0
# innodb_support_xa = 0
# init_connect = 'SET autocommit=0'
# key_buffer_size=64M
#
# OTHER SETTINGS (not tested)
# innodb_flush_method = O_DIRECT (for Linux)
# innodb_thread_concurrency = 17 or 2 x (number of cores + number of disks)
# innodb_read_io_threads = 16 (4 x number of cores)
# innodb_write_io_threads = 16 (4 x number of cores)
# max_allowed_packet = 32M (increase it if you have blob and text to insert)
```

#Evaluation
Tests executed on a Intel Core i7-3720 QM CPU @ 2.60GHz 2.60GHz with just 4GB of RAM.

Unzipped Dump Size   | Triggers | No Triggers | Tables
------------- | ------------- | ------------- | -------------
19.2 GB       |     7h30m     |     1h51m     |      all
42.2 GB       |    skipped    |     12h10m    |      all
63.7 GB       |    skipped    |      19h      |      all
96.3 GB       |    skipped    |      28h      |      all
