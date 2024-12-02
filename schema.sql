/* A sketch for the database */


-- guide is a general guide for the exercise that is shown before the exercise begins
CREATE TABLE Exercises
(
    id INTEGER PRIMARY KEY,
    name TEXT,
    guide TEXT
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
    correct_answers INTEGER,
    tests_completed INTEGER
);
