from prettytable import PrettyTable
from db_connection import Connection
import settings
import MySQLdb
import os
import glob

connection_obj = Connection()


class DatabaseFunc:
    """ this is the class to manipulate databases """

    conn = ""
    cursor = ""
    db_name = ""

    def __init__(self):
        pass

    def create_database(self, database_name):

        database_is = settings.get_database()

        try:

            global conn
            global cursor
            global db_name
            db_name = database_name

            query = "CREATE DATABASE {0};".format(database_name)

            if database_is == "mysql":
                conn = connection_obj.connect_db()
                cursor = conn.cursor()
                cursor.execute(query)
                conn.commit()
                conn = connection_obj.connect_db(db_arg=database_name)
                cursor = conn.cursor()

            elif database_is == "sqlite":
                conn = connection_obj.connect_db(db_arg=database_name)
                cursor = conn.cursor()

            elif database_is == "postgresql":
                conn = connection_obj.connect_db()
                cursor = conn.cursor()
                cursor.execute(query)
                conn.close()
                conn = connection_obj.connect_db(db_arg=database_name)
                cursor = conn.cursor()

            print "Database Successfully Created"
            return True

        except MySQLdb.ProgrammingError as e:
            print e

    def open_database(self, database_name):

        try:
            global conn
            global cursor
            global db_name
            db_name = database_name

            conn = connection_obj.connect_db(db_arg=database_name)
            cursor = conn.cursor()
            return True

        except MySQLdb.OperationalError as e:
            print e

    def delete_database(self, database_name):

        database_is = settings.get_database()

        try:
            global conn
            global cursor
            if database_is == "mysql" or database_is == "postgresql":
                conn = connection_obj.connect_db()
                cursor = conn.cursor()
                sql = "DROP DATABASE {0};".format(database_name)
                cursor.execute(sql)

            elif database_is == "sqlite":
                try:
                    database_name += ".db"
                    os.remove(database_name)
                except Exception as e:
                    print e
            return True
        except Exception as e:
            print e

    def create_table(self, table_name, columns, primary):

        database_is = settings.get_database()
        sql = ""
        try:
            if database_is == "mysql":
                sql = "CREATE TABLE {0} ( ID integer auto_increment, ".format(table_name)
            elif database_is == "postgresql":
                sql = "CREATE TABLE {0} ( ID SERIAL, ".format(table_name)
            elif database_is == "sqlite":
                sql = "CREATE TABLE {0} ( ID INTEGER PRIMARY KEY AUTOINCREMENT, ".format(table_name)

            sql += columns

            if database_is == "sqlite":
                sql += ");"
            else:
                if primary == "":
                    sql += ", PRIMARY KEY (ID));".format(primary)
                else:
                    sql += ", PRIMARY KEY (ID,{0}));".format(primary)

            print sql
            cursor.execute(sql)
            conn.commit()
            print "Table Successfully Created"
            return True
        except Exception as e:
            print e

    def show_databases(self):

        database_is = settings.get_database()
        sql = ""

        try:
            conn = connection_obj.connect_db()
            my_cursor = conn.cursor()
            if database_is == "mysql":
                sql = "SHOW SCHEMAS;"
            elif database_is == "postgresql":
                sql = "SELECT datname as Databases FROM pg_database WHERE datistemplate = false;"
            my_cursor.execute(sql)
            col_names = [cn[0] for cn in my_cursor.description]
            rows = my_cursor.fetchall()

            x = PrettyTable(col_names)
            x.padding_width = 1
            for row in rows:
                x.add_row(row)
            print(x)

        except Exception as e:
            print e

    def show_sqlite_database(self):

        db = glob.glob("*.db")
        for i in range(len(db)):
            print "| ", db[i], " |"

    def show_database_tables(self):

        database_is = settings.get_database()
        sql = ""
        try:
            if database_is == "mysql":
                sql = "SHOW TABLES;"
            elif database_is == "postgresql":
                sql = "SELECT table_name FROM information_schema.tables WHERE table_schema='public';"
            elif database_is == "sqlite":
                sql = "SELECT tbl_name FROM sqlite_master where type='table';"

            cursor.execute(sql)
            col_names = [cn[0] for cn in cursor.description]
            rows = cursor.fetchall()
            if rows:
                x = PrettyTable(col_names)
                x.padding_width = 1
                for row in rows:
                    x.add_row(row)
                print(x)
                return True
            else:
                return False

        except Exception as e:
            print e

    def show_table(self, table_name):

        try:
            sql = "SELECT * FROM {0} order by ID".format(table_name)
            cursor.execute(sql)
            col_names = [cn[0] for cn in cursor.description]
            rows = cursor.fetchall()

            x = PrettyTable(col_names)
            x.padding_width = 1
            for row in rows:
                x.add_row(row)
            print(x)

        except Exception as e:
            print e

    def is_table_exist(self, table_name):

        try:
            sql = "SELECT * FROM {0}".format(table_name)
            cursor.execute(sql)
            return True
        except Exception as e:
            print e

    def get_columns(self, table_name):

        database_is = settings.get_database()
        sql = ""

        try:
            if database_is == "mysql":
                sql = "SELECT COLUMN_NAME,DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS " \
                      "WHERE TABLE_NAME = '{0}' AND TABLE_SCHEMA = '{1}';".format(table_name, db_name)

            elif database_is == "postgresql":
                sql = "SELECT column_name,data_type FROM information_schema.columns " \
                      "WHERE table_name='{0}';".format(table_name).lower()

            elif database_is == "sqlite":
                sql = "PRAGMA table_info({0})".format(table_name)

            cursor.execute(sql)
            result = cursor.fetchall()
            if database_is == "sqlite":
                res = []
                for row in result:
                    res.append((row[1], row[2]))
                return res
            else:
                return result

        except Exception as e:
            print e

    def insert_record(self, table_name, cols, records):

        try:
            sql = "INSERT INTO {0} {1} values(".format(table_name, cols)
            sql += records
            cursor.execute(sql)
            conn.commit()
            return True
        except Exception as e:
            print e

    def update_record(self, table_name, data, col_data):

        try:
            sql = "UPDATE {0} SET ".format(table_name)
            sql += data
            sql += " WHERE ID={0};".format(col_data)
            cursor.execute(sql)
            conn.commit()
            return True
        except Exception as e:
            print e

    def delete_table(self, table_name):

        try:
            sql = "DROP TABLE {0}".format(table_name)
            cursor.execute(sql)
            conn.commit()
            return True
        except Exception as e:
            print e

    def delete_record(self, table_name, col_data):

        try:
            sql = "DELETE FROM {0} where ID = {1};".format(table_name, col_data)
            cursor.execute(sql)
            conn.commit()
            return True
        except Exception as e:
            print e

    def close_database(self):

        conn.commit()
        conn.close()

    def add_column(self, table_name, col_name, col_type, size=""):

        try:
            if size == "":
                sql = "ALTER TABLE {0} ADD {1} {2};".format(table_name, col_name, col_type)
            else:
                sql = "ALTER TABLE {0} ADD {1} {2}({3});".format(table_name, col_name, col_type, size)
            cursor.execute(sql)
            conn.commit()
            return True
        except Exception as e:
            print e

    def delete_column(self, table_name, col_name):

        try:
            sql = "ALTER TABLE {0} DROP COLUMN {1}".format(table_name, col_name)
            cursor.execute(sql)
            conn.commit()
            return True
        except Exception as e:
            print e

    def check_for_available(self, table_name):

        try:
            sql = "SELECT * FROM {0}".format(table_name)
            cursor.execute(sql)
            results = cursor.fetchall()
            IDs = []
            for result in results:
                IDs.append(result[0])
            return IDs
        except Exception as e:
            print e
