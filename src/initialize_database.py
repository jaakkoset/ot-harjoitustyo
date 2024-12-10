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
            guide TEXT,
            type TEXT
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
            correct_word_test_answers INTEGER,
            wrong_word_test_answers INTEGER,
            word_tests_completed INTEGER
        );
    """
    )

    connection.commit()


def add_word_test_1(connection):
    """Add data to the database"""
    words = [
        {"question": "puella", "answers": ("tyttö",)},
        {
            "question": "puer",
            "answers": (
                "poika",
                "lapsi",
            ),
        },
        {"question": "bellum", "answers": ("sota",)},
        {"question": "rēx", "answers": ("kuningas",)},
    ]
    info = {
        "name": "Helppo sanakoe",
        "guide": "Suomenna annetut sanat",
        "type": "word test",
    }
    insert_exercise_data(connection, words, info)


def add_word_test_2(connection):
    """Add data to the database"""
    words = [
        {"question": "lītus", "answers": ("ranta",)},
        {"question": "nāvis", "answers": ("laiva",)},
        {"question": "mare", "answers": ("meri",)},
        {"question": "bonus", "answers": ("hyvä",)},
        {
            "question": "parō",
            "answers": (
                "valmistaa",
                "valmistautua",
            ),
        },
        {"question": "audiō", "answers": ("kuulla",)},
    ]
    info = {
        "name": "Vaikea sanakoe",
        "guide": "Suomenna annetut sanat",
        "type": "word test",
    }
    insert_exercise_data(connection, words, info)


def insert_exercise_data(connection, questions: list[dict], info: dict):
    """Inserts given exercise data into the database."""
    cursor = connection.cursor()

    cursor.execute(
        """
            INSERT INTO Exercises
                (name, guide, type)
            VALUES
                (?, ?, ?);
            """,
        (info["name"], info["guide"], info["type"]),
    )
    exercise_id = cursor.lastrowid

    for question in questions:

        cursor.execute(
            """
            INSERT INTO Questions
                (exercise_id, question)
            VALUES
                (?, ?);
            """,
            (exercise_id, question["question"]),
        )

        question_id = cursor.lastrowid

        for answer in question["answers"]:
            cursor.execute(
                """
                INSERT INTO Answers
                    (question_id, answer)
                VALUES
                    (?, ?);
                """,
                (question_id, answer),
            )

    connection.commit()


def add_a_row_to_stats(connection):
    """Creates the first row of the Stats table. It is the only row needed"""
    cursor = connection.cursor()

    cursor.execute(
        """
            INSERT INTO Stats
                (correct_word_test_answers,
                wrong_word_test_answers,
                word_tests_completed)
            VALUES
                (0, 0, 0);
            """,
    )
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
    print("Add word test 2")
    add_word_test_2(connection)
    print("Add a row to Stats")
    add_a_row_to_stats(connection)


if __name__ == "__main__":
    initialize_database()
