.. Flask-MySQLdb documentation master file, created by
   sphinx-quickstart on Sat Feb  14 20:03:12 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Flask-MySQLdb's documentation!
=========================================

Flask-MySQLdb provides MySQL connection for Flask.


Quickstart
----------

First, you *may* need to install some dependencies for `mysqlclient <https://github.com/PyMySQL/mysqlclient)>`_
if you don't already have them, see `here <https://github.com/PyMySQL/mysqlclient#install>`_.

Second, install Flask-MySQLdb:

    .. code-block:: bash
      pip install flask-mysqldb

Flask-MySQLdb depends, and will install for you, recent versions of Flask
(0.12.4 or later) and `mysqlclient <https://github.com/PyMySQL/mysqlclient)>`_.
Flask-MySQLdb is compatible with and tested with Python 3.7+. It *should* work on any
version from Python 2.7 and up, but is not supported.

Next, add a :class:`~flask_mysqldb.MySQL` instance to your code:

    .. code-block:: python
      from flask import Flask
      from flask_mysqldb import MySQL

      app = Flask(__name__)

      # Required
      app.config["MYSQL_USER"] = "user"
      app.config["MYSQL_PASSWORD"] = "password"
      app.config["MYSQL_DB"] = "database"
      # Extra configs, optional:
      app.config["MYSQL_CURSORCLASS"] = "DictCursor"
      app.config["MYSQL_EXTRA_KWARGS"] = {"ssl": {"ca": "/path/to/ca-file"}}

      mysql = MySQL(app)

      @app.route("/")
      def users():
          cur = mysql.connection.cursor()
          cur.execute("""SELECT user, host FROM mysql.user""")
          rv = cur.fetchall()
          return str(rv)

      if __name__ == "__main__":
          app.run(debug=True)

Configuration
-------------

:class:`~flask_mysqldb.MySQL` understands the following configuration
directives:

============================ ===================================================
``MYSQL_HOST``               name of host to connect to.
                             Default: use the local host via a UNIX socket (where applicable)
``MYSQL_USER``               user to authenticate as. Default: current effective user.
``MYSQL_PASSWORD``           password to authenticate with. Default: no password.
``MYSQL_DB``                 database to use. Default: no default database.
``MYSQL_PORT``               TCP port of MySQL server. Default: 3306.
``MYSQL_UNIX_SOCKET``        location of UNIX socket. Default: use default location or TCP for remote hosts.
``MYSQL_CONNECT_TIMEOUT``    Abort if connect is not completed within given number of seconds.
                             Default: 10
``MYSQL_READ_DEFAULT_FILE``  MySQL configuration file to read; see the MySQL documentation for mysql_options().
``MYSQL_USE_UNICODE``        If True, CHAR and VARCHAR and TEXT columns are returned as Unicode strings,
                             using the configured character set.
``MYSQL_CHARSET``            If present, the connection character set will be changed to this character set,
                             if they are not equal. Default: 'utf-8'
``MYSQL_SQL_MODE``           If present, the session SQL mode will be set to the given string.
``MYSQL_CURSORCLASS``        If present, the cursor class will be set to the given string.
``MYSQL_AUTOCOMMIT``         If enabled, will use the autocommit feature of MySQL. Default: False
``MYSQL_EXTRA_KWARGS``       Use this to pass any extra directives that are not defined here. Default: None
============================ ===================================================


API
===

Classes
-------

.. autoclass:: flask_mysqldb.MySQL
   :members:


History
-------

Changes:

- 1.0.0: February 13, 2022

  - Added option for autocommit. Thanks to `@shaunpud <https://github.com/shaunpud>`_ on GitHub.
  - Added option to pass any extra configuration to mysqlclient.

- 0.2.0: September 5, 2015

  - Added option to change the cursor. Thanks to `@Sp1tF1r3 <https://github.com/Sp1tF1r3>`_ on GitHub.

- 0.1.1: February 14, 2015

  - Initial Release
