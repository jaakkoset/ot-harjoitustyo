from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists Word;
    ''')

    cursor.execute('''
        drop table if exists Translations;
    ''')

    connection.commit()


def create_tables(connection):
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
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
