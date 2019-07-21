from flask import Flask, redirect, request, render_template
from psycopg2 import connect, OperationalError
​
​
app = Flask(__name__)
​
​
def create_connection():
    username = "postgres"
    passwd = "coderslab"
    hostname = "localhost"  # lub "localhost"
    db_name = "chat"
    try:
        cnx = connect(user=username, password=passwd, host=hostname, database=db_name)
        print("Połączenie udane.")
        return cnx
    except OperationalError:
        print("Nieudane połączenie.")
        return None

