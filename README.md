Flask-MySQLdb [![Build Status](https://app.travis-ci.com/alexferl/flask-mysqldb.svg?branch=master)](https://app.travis-ci.com/alexferl/flask-mysqldb)
================

Flask-MySQLdb provides MySQL connection for Flask.

Quickstart
----------

First, you _may_ need to install some dependencies for [mysqlclient](https://github.com/PyMySQL/mysqlclient)
if you don't already have them, see [here](https://github.com/PyMySQL/mysqlclient#install).

Second, install Flask-MySQLdb:
```shell
pip install flask-mysqldb
```

Flask-MySQLdb depends, and will install for you, recent versions of Flask
(1.0.4 or later) and [mysqlclient](https://github.com/PyMySQL/mysqlclient).
Flask-MySQLdb is compatible with and tested with Python 3.8+.

Next, add a ``MySQL`` instance to your code:

```python
from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# Required
app.config["MYSQL_USER"] = "user"
app.config["MYSQL_PASSWORD"] = "password"
app.config["MYSQL_DB"] = "database"
# Extra configs, optional:
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
app.config["MYSQL_CUSTOM_OPTIONS"] = {"ssl": {"ca": "/path/to/ca-file"}}  # https://mysqlclient.readthedocs.io/user_guide.html#functions-and-attributes

mysql = MySQL(app)

@app.route("/")
def users():
    cur = mysql.connection.cursor()
    cur.execute("""SELECT user, host FROM mysql.user""")
    rv = cur.fetchall()
    return str(rv)

if __name__ == "__main__":
    app.run(debug=True)
```

Other configuration directives can be found [here](http://flask-mysqldb.readthedocs.io/en/latest/#configuration).

Why
---
Why would you want to use this extension versus just using MySQLdb by itself?
The only reason is that the extension was made using Flask's best practices in relation
to resources that need caching on the [app context](https://flask.palletsprojects.com/en/2.0.x/appcontext/).
What that means is that the extension will manage creating and teardown the connection to MySQL
for you while with if you were just using MySQLdb you would have to do it yourself.


Resources
---------

- [Documentation](http://flask-mysqldb.readthedocs.org/en/latest/)
- [PyPI](https://pypi.python.org/pypi/Flask-MySQLdb)
