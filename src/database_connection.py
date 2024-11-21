import os
import sqlite3
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)
load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))

connection = sqlite3.connect(
    os.path.join(dirname, "..", "data", os.getenv("DATABASE_FILENAME"))
)
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection
