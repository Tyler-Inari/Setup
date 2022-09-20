import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

MYSQL_HOST = os.environ.get("MYSQL_HOST")
MYSQL_PORT = os.environ.get("MYSQL_PORT")
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE")
MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
print(
    f"MYSQL_HOST: {MYSQL_HOST}, MYSQL_PORT: {MYSQL_PORT}, MYSQL_DATABASE: {MYSQL_DATABASE}, MYSQL_USER: {MYSQL_USER}"
)

print("START CONNECT")
mydb = mysql.connector.connect(
    # host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DATABASE
    # host="fastapi-db-1", port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DATABASE
    # host="fastapi-db-1", port=MYSQL_PORT, user='root', password=MYSQL_PASSWORD, database=MYSQL_DATABASE
    host="fastapi-db-1",
    port=MYSQL_PORT,
    user="root",
    password=MYSQL_PASSWORD  # , database=MYSQL_DATABASE
    # host="fastapi-db-1", port=MYSQL_PORT, user=MYSQL_USER, password="password", database=MYSQL_DATABASE
)
print("DONE")
