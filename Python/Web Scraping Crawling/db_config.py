# coding=utf-8
import MySQLdb

conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="root", db="kraftly_db")


class DatabaseFunc:
    """ this is the class to manipulate databases """

    def __init__(self):
        pass

    def insert_record(self, record):
        """
        This is function used to insert the data into database
        :param record: it is a dictionary of the records
        """
        global conn
        cursor = conn.cursor()

        sql = "INSERT INTO trending_items (name, price, cat_shop, details) values(%s, %s, %s, %s);"
        cursor.execute(sql, (record['name'], int(record['price']), record['cat_shop'].encode('utf8'), record['details'].encode('utf8')))
        conn.commit()
