# Ohjelman arkkitehtuuri

## Luokkakaavio

```mermaid
classDiagram
    Ui -- MainMenu
    Ui -- ExerciseUI
    Ui -- SelectExercise
    Ui -- StatisticsUI

    StatisticsUI -- StatisticsService
    SelectExercise -- ExercisesService
    ExerciseUI -- WordTestService
    Exercise ..> ExerciseRepository
    WordTestService -- Exercise
    WordTestService -- StatsRepository
    ExercisesService -- ExerciseRepository
    
    StatisticsService -- StatsRepository
    ExerciseRepository
    StatsRepository
```

Luokka UI on ylin käyttöliittymästä vastaava luokka ja se avaa näkymät, jotka käyttäjä näkee. MainMenu vastaa päävälikon/etusivun näkymästä. SelectExercise vastaa näkymästä, jossa käyttäjä voi valita harjoitukse. ExerciseUI vastaa kokeen näkymästä ja StatisticsUI vastaa sivusta, jolla näkyy tilastot.

Luokka Exercise sisältää meneillään olevan harjoituksen kysymykset ja vastaukset. Kun siitä luodaan uusi olio, se hakee harjoituksen tiedot ExerciseRepositorystä harjoituksen id-numeron perusteella.
WordTestService sisältää sanakokeiden ohjelmalogiikan. StatisticsService hakee tilastotiedot ja muokkaa ne valmiiksi tulostettavaan muotoon. ExercisesService hakee tietokannasta kaikki harjoitukset listana.

ExerciseRepository hakee harjoituksen tietoja tietokannasta. StatsRepository tallentaa ja hakee tilastoja tietokannasta.

## Sekvenssikaavio

Alla oleva sekvenssikaavio kuvaa tapahtumia, kun käyttäjä haluaa tehdä sanakokeen. Alussa käyttäjä on alkuvalikossa ja kaavio loppuu siihen, kun ohjelma odottaa käyttäjältä vastausta ensimmäiseen kysymykseen. WordTestin metodissa choose_word_test() käyttäjä myös valitsee minkä sanakokeen hän haluaa tehdä vaikka sitä ei kaaviossa käydä läpi.

```mermaid
sequenceDiagram
    actor User
    participant Ui
    participant IOConsole
    participant CommandHandler
    participant WordTest
    participant Exercise
    participant ExerciseRepository

    User ->> Ui: enter 1 on terminal
    Ui ->> CommandHandler: get(1)
    CommandHandler ->> Ui: return WordTest
    Ui ->> WordTest: run()
    WordTest ->> WordTest: choose_word_test()
    WordTest ->> Exercise: word_test_id
    Exercise ->> ExerciseRepository: get_exercise_data(exercise_id)
    ExerciseRepository ->> Exercise: return exercise, all_exercise_questions
    WordTest ->> Exercise: question()
    Exercise ->> WordTest: return question
    WordTest ->> IOConsole: write()
    IOConsole ->> User: Suomenna sana: question
    WordTest ->> IOConsole: read()
    IOConsole ->> User:
```