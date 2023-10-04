"""
Flask-MySQLdb
----------------

MySQLdb extension for Flask
"""
from setuptools import setup

from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name="Flask-MySQLdb",
    version="2.0.0",
    url="https://github.com/alexferl/flask-mysqldb",
    license="MIT",
    author="Alexandre Ferland",
    author_email="me@alexferl.com",
    description="MySQLdb extension for Flask",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["flask_mysqldb"],
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    install_requires=["Flask>=1.0.4", "mysqlclient>=2.2.0"],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
