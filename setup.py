"""
Flask-MySQLdb
----------------

MySQLdb extension for Flask
"""
from setuptools import setup


setup(
    name='Flask-MySQLdb',
    version='0.2.0',
    url='https://github.com/admiralobvious/flask-mysqldb',
    license='MIT',
    author='Alexandre Ferland',
    author_email='aferlandqc@gmail.com',
    description='MySQLdb extension for Flask',
    long_description=__doc__,
    packages=['flask_mysqldb'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.10',
        'mysqlclient'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
