"""
Flask-MySQLdb
----------------

MySQLdb extension for Flask
"""
from setuptools import setup


setup(
    name="Flask-MySQLdb",
    version="1.0.0",
    url="https://github.com/admiralobvious/flask-mysqldb",
    license="MIT",
    author="Alexandre Ferland",
    author_email="me@alexferl.com",
    description="MySQLdb extension for Flask",
    long_description=__doc__,
    packages=["flask_mysqldb"],
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    install_requires=["Flask>=0.12.4", "mysqlclient>=1.3.7"],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
