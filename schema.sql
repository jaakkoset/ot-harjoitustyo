/* A sketch for the database */


-- guide is a general guide for the exercise that is shown before the exercise begins
CREATE TABLE Exercise
(
    id SERIAL PRIMARY KEY,
    name TEXT,
    guide TEXT
);

CREATE TABLE Question
(
    id SERIAL PRIMARY KEY,
    exercise_id INTEGER REFERENCES Exercise,
    question TEXT
);

CREATE TABLE Answer
(
    id SERIAL PRIMARY KEY,
    question_id INTEGER REFERENCES Exercise,
    answer TEXT
);

CREATE TABLE Stats
(
    id SERIAL PRIMARY KEY,
    correct_answers INTEGER,
    tests_completed INTEGER,
);
