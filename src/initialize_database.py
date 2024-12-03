"""Functions for clearing and initializing the database"""

from database_connection import get_database_connection


def drop_tables(connection):
    """Delete all tables in the database if they exist"""
    cursor = connection.cursor()

    cursor.execute("""DROP TABLE IF EXISTS Exercises;""")

    cursor.execute("""DROP TABLE IF EXISTS Questions;""")

    cursor.execute("""DROP TABLE IF EXISTS Answers;""")

    cursor.execute("""DROP TABLE IF EXISTS Stats;""")

    connection.commit()


def create_tables(connection):
    """Create all tables"""
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE Exercises
        (
            id INTEGER PRIMARY KEY,
            name TEXT,
            guide TEXT
        );
    """
    )

    cursor.execute(
        """
        CREATE TABLE Questions
        (
            id INTEGER PRIMARY KEY,
            exercise_id INTEGER REFERENCES Exercise,
            question TEXT
        );
    """
    )

    cursor.execute(
        """
        CREATE TABLE Answers
        (
            id INTEGER PRIMARY KEY,
            question_id INTEGER REFERENCES Exercise,
            answer TEXT
        );
    """
    )

    cursor.execute(
        """
        CREATE TABLE Stats
        (
            id INTEGER PRIMARY KEY,
            correct_answers INTEGER,
            tests_completed INTEGER
        );
    """
    )

    connection.commit()


def add_word_test_1(connection):
    """Add data to the database"""
    words = [
        {"latin": "puella", "translations": ("tyttö",)},
        {
            "latin": "puer",
            "translations": (
                "poika",
                "lapsi",
            ),
        },
        {"latin": "bellum", "translations": ("sota",)},
        {"latin": "rēx", "translations": ("kuningas",)},
    ]
    cursor = connection.cursor()

    cursor.execute(
        """
            INSERT INTO Exercises
                (name, guide)
            VALUES
                ("Helppo Sanakoe", "Suomenna annetut sanat");
            """
    )
    exercise_id = cursor.lastrowid

    for word in words:

        cursor.execute(
            """
            INSERT INTO Questions
                (exercise_id, question)
            VALUES
                (?, ?);
            """,
            (exercise_id, word["latin"]),
        )
        #print("INSERT INTO Questions", word["latin"])
        question_id = cursor.lastrowid

        for answer in word["translations"]:
            cursor.execute(
                """
                INSERT INTO Answers
                    (question_id, answer)
                VALUES
                    (?, ?);
                """,
                (question_id, answer),
            )
            #print("INSERT INTO Answers", answer)

    connection.commit()


def initialize_database():
    """Delete all tables if they exist and recreate them"""
    connection = get_database_connection()

    print("Drop tables")
    drop_tables(connection)
    print("Create tables")
    create_tables(connection)
    print("Add word test 1")
    add_word_test_1(connection)


if __name__ == "__main__":
    initialize_database()
