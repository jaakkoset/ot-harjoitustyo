"""Functions for clearing and initializing the database"""

from database_connection import get_database_connection


def drop_tables(connection):
    """Delete all tables in the database"""
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS Word;
    ''')

    cursor.execute('''
        DROP TABLE IF EXISTS Translations;
    ''')

    connection.commit()


def create_tables(connection):
    """Create all tables"""
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE Word
        (
            id SERIAL PRIMARY KEY,
            word TEXT,
            inflection TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE Translation
        (
            id SERIAL PRIMARY KEY,
            word_id INTEGER REFERENCES Word,
            translation TEXT
        );
    ''')

    connection.commit()


def initialize_database():
    """Delete all tables if they exist and recreate them"""
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
