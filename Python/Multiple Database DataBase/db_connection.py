import settings


class Connection:
    def __init__(self):
        pass

    def connect_db(self, db_arg=""):
        """It connect to the database as per the user's choice"""

        database_is = settings.get_database()

        if database_is == "mysql":
            import MySQLdb
            host_db = "localhost"
            user_db = "root"
            pass_db = "root"
            conn = MySQLdb.connect(host=host_db, user=user_db, passwd=pass_db, db=db_arg)

        elif database_is == "sqlite":
            import sqlite3
            db_arg += ".db"
            conn = sqlite3.connect(db_arg)

        elif database_is == "postgresql":
            import psycopg2
            from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
            user = "postgres"
            password = "root"
            host = "127.0.0.1"
            port = "5432"
            conn = psycopg2.connect(database=db_arg, user=user, password=password, host=host, port=port)
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        return conn
