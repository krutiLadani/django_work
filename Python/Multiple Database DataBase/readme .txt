***********************************************************************
           		 Database Application 
***********************************************************************

This is an Application where you can manage database using multiple
databases like MySQl, SQLite or PostGreSQL,Where You can

1. Create Database
2. Open / Drop Existing Database
3. CURD Operations on Table

::: Requirements :::
    
*_* Install Python *_*
	
	http://tecadmin.net/install-python-3-4-on-ubuntu-and-linuxmint/

*_* MySQL *_*

	$ sudo apt-get purge mysql-client-core-5.6
	$ sudo apt-get autoremove
	$ sudo apt-get autoclean
	$ sudo apt-get install mysql-client-core-5.5
	$ sudo apt-get install mysql-server

*_* SQLite *_*

	$ sudo apt-get install sqlite3 libsqlite3-dev

*_* PostGreSQL *_*

	$ sudo apt-get install python-pip python-dev 
	$ sudo apt-get install libpq-dev postgresql postgresql-contrib
	$ pip install django psycopg2

*_* PrettyTable *_*
	
	$ sudo apt-get update
	$ sudo apt-get install python-prettytable

::: How TO Run :::

	-> Open Terminal and Goto the directory where all files are places
	-> e.g $ cd Desktop/DatabaseApp
	-> Type $ python main.py , Press Enter 


