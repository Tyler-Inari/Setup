import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_NAME = os.environ.get("DB_NAME")
print(
    f"DB_HOST: {DB_HOST}, DB_PORT: {DB_PORT}, DB_USER: {DB_USER}, DB_PASS: {DB_PASS}, DB_NAME: {DB_NAME}"
)

print("START CONNECT")
mydb = mysql.connector.connect(
    DB_HOST="corpus-db", port=DB_PORT, user=DB_USER, password=DB_PASS, database=DB_NAME
)
print("DONE")
