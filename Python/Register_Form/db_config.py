import MySQLdb
from collections import OrderedDict

conn = MySQLdb.connect(host="", user="root", passwd="root", db="user_info")


class DatabaseFunc:
    """ this is the class to manipulate databases """

    def __init__(self):
        pass

    def insert_record(self, table_name, records):

        global conn
        cursor = conn.cursor()
        columns = self.get_columns()
        cols = []
        columns = OrderedDict((x, y) for x, y in columns)
        for key, value in columns.iteritems():
            if key != columns.keys()[0]:
                cols.append(key)
        str_col = "("
        str_record = "("
        for col in cols:
            if col == cols[-1]:
                str_col += col + ")"
            else:
                str_col += col + ","

        for key, value in records.iteritems():
            if key == records.keys()[-1]:
                if columns[key] == 'int' or columns[key] == 'float' or columns[key] == 'double':
                    str_record += value + ");"
                else:
                    str_record += "'" + value + "');"
            else:
                if columns[key] == 'int' or columns[key] == 'float' or columns[key] == 'double':
                    str_record += value + ","
                else:
                    str_record += "'" + value + "',"

        sql = "INSERT INTO {0} {1} VALUES ".format(table_name, str_col)
        sql += str_record
        cursor.execute(sql)
        conn.commit()
        print "Record Inserted !"

    def get_columns(self):

        global conn
        cursor = conn.cursor()
        sql = "SELECT COLUMN_NAME,DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS " \
              "WHERE TABLE_NAME = 'user_register' AND TABLE_SCHEMA = 'user_info';"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

