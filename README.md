Flask-MySQLdb
================

[![Build Status](https://travis-ci.org/admiralobvious/flask-mysqldb.svg?branch=master)](https://travis-ci.org/admiralobvious/flask-mysqldb)

Flask-MySQLdb provides MySQL connection for Flask.

Quickstart
----------

First, install Flask-MySQLdb:
    
    $ pip install flask-mysqldb
    
Flask-MySQLdb depends, and will install for you, recent versions of Flask
(0.10.1 or later) and [mysqlclient](https://github.com/PyMySQL/mysqlclient-python). Flask-MySQLdb is compatible
with and tested on Python 2.7, 3.4 and 3.5.

Next, add a ``MySQL`` instance to your code:

```python
from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)


@app.route('/')
def users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT user, host FROM mysql.user''')
    rv = cur.fetchall()
    return str(rv)

if __name__ == '__main__':
    app.run(debug=True)
```


Resources
---------

- [Documentation](http://flask-mysqldb.readthedocs.org/en/latest/)
- [PyPI](https://pypi.python.org/pypi/Flask-MySQLdb)
