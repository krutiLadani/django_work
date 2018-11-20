from db_config import DatabaseFunc
import os
import settings

clear = lambda: os.system('clear')  # It clears the screen
conn = DatabaseFunc()  # Object of DatabaseFunc where all the database stuff is available
settings.init()


class Database:
    """This is an Application to manipulate database"""

    def __init__(self):
        pass

    def create_database_data(self):
        """creates the database"""

        while True:
            dbname = raw_input("\nEnter Database Name :")  # get database name
            if conn.create_database(dbname):  # Calling the function of DatabaseFunc Class
                self.print_new_db_action()  # Display Sub screen which have table options

    def open_database_data(self):
        """open the existing database"""
        while True:
            dbname = raw_input("\nEnter Database Name :")  # get database name
            if conn.open_database(dbname):  # calling the function of Databasefunc Class
                self.print_old_db_action()

    def delete_database(self):
        """deleting the existing database"""
        while True:
            dame = raw_input("\nEnter Database Name :")
            if conn.delete_database(dame):
                if 'Y' == raw_input("Do you want to delete another ? (y/n) :").upper():
                    continue
                else:
                    self.print_home()
                    break

    def create_table_data(self):
        """create new table into database"""
        tbname = raw_input("\nEnter Table Name :").upper()  # get table name to create
        exist = conn.is_table_exist(tbname)
        if exist:
            print "Table Already Exist"
            return False
        else:
            col_no = input("\nEnter Number Of Columns :")  # get number of columns
            columns = ""
            primary = ""
            primaryFlag = 0
            if settings.get_database() == "sqlite":
                primaryFlag = 1
            keys = []
            for col in range(col_no):
                print "\n<<<<< Enter Column {0} Data >>>>>".format(col + 1)
                while True:
                    col_name = raw_input("Columns Name :").upper()  # column name
                    if col_name == "ID":
                        print "ID column is default"
                    else:
                        break
                data_type = raw_input("Datatype :").upper()  # get datatype of column
                if data_type != "int" and data_type != "integer":
                    size = raw_input("Size :")  # size of column
                while True:
                    if primaryFlag == 0:
                        pk = raw_input("Is Primary Key ? (y/n) :").upper()  # is primary key or not
                        if pk == 'Y':
                            pk = "PRIMARY KEY"
                            primaryFlag = 1
                            null = ""
                            primary = col_name
                            break
                        elif pk == 'N':
                            pk = ""
                            break
                        else:
                            print "Invalid Entry !"
                    else:
                        pk = ""
                        break

                if pk != "PRIMARY KEY":
                    fk = raw_input("Is Foreign Key ? (y/n)").upper()
                    if fk == 'Y':
                        foreign_table = raw_input("Enter Reference Table Name :").upper()
                        foreign_column = raw_input("Enter Reference Table's Primary Column :").upper()
                        if conn.is_table_exist(foreign_table):
                            fk = "FOREIGN KEY ({0}) REFERENCES {1}({2})".format(col_name, foreign_table, foreign_column)
                            keys.append(fk)
                        else:
                            print "Table Not Exist"
                    elif fk == 'N':
                        pass

                    else:
                        print "Invalid Entry"

                if pk == "":
                    while True:
                        null = raw_input("Is NOT NULL ? (y/n) :").upper()  # is null or not null
                        if null == 'Y':
                            null = "NOT NULL"
                            break
                        elif null == 'N':
                            null = ""
                            break
                        else:
                            print "Invalid Entry !"

                if col == col_no - 1:
                    if size == "":
                        per_col = "{0} {1} {2} {3}".format(col_name, data_type, size, null)
                    else:
                        per_col = "{0} {1}({2}) {3}".format(col_name, data_type, size, null)
                else:
                    if size == "":
                        per_col = "{0} {1} {2} {3},".format(col_name, data_type, size, null)
                    else:
                        per_col = "{0} {1}({2}) {3},".format(col_name, data_type, size, null)

                columns += per_col  # concat columns and making the query

            for key in keys:
                if key == keys[-1]:
                    columns += key
                else:
                    columns += key + ","

            if conn.create_table(tbname, columns, primary):
                return True

    def insert_record_data(self, tb_name):
        """Inserting the records into table"""
        rows = conn.get_columns(tb_name)
        sql = ""
        cols = "("
        for row in rows:
            if row[1] == "date":
                print "Date Format : YYYY-MM-DD"
            if row != rows[0]:
                if row == rows[-1]:
                    if row[1] != 'integer':
                        sql = sql + "'" + raw_input("Enter {0} of type({1}) :".format(row[0], row[1])) + "');"
                    else:
                        sql = sql + raw_input("Enter {0} of type({1}) :".format(row[0], row[1])) + ");"
                    cols += row[0] + ")"
                else:
                    if row[1] != 'integer':
                        sql = sql + "'" + raw_input("Enter {0} of type({1}) :".format(row[0], row[1])) + "'" + ","
                    else:
                        sql = sql + raw_input("Enter {0} of type({1}) :".format(row[0], row[1])) + ","
                    cols += row[0] + ","

        if conn.insert_record(tb_name, cols, sql):
            print "Record Inserted"
        else:
            print "Enter Valid Values!"

    def delete_table_data(self, table_name):
        """Delete the table from database"""
        if conn.delete_table(table_name):
            print "Table Successfully Deleted"
            self.print_old_db_action()

    def delete_record_data(self, table_name):
        """Deletes the Records from table"""
        while True:
            column_data = input("Enter ID :")
            Ids = conn.check_for_available(table_name)
            if not column_data in Ids:
                print "ID not available"
            else:
                conn.delete_record(table_name, column_data)
                print "Record Deleted"
                self.print_table_action(table_name)

    def update_record_data(self, tbl_name):
        """updates the records of table"""
        while True:
            column_data = input("Enter ID :")
            Ids = conn.check_for_available(tbl_name)
            if not column_data in Ids:
                print "ID not available"
            else:
                rows = conn.get_columns(tbl_name)
                sql = ""
                for row in rows:
                    if row != rows[0]:
                        value = raw_input("Enter {0} :".format(row[0]))
                        if value != "":
                            if row[1] == "date":
                                print "Date Format : YYYY-MM-DD"
                            if row == rows[-1]:
                                if row[1] != 'integer':
                                    sql = sql + " " + row[0] + "='" + value + "'"
                                else:
                                    sql = sql + " " + row[0] + "=" + value
                            else:
                                if row[1] != 'integer':
                                    sql = sql + " " + row[0] + "='" + value + "'" + ","
                                else:
                                    sql = sql + " " + row[0] + "=" + value + ","

                if conn.update_record(tbl_name, sql, column_data):
                    print "Record Updated"
                    self.print_table_action(tbl_name)
                else:
                    print "Enter Valid Values!"

    def add_column_data(self, table_name):
        """Adds the column into existing table"""
        while True:

            column_name = raw_input("Enter New Column Name :").upper()
            column_type = raw_input("Enter New Column Data type :")
            size = raw_input("Enter Size :")
            if size == "":
                if conn.add_column(table_name, column_name, column_type):
                    return True
            else:
                if conn.add_column(table_name, column_name, column_type, size):
                    return True

    def delete_column_data(self, table_name):
        """deletes the existing column of table"""
        while True:
            col_name = raw_input("Enter Column Name To Delete :").upper()
            if conn.delete_column(table_name, col_name):
                return True

    def choose_database(self):
        """get the database which user wants to use"""
        clear()
        print "************************  Select Your Database Server ************************\n"
        print "\t1. MySQL"
        print "\t2. SQLite"
        print "\t3. PostgreSQL"

        print "\ntype exit to close"

        while True:

            choose = raw_input("Enter Your Choice Here :")  # get the choice

            if choose == '1':

                settings.set_database("mysql")
                break

            elif choose == '2':

                settings.set_database("sqlite")
                break

            elif choose == '3':

                settings.set_database("postgresql")
                break

            elif choose == 'exit':
                exit(0)

            else:
                print "Enter Valid Entry !"

        print settings.get_database()
        self.print_home()

    def print_home(self):  # To display Database Options

        clear()
        print "*************************  Wel-Come to {0}  *************************\n".format(
            settings.get_database().upper())
        print "\t1. Create Database"
        print "\t2. Open Database"
        print "\t3. See All Database"
        print "\t4. Delete Database"
        print "\t5. Change Database Server"

        print "\ntype exit to close"

        while True:

            choose = raw_input("Enter Your Choice Here :")  # get the choice

            if choose == '1':
                self.create_database_data()

            elif choose == '2':
                self.open_database_data()

            elif choose == '3':
                if settings.get_database() == "mysql" or settings.get_database() == "postgresql":
                    conn.show_databases()
                else:
                    conn.show_sqlite_database()

            elif choose == '4':
                if settings.get_database() == "mysql" or settings.get_database() == "postgresql":
                    conn.show_databases()
                else:
                    conn.show_sqlite_database()
                self.delete_database()

            elif choose == '5':
                self.choose_database()

            elif choose == 'exit':
                exit(0)  # exit to close the application

            else:
                print "Invalid Choice !!"

    def print_new_db_action(self):  # To display Table Options to manipulate it

        clear()
        print "*************************  Wel-Come to {0}  *************************\n".format(
            settings.get_database().upper())
        print "\t1. Create Table"
        print "\ntype exit to close"

        while True:

            choose = raw_input("Enter Your Choice Here :")  # getting the choice
            if choose == '1':
                if self.create_table_data():
                    self.print_old_db_action()

            elif choose == 'exit':
                conn.close_database()
                exit(0)
            else:
                print "Invalid Choice !!"

    def print_old_db_action(self):  # To display Table Options to manipulate it

        clear()
        print "****************************  Wel-Come to {0}  ****************************\n".format(
            settings.get_database().upper())
        print "\t1. Create Table"
        print "\t2. Show Tables"
        print "\ntype exit to close"

        while True:

            choose = raw_input("Enter Your Choice Here :")  # getting the choice

            if choose == '1':
                self.create_table_data()
                while True:
                    con = raw_input("Do you want to add another Table ? (y/n) :").upper()
                    if con == 'Y':
                        self.create_table_data()
                    else:
                        self.print_old_db_action()

            elif choose == '2':
                self.show_table_data()
                break

            elif choose == 'exit':
                conn.close_database()
                exit(0)

            else:
                print "Invalid Choice !!"

    def show_table_data(self):

        clear()
        print "****************************  Wel-Come to {0}  ****************************\n".format(
            settings.get_database().upper())
        if conn.show_database_tables():
            while True:

                table = raw_input("Enter Table Name From Above :").upper()  # getting the choice
                print "nothing"
                if conn.is_table_exist(table):
                    self.print_table_action(table)
                    break
                else:
                    print "Invalid Table Name"
        else:
            raw_input("There are no any tables available press enter key to create table")
            self.print_new_db_action()

    def print_table_action(self, tablename):

        clear()
        print "*************************  Wel-Come to {0}  *************************\n".format(
            settings.get_database().upper())

        conn.show_table(tablename)

        print "\t1. Insert Record"
        print "\t2. Update Record"
        print "\t3. Delete Record"
        print "\t4. Drop Table"
        print "\t5. Add Column"
        print "\t6. Delete Column"
        print "\t7. Change Table"
        print "\t8. Close DATABASE"

        print "\ntype exit to close"

        while True:

            choose = raw_input("Enter Your Choice Here :")  # getting the choice

            if choose == '1':
                self.insert_record_data(tablename)
                while True:
                    confirm = raw_input("Do you want to add another data ? (y/n) :").upper()
                    if confirm == 'Y':
                        self.insert_record_data(tablename)
                    else:
                        self.print_table_action(tablename)

            elif choose == '2':
                self.update_record_data(tablename)

            elif choose == '3':
                self.delete_record_data(tablename)

            elif choose == '4':
                delete = raw_input("Are you sure want to drop the table ? (y/n)").upper()
                if delete == 'Y':
                    self.delete_table_data(tablename)
                else:
                    pass

            elif choose == '5':
                if self.add_column_data(tablename):
                    self.print_table_action(tablename)

            elif choose == '6':
                if settings.get_database() == "sqlite":
                    print "You can not delete column in SQLite"
                else:
                    if self.delete_column_data(tablename):
                        self.print_table_action(tablename)

            elif choose == '7':
                self.show_table_data()

            elif choose == '8':
                close = raw_input("Are you sure want to close database ? (y/n) :").upper()
                if close == 'Y':
                    conn.close_database()
                    self.print_home()
                else:
                    pass

            elif choose == 'exit':
                conn.close_database()
                exit(0)  # exit to close application


data = Database()
data.choose_database()