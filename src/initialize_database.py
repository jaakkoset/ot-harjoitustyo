"""Functions for clearing and initializing the database"""

from database_connection import get_database_connection


def drop_tables(connection):
    """Delete all tables in the database if they exist"""
    cursor = connection.cursor()

    cursor.execute("""DROP TABLE IF EXISTS Words;""")

    cursor.execute("""DROP TABLE IF EXISTS Translations;""")

    connection.commit()


def create_tables(connection):
    """Create all tables"""
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE Words
        (
            id INTEGER PRIMARY KEY,
            word TEXT,
            inflection TEXT
        );
    """
    )

    cursor.execute(
        """
        CREATE TABLE Translations
        (
            id INTEGER PRIMARY KEY,
            word_id INTEGER REFERENCES Word,
            translation TEXT
        );
    """
    )

    connection.commit()


def add_test_data(connection):
    """Add data to the database"""
    words = [
        ("puella", ("tyttö",)),
        ("colōnus", ("maanviljelijä",)),
        (
            "puer",
            (
                "poika",
                "lapsi",
            ),
        ),
    ]

    for word in words:
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO 
            Words
                (word, inflection)
            VALUES
                (?, ?);
            """,
            (word[0], "lemma"),
        )

        last_id = cursor.lastrowid

        for translation in word[1]:
            cursor.execute(
                """
                INSERT INTO 
                Translations
                    (word_id, translation)
                VALUES
                    (?, ?);
                """,
                (last_id, translation),
            )

        connection.commit()


def initialize_database():
    """Delete all tables if they exist and recreate them"""
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)
    add_test_data(connection)


if __name__ == "__main__":
    initialize_database()
