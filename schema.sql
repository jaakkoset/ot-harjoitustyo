/* A sketch for the database */


-- guide is a general guide for the exercise that is shown before the exercise begins.
-- type is the type of the exercise, e.g. a word test.
CREATE TABLE Exercises
(
    id INTEGER PRIMARY KEY,
    name TEXT,
    guide TEXT,
    type TEXT
);

CREATE TABLE Questions
(
    id INTEGER PRIMARY KEY,
    exercise_id INTEGER REFERENCES Exercise,
    question TEXT
);

CREATE TABLE Answers
(
    id INTEGER PRIMARY KEY,
    question_id INTEGER REFERENCES Exercise,
    answer TEXT
);

CREATE TABLE Stats
(
    id INTEGER PRIMARY KEY,
    correct_word_test_answers INTEGER,
    wrong_word_test_answers INTEGER,
    word_tests_completed INTEGER
);
